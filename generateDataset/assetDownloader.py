import requests
from .imageNameHelper import ImageNameHelper

class AssetDownloader:
    def DownloadImage(self, url):
        img_data = requests.get(url).content
        image_name =  ImageNameHelper.GetImageName(url)
        image_url = "E:/magic-images/originals/" + image_name
        with open(image_url, 'wb') as handler:
            handler.write(img_data)