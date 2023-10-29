Overview:
Scripts, support files, and output files for color analysis of images

TABLE OF CONTENTS:
---- main files ----
flickr_data_building(_lt).py - main files (stored on dropbox, run on different computers)
file_maip.py - custom module, holds two functions for flickr_data_building (getting next flickr ID from asset list and 
all_img_data.csv - primary output of color values. Is a dump of all class attributes, so some are unnecessary for processing
all_img_data_cc.csv - secondary output of color values when code was running on 2 computers
asset_list.csv - actively used during script. file is read in, an ID is randomly selected and removed, file is rewritten without selected value
column_names_defined.txt - descriptions of most columns in all_img_data. (may be slightly outdated)
exif_data.csv - exif data pulled from flickr during flickr_data_building.py
current_img.jpg - flickr img downloaded to here


---- Dev notebooks ----
exif_sourcing.ipynb - testing file for finding desired EXIF data from flickr api
flickr_working.ipynb - test notebook for working with flickr api/library
pillowy_goodness.ipynb - test notebook for image manipulation. this is where most of the do_img() code was developed
pymeanshift samples.psd - each layer is a sample of the pymeanshift process run on the same source image. layer names indicate the input variables used in the pymeanshift function, the number of color regions in the final product (output by the pymeanshift function, also saved in all_img_data as post_num_regions), and the number of seconds it took to run. 



---- other files --- 
asset_list_backup.txt - copy of the asset list prior to processing
column_names.txt - names only (may be slightly outdated)
current_page.txt - part of scraping flickr for valid images
dx_succulent_bricks.jpg - used for testing in "pillowy_goodness.ipynb"
calculating subimage coordinates)
flickr_sourcing.py - script for crawling my flickr photostream and saving the ids of images that met certain conditions
flickr.ipynb - old version of flickr_working
image_variables.txt - scratch paper from the development process
next steps.txt - notes to self during dev process
process.txt - scratch paper from dev process
real_assets_used.txt - list of processed images, should match IDs in exif_data and all_img_data
reject_list.txt - old, from the scraping phase
test_assets.csv/txt - old, used when testing flickr_data_building
test.ipynb - test file for whatever little extra thing I need