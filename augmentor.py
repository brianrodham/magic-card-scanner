import Augmentor

p = Augmentor.Pipeline(
    source_directory="./input",
    output_directory="../output")

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

# Generate and save 100 new images to the output directory.
p.sample(100)
