class ImageNameHelper:
    @staticmethod
    def GetImageName(url):
        image_name =  url.split('/')[-1]
        return image_name.split("?", 1)[0]
