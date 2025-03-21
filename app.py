from flask import Flask,render_template, request, jsonify
import pickle

app = Flask(__name__)

with open("artifacts/model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True)
    