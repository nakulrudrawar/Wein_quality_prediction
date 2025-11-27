# 🍷 Wine Quality Prediction

A machine learning web application that predicts whether a wine is of good or bad quality based on its chemical properties.

## 📋 Overview

This project uses a **Random Forest Classifier** to classify red wine quality as either "Good" (quality >= 7) or "Bad" (quality < 7). The application features a user-friendly web interface built with Streamlit.

## 🎯 Features

- Interactive web interface for wine quality prediction
- Real-time predictions based on 11 chemical parameters
- Beautiful and intuitive UI with wine-themed styling
- Model trained on red wine quality dataset

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Scikit-learn** - Machine learning library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Data visualization
- **Streamlit** - Web application framework

## 📊 Dataset

The project uses the **Wine Quality Dataset** (winequality-red.csv) containing:
- 1,599 red wine samples
- 11 input features (chemical properties)
- 1 target variable (quality rating)

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To launch the web app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📝 How to Use

1. Enter the wine parameters (11 chemical properties) in the sidebar
2. Click the **"Predict Wine Quality"** button
3. View the prediction result:
   - ✅ **Good Quality Wine** - Enjoyable and well-balanced
   - ❌ **Low Quality Wine** - Needs improvement

## 📁 Project Structure

```
Wein_quality_prediction/
├── app.py                      # Streamlit web application
├── final_project.ipynb         # Jupyter notebook with ML model development
├── winequality-red.csv         # Dataset
├── wine_model.pkl              # Trained model (binary)
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## 🔍 Model Details

- **Algorithm**: Random Forest Classifier
- **Training/Test Split**: 80/20
- **Features**: 11 chemical properties of wine
- **Target Classes**: Good (1) / Bad (0)

## 👨‍💻 Developer

**G6** - MCA Student, Pune  
G H Raisoni College of Engineering and Management

## 📄 License

This project is open source and available for educational purposes.
