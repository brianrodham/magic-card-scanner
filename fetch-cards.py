import json

#f = open('./default-cards.json')
#data = json.load(f)

with open("./default-cards.json", encoding="utf8") as file:
    reader = json.load(file)
    for card in reader:
        print(card["name"])
#print(len(data))
#for card in data:
#    print(card.name)


#def DownloadImage(url):
#    img_data = requests.get(url).content
#    image_name =  url.split('/')[-1]
#    image_url = "./output/" + image_name
#    with open(image_url, 'wb') as handler:
#        handler.write(img_data)