from time import sleep
import flickrapi
import json


class GettingPhotos:
    def __init__(self):
        """Initializes the class, creating an authenticated connection to flickr"""
        api_key = "82fbf72fad4735faa2b9652df0961703"
        api_secret = "ef3b2eae6d3b0572"
        self.itesser_id = "40084484@N00"
        self.flickr = flickrapi.FlickrAPI(api_key, api_secret, format="json")
        self.flickr.authenticate_via_browser(perms="read")
        self.start_page = self.get_page()
        self.current_page = 0
        self.error_free = True

    def page_wrapper(self):
        """makes sure the contents of current-page.txt is saved as an attribute"""
        self.current_page = self.get_page()

    def get_page(self):
        """looks at the current page file and brings back its contents as an int."""
        with open("current_page.txt", "r") as page:
            page_read_in = int(page.read())
            return page_read_in

    def get_10_ids(self):
        """goes through the current page and collects all the flickr IDs."""
        photo_payload = self.flickr.photos.search(
            user_id=self.itesser_id, per_page=10, page=self.current_page
        ).decode("utf-8")
        photos = json.loads(photo_payload)  # all data from query
        reply_list = photos["photos"]["photo"]  # just the list of photo dicts
        self.ph_ids_from_page = []
        for i in range(len(reply_list)):
            self.ph_ids_from_page.append(reply_list[i]["id"])

    def update_page(self):
        """incremets current page and saves it to the txt file (allows this process to be run in succession)"""
        with open("current_page.txt", "w") as page:
            page.write(str(self.current_page + 1))

    def check_page_ids(self):
        """for each photo id on the most recent page, checks to see if has the correct kind of EXIF data to indicate it was taken by me."""
        for id in self.ph_ids_from_page:
            sleep(10)
            try:
                exif = json.loads(
                    self.flickr.photos.getExif(photo_id=id).decode("utf-8")
                )
            except:
                print(
                    f"process exited after crawling from {self.start_page} to {self.current_page}"
                )
                self.error_free = False
            if len(exif["photo"]["exif"]) < 1:
                self.reject_id(
                    id
                )  # this is just for fun, but helps to make sure the process is still running
            else:
                exif_list = exif["photo"]["exif"]
                for i in range(len(exif_list)):
                    if exif_list[i]["label"] == "ISO Speed":
                        self.append_id(id)

    def append_id(self, id):
        """images with the correct kind of exif data have their IDs saved to a file for processing later"""
        with open("asset_list.txt", "a") as file:
            file.write(f"{id},\n")

    def reject_id(self, id):
        with open("reject_list.txt", "a") as file:
            file.write(f"{id},\n")


ya = GettingPhotos()
while ya.current_page < 600:
    ya.page_wrapper()
    ya.get_10_ids()
    if ya.error_free == False:
        break
    ya.update_page()
    ya.check_page_ids()
