import tensorflow as tf
from keras.models import load_model
import numpy as np

def Apple(img_path):
    model = load_model('models/apple_vgg16.h5')
    class_names = ["scab","rot","Healthy"]
    img_array =  tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.expand_dims(img_array,0)
    vgg = model.predict(img_array)
    predicted_class = class_names[np.argmax(vgg[0])]
    return predicted_class

def Cherry(img_path):
    model = load_model('models/cherry_vgg16.h5')
    class_names = ["mildew","Healthy"]
    img_array =  tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.expand_dims(img_array,0)
    vgg = model.predict(img_array)
    predicted_class = class_names[np.argmax(vgg[0])]
    return predicted_class

def Grape(img_path):
    model = load_model('models/grape_vgg16.h5')
    class_names = ["Measels","Leaf Blight","Healthy"]
    img_array =  tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.expand_dims(img_array,0)
    vgg = model.predict(img_array)
    predicted_class = class_names[np.argmax(vgg[0])]
    return predicted_class

def Strawberry(img_path):
    model = load_model('models/strawberry_vgg16.h5')
    class_names = ["Leaf Scroch","Healthy"]
    img_array =  tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.expand_dims(img_array,0)
    vgg = model.predict(img_array)
    predicted_class = class_names[np.argmax(vgg[0])]
    return predicted_class

def Potato(img_path):
    model = load_model('models/Potato_vgg16.h5')
    class_names = ["Early Blight","Late Blight","Healthy"]
    img_array =  tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = tf.expand_dims(img_array,0)
    vgg = model.predict(img_array)
    predicted_class = class_names[np.argmax(vgg[0])]
    return predicted_class