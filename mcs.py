import sys
from generateDataset.assetFetcher import AssetFetcher

assetFetcher = AssetFetcher()

command = sys.argv[1]

if command == "fetch":
    print("THIS COMMAND WILL CAUSE LARGE AMOUNTS OF DATA TO BE DOWNLOADED, AND WILL TAKE AN EXTENDED PERIOD OF TIME.")
    print("Proceed? (y/N)", end=' ')
    input = input()
    if input.lower() == 'y':
        assetFetcher.Fetch()
    else:
        print("Action canceled")

if command == "train":
    print("Not implemented yet")
    

