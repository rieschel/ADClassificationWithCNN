import tensorflow as tf
from tensorflow.keras import datasets, models, layers
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import nibabel as nib 
import os
from sklearn.utils import shuffle
import glob

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

for (root, dirs, files) in os.walk("./new data/cn"):
    i = 0
    for filename in files:
        if filename.endswith(".png"):
            image = Image.open('./new data/cn/' + filename)
            image = image.convert('RGB')
            image.thumbnail((224, 224))
            image.save("./new data/resized2/cn/resized_" + filename)
        else:
            continue
        i =+ 1
    print(i)