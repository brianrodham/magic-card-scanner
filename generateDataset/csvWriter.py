from .imageNameHelper import ImageNameHelper
import os

class CsvWriter:
    def ResetCSVFile(self, ):
        csvColumnNames = "id, tcgplayer_id, name, image_name\n"
        csv = self.OpenCSVFile("w")
        csv.write(csvColumnNames)
        csv.close()

    def WriteCSVRecord(self, card):
        id = card.get("id")
        tcgplayer_id = card.get("tcgplayer_id")
        name = card.get("name")
        url = card["image_uris"].get("normal")
        image_name = ImageNameHelper.GetImageName(url)
        with self.OpenCSVFile() as file:
            file.write(f'{id}, {tcgplayer_id}, {name}, {image_name}\n')

    def OpenCSVFile(self, mode="a"):
        csvFileName = "card-values.csv"
        return open(csvFileName, mode)