import flickrapi
import json
import requests
import numpy as np
from PIL import Image
import colorsys
import pandas as pd
import pymeanshift as pms
from file_manip import get_one_id, subimages
import csv
from time import time

GAMMA = 2.2


class FlickrData:
    def __init__(self):
        """Initializes the class, creating an authenticated connection to flickr"""
        api_key = "82fbf72fad4735faa2b9652df0961703"
        api_secret = "ef3b2eae6d3b0572"
        #        self.itesser_id = "40084484@N00"
        self.flickr = flickrapi.FlickrAPI(api_key, api_secret, format="json")
        self.flickr.authenticate_via_browser(perms="read")

    def manage_photo_list(self):
        self.using_id = get_one_id().strip(",")

    def do_exif(self):
        # preparation
        fetch_raw_exif = json.loads(
            self.flickr.photos.getExif(photo_id=self.using_id).decode("utf-8")
        )
        bulk_exif = fetch_raw_exif["photo"]["exif"]

        # defining the values we need and getting a dict ready
        tag_list = [
            "FlickrID",
            "DateTimeOriginal",
            "CreateDate",
            "ModifyDate",
            "Software",
            "LensInfo",
            "LensModel",
            "JFIFVersion",
            "ISO",
            "ExposureTime",
            "FNumber",
            "FocalLength",
            "FocalLengthIn35mmFormat",
            "BrightnessValue",
            "SubjectArea",
        ]
        pic_dict = dict.fromkeys(tag_list)

        # Adding everything to the dict
        pic_dict["FlickrID"] = self.using_id
        for item in bulk_exif:
            if item["tag"] in tag_list:
                pic_dict[item["tag"]] = item["raw"]["_content"]

        # append the dict to the exif CSV:
        with open(r"exif_data.csv", "a") as file:
            write = csv.writer(file)
            write.writerow(list(pic_dict.values()))

    def get_image(self):
        # connect to flickr, get the img url of the correct size
        img_sizes = json.loads(
            self.flickr.photos.getSizes(photo_id=self.using_id).decode("utf-8")
        )
        xl_img = img_sizes["sizes"]["size"][-3]
        xl_url = xl_img["source"]
        # download image and save locally.
        img_download = requests.get(xl_url).content
        self.img_loc = "current_img.jpg"
        with open(self.img_loc, "wb") as pic:
            pic.write(img_download)

    def load_image(self):
        # load the main file and set up for subimages
        with Image.open(self.img_loc) as self.the_image:
            self.the_image.load()
        dim = self.the_image.size
        self.img_width = dim[0]
        self.img_height = dim[1]

        # crop coords returns a list of 9 tuples, each containing subimage coordinates.
        # these will be referenced via loop to create subimages.
        self.crop_coords = subimages(self.img_width, self.img_height)

    def make_hue_vars(self):
        # making placeholder values in the right list structure
        return [
            ["frc", "vbrc", "vdrc"],
            ["foc", "vboc", "vdoc"],
            ["fyc", "vbyc", "vdyc"],
            ["fgc", "vbcg", "vdgc"],
            ["fcc", "vbcc", "vdcc"],
            ["fbc", "vbbc", "vdbc"],
            ["fpc", "vbpc", "vdpc"],
            ["fmc", "vbmc", "vdmc"],
        ]

    def assign_hue_vars(self, vals):
        self.full_red_count = vals[0][0]
        self.visib_red_count = vals[0][1]
        self.vivid_red_count = vals[0][2]
        self.full_orange_count = vals[1][0]
        self.visib_orange_count = vals[1][1]
        self.vivid_orange_count = vals[1][2]
        self.full_yellow_count = vals[2][0]
        self.visib_yellow_count = vals[2][1]
        self.vivid_yellow_count = vals[2][2]
        self.full_green_count = vals[3][0]
        self.visib_green_count = vals[3][1]
        self.vivid_green_count = vals[3][2]
        self.full_cyan_count = vals[4][0]
        self.visib_cyan_count = vals[4][1]
        self.vivid_cyan_count = vals[4][2]
        self.full_blue_count = vals[5][0]
        self.visib_blue_count = vals[5][1]
        self.vivid_blue_count = vals[5][2]
        self.full_purple_count = vals[6][0]
        self.visib_purple_count = vals[6][1]
        self.vivid_purple_count = vals[6][2]
        self.full_mag_count = vals[7][0]
        self.visib_mag_count = vals[7][1]
        self.vivid_mag_count = vals[7][2]

    def do_image(self, subimage=0):
        self.do_img_at = time()
        """
        Meat and potatoes of the gane. Reads in the image and processes it a few different ways:
        - linearize (apply gamma)
        - posterize/segment (apply mean shift filter with pymeanshift)
        - convert to HSL (Hue Saturation Lightness)

        Along the way, key values are saved to class attributes for exporting (to csv)

        Many variables have the prefix "c_" for "current image"
        This helped me to keep track of what code I was bringing over from testing notebooks.
        """

        def rgb_to_hsl(rgb):
            """
            Localised formula that converts RGB color values to HSL color values.
            Used on NP arrays.
            """
            r, g, b = rgb / 255
            h, l, s = colorsys.rgb_to_hls(r, g, b)
            return [h, s, l]

        if subimage == 0:
            c_img = self.the_image
            self.sub_img = subimage
        else:
            c_img = self.the_image.crop(self.crop_coords[subimage - 1])
            self.sub_img = subimage
            dim = c_img.size
            self.img_width = dim[0]
            self.img_height = dim[1]
        self.full_id = f"{self.using_id}0{subimage}"
        c_rgb_array = np.asarray(c_img)
        # rgb is given a gamma adjustment for linearization, then brough back into whole RGB numbers
        c_lin_rgb_arr = np.round((c_rgb_array / 255) ** (1 / GAMMA) * 255).astype(
            np.uint8
        )

        # branch to get rgb specific values
        c_lin_rgb_df = pd.DataFrame(
            c_lin_rgb_arr.reshape((c_lin_rgb_arr.shape[0] * c_lin_rgb_arr.shape[1]), 3)
        )
        c_lin_rgb_df.columns = ["red", "green", "blue"]
        c_lin_df_desc = c_lin_rgb_df.describe()
        self.r_min = c_lin_df_desc["red"].iloc[3]
        self.r_max = c_lin_df_desc["red"].iloc[7]
        self.r_mean = c_lin_df_desc["red"].iloc[1]
        self.r_mode = list(
            c_lin_rgb_df["red"].value_counts().sort_values(ascending=False).head(1)
        )[0]
        self.g_min = c_lin_df_desc["green"].iloc[3]
        self.g_max = c_lin_df_desc["green"].iloc[7]
        self.g_mean = c_lin_df_desc["green"].iloc[1]
        self.g_mode = list(
            c_lin_rgb_df["green"].value_counts().sort_values(ascending=False).head(1)
        )[0]
        self.b_min = c_lin_df_desc["blue"].iloc[3]
        self.b_max = c_lin_df_desc["blue"].iloc[7]
        self.b_mean = c_lin_df_desc["blue"].iloc[1]
        self.b_mode = list(
            c_lin_rgb_df["blue"].value_counts().sort_values(ascending=False).head(1)
        )[0]
        c_lin_rgb_df = 0
        # /end branch

        # get center pixel in rgb
        center_row = int(round(c_lin_rgb_arr.shape[0] / 2))
        center_col = int(round(c_lin_rgb_arr.shape[1] / 2))
        self.center_rgb = tuple(c_lin_rgb_arr[center_row, center_col, :])

        ## pymeanshift segmenting
        # turn linearized array back into image.
        lin_img = Image.fromarray(c_lin_rgb_arr)
        (segmented_image, labels_image, number_regions) = pms.segment(
            lin_img, spatial_radius=7, range_radius=7, min_density=450
        )
        self.post_num_regions = number_regions

        # turn segmented image to HSL values (and correct hue values)
        segment_hsl = np.apply_along_axis(rgb_to_hsl, axis=-1, arr=segmented_image)
        segment_hsl[:, :, 0] = segment_hsl[:, :, 0] * 360

        # reshaping to list of pixels
        seg_hsl_pixels = segment_hsl.reshape(
            (segment_hsl.shape[0] * segment_hsl.shape[1]), 3
        )

        # converting to dataframe
        seg_df = pd.DataFrame(seg_hsl_pixels)
        seg_df.columns = ["hue", "saturation", "lightness"]

        # combining rows to discrete pixels
        seg_hsl_tuples = [tuple(row) for row in seg_hsl_pixels]

        # adding tuples as a row in the dataframe
        seg_df["combined"] = seg_hsl_tuples

        # finding the 6 most common combined values and creating a dataframe of it.
        common_seg_df = (
            seg_df.value_counts("combined")
            .sort_values(ascending=False)
            .head(6)
            .to_frame()
            .reset_index()
        )

        # saving the values in that dataframe to variables
        self.post_top_hsl = common_seg_df["combined"].iloc[0]
        self.post_top_count = common_seg_df["count"].iloc[0]
        try:
            self.post_2_hsl = common_seg_df["combined"].iloc[1]
            self.post_2_count = common_seg_df["count"].iloc[1]
        except:
            self.post_2_hsl = None
            self.post_2_count = 0
        try:
            self.post_3_hsl = common_seg_df["combined"].iloc[2]
            self.post_3_count = common_seg_df["count"].iloc[2]
        except:
            self.post_3_hsl = None
            self.post_3_count = 0
        try:
            self.post_4_hsl = common_seg_df["combined"].iloc[3]
            self.post_4_count = common_seg_df["count"].iloc[3]
        except:
            self.post_4_hsl = None
            self.post_4_count = 0
        try:
            self.post_5_hsl = common_seg_df["combined"].iloc[4]
            self.post_5_count = common_seg_df["count"].iloc[4]
        except:
            self.post_5_hsl = None
            self.post_5_count = 0
        try:
            self.post_6_hsl = common_seg_df["combined"].iloc[5]
            self.post_6_count = common_seg_df["count"].iloc[5]
        except:
            self.post_6_hsl = None
            self.post_6_count = 0

        # zeroing out unneded vars
        lin_img = 0
        segmented_image = 0
        labels_image = 0
        segment_hsl = 0
        seg_hsl_pixels = 0
        seg_df = 0
        seg_hsl_tuples = 0
        # / pymeanshift section

        # HSL calculations for linearized image
        c_hsl_array = np.apply_along_axis(rgb_to_hsl, axis=-1, arr=c_lin_rgb_arr)
        c_hsl_array[:, :, 0] = c_hsl_array[:, :, 0] * 360
        self.center_hsl = list(c_hsl_array[center_row, center_col, :])

        # putting all the pixels in a blender then sorting them.
        # reshaping to HSL columns in numpy, then creating as dataframe with a combined pixel row.
        c_hsl_midstep = c_hsl_array.reshape(
            (c_hsl_array.shape[0] * c_hsl_array.shape[1]), 3
        )
        c_hsl_df = pd.DataFrame(c_hsl_midstep)
        c_hsl_df.columns = ["hue", "saturation", "lightness"]
        c_hsl_tuples = [tuple(row) for row in c_hsl_midstep]
        c_hsl_df["combined"] = c_hsl_tuples

        # slight detour to add color column so the dataframe is complete
        color_dict = {
            15: "red",
            35: "orange",
            80: "yellow",
            140: "green",
            215: "cyan",
            235: "blue",
            285: "purple",
            340: "mag",
            361: "red",
        }

        def color_conversion(hue):
            for key in color_dict.keys():
                if hue <= key:
                    return color_dict[key]

        c_hsl_df["color"] = c_hsl_df["hue"].apply(color_conversion)
        # /color detour.

        # super useful dataframe we will refer to a lot going forward
        c_hsl_desc = c_hsl_df.describe()

        ## hue/color details
        # make df of only pixels with discernable colors
        c_df_visible = c_hsl_df[
            (c_hsl_df["saturation"] >= 0.4)
            & (c_hsl_df["lightness"] >= 0.20)
            & (c_hsl_df["lightness"] <= 0.75)
        ]
        c_df_vivid = c_hsl_df[
            (c_hsl_df["saturation"] >= 0.7)
            & (c_hsl_df["lightness"] >= 0.30)
            & (c_hsl_df["lightness"] <= 0.70)
        ]

        # get dicts with counts of colors in misc ranges
        full_color_dict = dict(c_hsl_df["color"].value_counts())
        visible_color_dict = dict(c_df_visible["color"].value_counts())
        vivid_color_dict = dict(c_df_vivid["color"].value_counts())

        color_list = [
            "red",
            "orange",
            "yellow",
            "green",
            "cyan",
            "blue",
            "purple",
            "mag",
        ]
        var_list = self.make_hue_vars()
        for i in range(len(color_list)):
            try:
                var_list[i][0] = full_color_dict[color_list[i]]
            except:
                var_list[i][0] = 0
            try:
                var_list[i][1] = visible_color_dict[color_list[i]]
            except:
                var_list[i][1] = 0
            try:
                var_list[i][2] = vivid_color_dict[color_list[i]]
            except:
                var_list[i][2] = 0
        self.assign_hue_vars(var_list)

        self.vivid_count = c_hsl_df[
            (c_hsl_df["saturation"] >= 0.7)
            & (c_hsl_df["lightness"] >= 0.30)
            & (c_hsl_df["lightness"] <= 0.70)
        ].shape[0]

        # saturation details
        self.sat_min_val = c_hsl_desc["saturation"].iloc[3]
        self.sat_25_val = c_hsl_desc["saturation"].iloc[4]
        self.sat_50_val = c_hsl_desc["saturation"].iloc[5]
        self.sat_75_val = c_hsl_desc["saturation"].iloc[6]
        self.sat_max_val = c_hsl_desc["saturation"].iloc[7]

        # a couple things in weird order to have the three means together
        self.hue_mean_val = c_hsl_desc["hue"].iloc[1]
        self.sat_mean_val = c_hsl_desc["saturation"].iloc[1]

        # lightness details
        self.light_mean_val = c_hsl_desc["lightness"].iloc[1]
        self.light_max_val = c_hsl_desc["lightness"].iloc[7]
        self.light_max_count = c_hsl_df[
            c_hsl_df["lightness"] >= self.light_max_val - 0.015
        ].shape[0]
        self.light_min_val = c_hsl_desc["lightness"].iloc[3]
        self.light_min_count = c_hsl_df[
            c_hsl_df["lightness"] <= self.light_min_val + 0.015
        ].shape[0]
        self.light_25_value = c_hsl_desc["lightness"].iloc[4]
        self.light_50_value = c_hsl_desc["lightness"].iloc[5]
        self.light_75_value = c_hsl_desc["lightness"].iloc[6]
        self.gen_bright_count = c_hsl_df[c_hsl_df["lightness"] >= 0.85].shape[0]
        self.gen_dark_count = c_hsl_df[c_hsl_df["lightness"] <= 0.15].shape[0]

        # AT LONG LAST. Frequent Colors
        common_pix = (
            c_hsl_df.value_counts("combined")
            .sort_values(ascending=False)
            .head(4)
            .to_frame()
            .reset_index()
        )
        self.common_hsl_1_val = common_pix["combined"].iloc[0]
        self.common_hsl_1_count = common_pix["count"].iloc[0]
        try:
            self.common_hsl_2_val = common_pix["combined"].iloc[1]
        except:
            self.common_hsl_2_val = None
        try:
            self.common_hsl_2_count = common_pix["count"].iloc[1]
        except:
            self.common_hsl_2_count = 0
        try:
            self.common_hsl_3_val = common_pix["combined"].iloc[2]
        except:
            self.common_hsl_3_val = None
        try:
            self.common_hsl_3_count = common_pix["count"].iloc[2]
        except:
            self.common_hsl_3_count = 0
        try:
            self.common_hsl_4_val = common_pix["combined"].iloc[3]
        except:
            self.common_hsl_4_val = None
        try:
            self.common_hsl_4_count = common_pix["count"].iloc[3]
        except:
            self.common_hsl_4_count = 0

        # c_img.show() proved that subimaging works correctly
        # next step is to start walking through the array stuff!


doinit = FlickrData()
count = 0
while count < 420:
    doinit.manage_photo_list()  # works!
    doinit.do_exif()  # works!
    doinit.get_image()  # works!
    doinit.load_image()  # works!
    doinit.do_image()
    headers = list(vars(doinit).keys())
    with open("all_img_data_cc.csv", "a", newline="") as imgdata:
        writer = csv.DictWriter(imgdata, fieldnames=headers)
        writer.writerow(vars(doinit))
    for i in range(9):
        doinit.do_image(i + 1)
        headers = list(vars(doinit).keys())
        with open("all_img_data_cc.csv", "a", newline="") as imgdata:
            writer = csv.DictWriter(imgdata, fieldnames=headers)
            writer.writerow(vars(doinit))
    count += 1
