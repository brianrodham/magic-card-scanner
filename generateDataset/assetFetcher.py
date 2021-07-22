import os
from generateDataset.imageNameHelper import ImageNameHelper
import json
from .csvWriter import CsvWriter
from .assetAugmentor import AssetAugmentor
from .imageNameHelper import ImageNameHelper
import requests
import urllib
class AssetFetcher:

    csvWriter = CsvWriter()
    sanityCheck = True
    sanityBreakpoint = 10
    augmentCount = 100

    baseUrl = "E:/magic-images/originals/"

    def Fetch(self):
        self.csvWriter.ResetCSVFile()
        with open("./default-cards.json", encoding="utf8") as file:
            reader = json.load(file)
            i = 0;
            for card in reader:
                if("image_uris" in card):
                   # print(card["name"], card["image_uris"]["normal"])
                    url = card["image_uris"].get("normal")
                    name = card["name"];
                    # Download image
                    self.DownloadImage(url, name)

                    # Store useful data, including image name in a csv file for later use
                    self.csvWriter.WriteCSVRecord(card)
                    
                    # Sanity check to work with a smaller dataset
                    i += 1
                    if(i >= self.sanityBreakpoint and self.sanityCheck):
                        break
                    
        assetAugmentor = AssetAugmentor()
        assetAugmentor.Augment(self.augmentCount)

    def DownloadImage(self, url, name):
        img_data = requests.get(url).content
        image_guid =  ImageNameHelper.GetImageName(url)
        name = name.replace('/', '_')
        cardDirectory = self.baseUrl + name;
        if not os.path.exists(cardDirectory):
            os.makedirs(cardDirectory)

        image_url = cardDirectory + "/" + image_guid
        with open(image_url, 'wb') as handler:
            handler.write(img_data)




