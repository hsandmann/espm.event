import os
import sys

import tensorflow as tf
import tensorflow_hub as hub

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DIR_STYLE = os.path.join(DIR_PATH, 'styles')
DIR_PHOTO = os.path.join(DIR_PATH, 'in')
DIR_ART = os.path.join(DIR_PATH, 'out')
DIR_WEIGHTS = os.path.join(DIR_PATH, 'weights')

style_file = lambda name, ext='jpg': os.path.join(DIR_STYLE, f'{name}.{ext}')
photo_file = lambda name, ext='jpg': os.path.join(DIR_PHOTO, f'{name}.{ext}')
art_file = lambda name, ext='jpg': os.path.join(DIR_ART, f'{name}.{ext}')

def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)

def load_img(path_to_img):
    max_dim = 512
    img = tf.io.read_file(path_to_img)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    return img

def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)

def printHelp():
    print('usage:')
    print('')
    print('   python3 main.py <filename> <style>')
    print('')
    print('   <filename>  name of jpg image file from directory [photos], WITHOUT extesion')
    print('   <style>     choice one in directory [styles], ONLY NAME')
    print('')
    exit()

if '--help' in sys.argv:
    printHelp()
    exit(0)
elif len(sys.argv) != 3:
    print()
    print('---> WRONG COMMAND')
    print()
    printHelp()
    exit(1)

photo = sys.argv[1]
style = sys.argv[2]
result = art_file(f'{photo}.{style}')

print(f'Applying {style} on {photo} -> {result}')

hub_module = hub.load(f'file:///{DIR_WEIGHTS}/magenta_arbitrary-image-stylization-v1-256_2')
stylized_image = hub_module(tf.constant(load_img(photo_file(photo))), tf.constant(load_img(style_file(style))))[0]
dataimg = tensor_to_image(stylized_image)
dataimg.save(result)
