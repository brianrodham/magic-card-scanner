from generateDataset.imageNameHelper import ImageNameHelper
import json
from .csvWriter import CsvWriter
from .assetAugmentor import AssetAugmentor
from .imageNameHelper import ImageNameHelper
import requests
class AssetFetcher:

    csvWriter = CsvWriter()

    def Fetch(self):
        self.csvWriter.ResetCSVFile()
        with open("./default-cards.json", encoding="utf8") as file:
            reader = json.load(file)
            i = 0;
            for card in reader:
                if("image_uris" in card):
                    print(card["name"], card["image_uris"]["normal"])
                    url = card["image_uris"].get("normal")
                    # Download image
                    self.DownloadImage(url)

                    # Store useful data, including image name in a csv file for later use
                    self.csvWriter.WriteCSVRecord(card)
                    
                    # Temporary sanity check to work with a smaller dataset
                    i += 1
                    if(i >= 10):
                        break
        assetAugmentor = AssetAugmentor()
        assetAugmentor.Augment(100)

    def DownloadImage(self, url):
        img_data = requests.get(url).content
        image_name =  ImageNameHelper.GetImageName(url)
        image_url = "E:/magic-images/originals/" + image_name
        with open(image_url, 'wb') as handler:
            handler.write(img_data)




