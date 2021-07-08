import json
from .csvWriter import CsvWriter
from .assetFetcher import AssetFetcher

csvWriter = CsvWriter()
assetFetcher = AssetFetcher()

class AssetFetcher:

    def Fetch(self):
        csvWriter.ResetCSVFile()
        with open("./default-cards.json", encoding="utf8") as file:
            reader = json.load(file)
            i = 0;
            for card in reader:
                if("image_uris" in card):
                    print(card["name"], card["image_uris"]["normal"])
                    url = card["image_uris"].get("normal")
                    # Download image
                    self.assetFetcher.DownloadImage(url)

                    # Store useful data, including image name in a csv file for later use
                    self.csvWriter.WriteCSVRecord(card)
                    
                    # Temporary sanity check to work with a smaller dataset
                    i += 1
                    if(i >= 10):
                        break

                




