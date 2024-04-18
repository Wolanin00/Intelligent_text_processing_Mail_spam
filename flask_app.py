import pickle
from flask import Flask, render_template, request, jsonify
from pathlib import Path
import os
import signal

app = Flask(__name__)

# Load the saved model
with open(Path(__file__).resolve().parent / "best_model.pkl", "rb") as f:
    svm_classifier = pickle.load(f)

with open(Path(__file__).resolve().parent / "vectorizer_model.pkl", "rb") as f:
    vectorizer = pickle.load(f)


@app.route("/")
def index():
    """
    index
    """
    return render_template("index.html")


@app.route("/classify", methods=["POST"])
def classify():
    """
    classify
    """
    email_text = request.form["email_text"]

    if not email_text.strip():
        return jsonify({"result": "Please enter your email text."})

    email_vectorized = vectorizer.transform([email_text])
    prediction = svm_classifier.predict(email_vectorized)

    if prediction[0] == 1:
        return jsonify({"result": "Email is spam!"})
    return jsonify({"result": "Email is NOT spam."})


@app.route("/shutdown")
def shutdown():
    """
    shutdown
    """
    os.kill(os.getpid(), signal.SIGINT)


if __name__ == "__main__":
    app.run(debug=True)
