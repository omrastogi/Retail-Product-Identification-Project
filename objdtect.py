import numpy as np
import time
import cv2

import PIL.Image as Image

import tensorflow as tf
import tensorflow_hub as hub

IMAGE_SHAPE = (224, 224)
classifier_model = 'tf2-preview_mobilenet_v2_classification_4/'
classifier = tf.keras.Sequential([
    hub.KerasLayer(classifier_model, input_shape=IMAGE_SHAPE+(3,))
])
labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','')
imagenet_labels = np.array(open(labels_path).read().splitlines())

def give_class(img):
    IMAGE_SHAPE = (224, 224)
    img = cv2.resize(img,IMAGE_SHAPE,interpolation = cv2.INTER_NEAREST)
    img = np.array(img)/255.0
    result = classifier.predict(img[np.newaxis, ...])
    predicted_class = np.argmax(result[0], axis=-1)
    predicted_class_name = imagenet_labels[predicted_class]
    return (predicted_class_name)
