import json
import requests

def DownloadImage(url):
    img_data = requests.get(url).content
    image_name =  url.split('/')[-1]
    image_name = image_name.split("?", 1)[0]
    image_url = "E:/magic-images/originals/" + image_name
    with open(image_url, 'wb') as handler:
        handler.write(img_data)

with open("./default-cards.json", encoding="utf8") as file:
    reader = json.load(file)
    i = 0;
    for card in reader:
        if("image_uris" in card):
            print(card["name"], card["image_uris"]["normal"])
            # Get all useful information
            id = card.get("id")
            tcgplayer_id = card.get("tcgplayer_id")
            name = card.get("name")
            url = card["image_uris"].get("normal")

            # Download image
            DownloadImage(url)
            
            
            # Temporary sanity check to work with a smaller dataset
            i += 1
            if(i >= 10):
                break

            # Store useful data, including image name in a csv file for later use



