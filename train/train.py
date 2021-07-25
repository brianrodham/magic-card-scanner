import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib
dataset_url = "E:/magic-images/augmented"
data_dir = pathlib.Path(dataset_url)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)