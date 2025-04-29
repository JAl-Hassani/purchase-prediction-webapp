
# 🛍️ Purchase Prediction Web App

A machine learning-powered web application that predicts whether a customer will make a purchase based on their input data. Built with Python and scikit-learn, this app demonstrates a complete ML pipeline from training to deployment.

---

## 🚀 Features

- **Binary Classification**: Predicts purchase likelihood (Yes/No).
- **Pre-trained Model**: Utilizes a Random Forest classifier saved as `pipeline_rf.joblib`.
- **Simple Interface**: Accepts user input via command-line prompts.
- **Lightweight Deployment**: Runs as a standalone Python script—no web server required.

---

## 🧠 How It Works

The application loads a pre-trained machine learning pipeline and prompts the user to input relevant features. It then processes the input through the pipeline to predict the probability of a purchase.

---

## 📁 Project Structure

```
purchase-prediction-webapp/
├── pipeline_rf.joblib           # Trained ML pipeline
├── purchase-prediction.py       # Main application script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JAl-Hassani/purchase-prediction-webapp.git
   cd purchase-prediction-webapp
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python purchase-prediction.py
   ```

   Follow the on-screen prompts to input customer data and receive a purchase prediction.

---

## 📦 Dependencies

- `scikit-learn`
- `joblib`
- `pandas`
- `numpy`

*(See `requirements.txt` for the full list.)*

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

- **JAl-Hassani** – [GitHub Profile](https://github.com/JAl-Hassani)
