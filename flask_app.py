import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the saved model
with open('best_model.pkl', 'rb') as f:
    svm_classifier = pickle.load(f)

with open('vectorizer_model.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def index():
    """
    index
    """
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    """
    classify
    """
    email_text = request.form['email_text']

    if not email_text.strip():
        return jsonify({'result': 'Please enter your email text.'})

    email_vectorized = vectorizer.transform([email_text])
    prediction = svm_classifier.predict(email_vectorized)

    if prediction[0] == 1:
        return jsonify({'result': 'The email is spam!'})
    else:
        return jsonify({'result': 'Email is not spam.'})

if __name__ == '__main__':
    app.run(debug=True)
    