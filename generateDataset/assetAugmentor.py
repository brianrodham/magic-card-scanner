import Augmentor
import os
class AssetAugmentor:

    originalsBaseDir = "E:/magic-images/originals"
    augmentedBaseDir = "E:/magic-images/augmented"
    # Generate and save X new images to the output directory.
    def Augment(self, sampleSize):
        for dir in os.listdir(self.originalsBaseDir):
            p = self.buildPipeline(dir)
            p.sample(sampleSize)

    def buildPipeline(self, dir):
        p = Augmentor.Pipeline(
            source_directory= self.originalsBaseDir + "/" + dir,
            output_directory= self.augmentedBaseDir + "/" + dir)

        # Manipulate the example card.
        p.rotate_without_crop(
            probability=.5,
            max_left_rotation=10,
            max_right_rotation=10,
            expand=True)
        p.zoom(
            probability=.3,
            min_factor=.8,
            max_factor=1.1)
        p.skew(
            probability=.3,
            magnitude=.15)
        p.random_brightness(
            probability=.5,
            min_factor=.5,
            max_factor=1.75)
        return p

# https://c2.scryfall.com/file/scryfall-bulk/default-cards/default-cards-20210601210412.json