import Augmentor
import os
class AssetAugmentor:

    originalsBaseDir = "E:/magic-images/originals"
    augmentedBaseDir = "E:/magic-images/augmented"

    augmentCount = 500


    # Generate and save X new images to the output directory.
    def Augment(self):
        for dir in os.listdir(self.originalsBaseDir):
            sampleSize = self.GetFileCount(dir);
            p = self.BuildPipeline(dir)
            p.sample(sampleSize * self.augmentCount)

    def BuildPipeline(self, dir):
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
    
    def GetFileCount(self, dir):
        path = self.originalsBaseDir + "/" + dir
        return len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

# https://c2.scryfall.com/file/scryfall-bulk/default-cards/default-cards-20210601210412.json