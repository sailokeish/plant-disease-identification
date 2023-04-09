from flask import Flask, render_template, jsonify, request, Markup
from model import predict_image
import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/products",methods=["POST","GET"])
def product():
    
    return render_template("product.html")

@app.route("/about")
def about():
    
    return render_template("aboutus.html")

@app.route("/diseases")
def diseases():
    
    return render_template("disease.html")
    
@app.route("/description")
def description():
    
    return render_template("description.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('display.html', status=200, result=res)
        except:
            pass
    return render_template('index.html', status=500, res="Internal Server Error")


if __name__ == "__main__":
    app.run(debug=True)
