Crop Recommendation System

Overview
This project is a Machine Learning-based Crop Recommendation System that helps farmers and agricultural researchers identify the most suitable crop to grow based on soil and environmental conditions. The system takes parameters like Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall as input and suggests the best crop accordingly.

Tech Stack
- Python (Data Processing, ML Model)
- Scikit-learn (Machine Learning)
- Pandas, NumPy (Data handling)
- Matplotlib, Seaborn (Visualization)
- Streamlit (Web App interface)
- Joblib (Model saving/loading)

Features
✔️ Recommends crops based on soil and weather data
✔️ Simple and user-friendly interface using Streamlit
✔️ Pre-trained machine learning model for instant predictions
✔️ Easy to run on any system with required dependencies


Project Structure
crop_project/
│── crop_env/              # Virtual environment
│── app.py                 # Streamlit web app
│── train_model.py         # ML model training script
│── crop_recommendation.pkl# Saved ML model
│── README.md              # Project documentation
│── requirements.txt       # Required Python packages


Installation & Setup
1️⃣ Clone the repository
git clone <repo_link>
cd crop_project
2️⃣ Create a virtual environment
python -m venv crop_env
3️⃣ Activate the environment
- For PowerShell (Windows):
 .\crop_env\Scripts\activate
- For Mac/Linux:
 source crop_env/bin/activate
4️⃣ Install dependencies
pip install -r requirements.txt
5️⃣ Run the app
streamlit run app.py

Example Input
- Nitrogen: 90
- Phosphorus: 42
- Potassium: 43
- Temperature: 20°C
- Humidity: 82%
- pH: 6.5
- Rainfall: 200 mm

👉 Output: Recommended Crop → Rice 🌾

Contribution
Contributions are welcome! Feel free to fork this repo, open issues, and submit PRs.

