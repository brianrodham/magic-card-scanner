import Augmentor

class AssetAugmentor:
    p = Augmentor.Pipeline(
        source_directory="E:/magic-images/originals",
        output_directory="E:/magic-images/augmented")

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

    # Generate and save X new images to the output directory.
    def Augment(self, sampleSize):
        self.p.sample(sampleSize)


# https://c2.scryfall.com/file/scryfall-bulk/default-cards/default-cards-20210601210412.json