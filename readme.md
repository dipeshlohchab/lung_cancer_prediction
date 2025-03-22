# Lung Cancer Prediction

This is a web application for lung cancer prediction based on various health parameters. It is built using Flask for the backend, HTML/CSS/JavaScript for the frontend, and a machine learning model for prediction.

## Features
- Collects user inputs related to lung cancer risk factors
- Sends input data to a Flask API for prediction
- Returns a prediction (Yes/No) based on the trained ML model
- Supports dark mode

---

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask
- **Machine Learning Model:** Scikit-learn (saved as a `.pkl` file)
- **Deployment:** Render

---

## Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/lung-cancer-prediction.git
cd lung-cancer-prediction
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App Locally**
```sh
python app.py
```
Your app will be available at `http://127.0.0.1:5000`.

---

## API Endpoint
### **POST /predict**
- **URL:** `http://127.0.0.1:5000/predict`
- **Request Body (JSON):**
  ```json
  {
    "AGE": 50,
    "GENDER": "male",
    "SMOKING": "yes",
    "FINGER_DISCOLORATION": "no",
    "LEVEL": "yes",
    "EXPOSURE_POL": "yes",
    "LONG_TERM_ILLNESS": "no",
    "ENERGY": 80,
    "IMMUNE_WEAKNESS": "no",
    "BREATHING_ISSUE": "yes",
    "ALCOHOL_CONSUMPTION": "no",
    "THROAT_DISCOMFORT": "yes",
    "OXYGEN_SATURATION": 95,
    "CHEST_TIGHTNESS": "no",
    "FAMILY_HISTORY": "yes",
    "SMOKING_FAMILY_HISTORY": "yes",
    "STRESS_IMMUNE": "no"
  }
  ```
- **Response:**
  ```json
  {
    "prediction": "yes"
  }
  ```

---

## Deployment on Render

1. **Create a `requirements.txt` file**
   ```sh
   pip freeze > requirements.txt
   ```

2. **Create a `start.sh` file**
   ```sh
   #!/bin/bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Push to GitHub**
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

4. **Deploy on Render:**
   - Go to [Render](https://render.com/)
   - Click **New Web Service**
   - Select **GitHub Repository**
   - **Set Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `bash start.sh`
   - Click **Deploy**

---

## Issues & Contributing
If you find any issues, please raise them in the GitHub repository. Contributions are welcome!

---

## License
This project is open-source and available under the MIT License.

