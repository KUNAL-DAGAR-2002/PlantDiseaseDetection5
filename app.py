from flask import Flask,request,render_template
from predicttion import Apple,Cherry,Grape,Potato,Strawberry
import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np
import os

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apple")
def apple():
    return render_template("apple.html")

@app.route("/cherry")
def cherry():
    return render_template("cherry.html")

@app.route("/grape")
def grape():
    return render_template("grape.html")

@app.route("/potato")
def potato():
    return render_template("potato.html")

@app.route("/strawberry")
def strawberry():
    return render_template("strawberry.html")

@app.route("/submitApple", methods=['POST'])
def get_output_apple():

    if request.method == 'POST':
        image = request.files['my_image']
        img_path = "static/" + image.filename
        image.save(img_path)
        prediction = Apple(img_path)
            
        os.makedirs(f"static/Apple/{prediction}", exist_ok=True)

        # Move the uploaded image to the subfolder within the "Apple" folder
        new_img_path = f"static/Apple/{prediction}/{image.filename}"
        os.rename(img_path, new_img_path)
    return render_template("apple.html", prediction = prediction, img_path = new_img_path)
    
        

@app.route("/submitCherry", methods=['POST'])
def get_output_cherry():
    if request.method == 'POST':
        image = request.files['my_image']
        img_path = "static/" + image.filename
        image.save(img_path)
        prediction = Cherry(img_path=img_path)
        os.makedirs(f"static/Cherry/{prediction}", exist_ok=True)

        # Move the uploaded image to the subfolder within the "Apple" folder
        new_img_path = f"static/Cherry/{prediction}/{image.filename}"
        os.rename(img_path, new_img_path)

    return render_template("cherry.html", prediction = prediction, img_path = new_img_path)

@app.route("/submitGrape", methods=['POST'])
def get_output_grape():
    if request.method == 'POST':
        image = request.files['my_image']
        img_path = "static/" + image.filename
        image.save(img_path)
        prediction = Grape(img_path=img_path)
        os.makedirs(f"static/Grape/{prediction}", exist_ok=True)

        # Move the uploaded image to the subfolder within the "Apple" folder
        new_img_path = f"static/Grape/{prediction}/{image.filename}"
        os.rename(img_path, new_img_path)

    return render_template("grape.html", prediction = prediction, img_path = new_img_path)

@app.route("/submitPotato", methods=['POST'])
def get_output_potato():
    if request.method == 'POST':
        image = request.files['my_image']
        img_path = "static/" + image.filename
        image.save(img_path)
        prediction = Potato(img_path=img_path)
        os.makedirs(f"static/Potato/{prediction}", exist_ok=True)

        # Move the uploaded image to the subfolder within the "Apple" folder
        new_img_path = f"static/Potato/{prediction}/{image.filename}"
        os.rename(img_path, new_img_path)

    return render_template("potato.html", prediction = prediction, img_path = new_img_path)

@app.route("/submitStrawberry", methods=['POST'])
def get_output_strawberry():
    if request.method == 'POST':
        image = request.files['my_image']
        img_path = "static/" + image.filename
        image.save(img_path)
        prediction = Strawberry(img_path=img_path)
        os.makedirs(f"static/Strawberry/{prediction}", exist_ok=True)

        # Move the uploaded image to the subfolder within the "Apple" folder
        new_img_path = f"static/Strawberry/{prediction}/{image.filename}"
        os.rename(img_path, new_img_path)

    return render_template("strawberry.html", prediction = prediction, img_path = new_img_path)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)