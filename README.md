
# 📧 DSBSA Mini Project: Spam SMS Detection using Machine Learning

## 📌 Project Title
Spam SMS Detection using Machine Learning and Natural Language Processing (NLP)

---

## 🎯 Objective
The objective of this project is to build a machine learning model that can automatically classify SMS messages into:

- 🚫 Spam (Unwanted / Fraud messages)
- ✅ Ham (Normal / Safe messages)

This helps in filtering unwanted messages and improving communication safety.

---

## 🧠 Problem Statement
With the increasing number of SMS-based scams and spam messages, it becomes difficult for users to manually identify harmful messages. This project uses Machine Learning to automatically detect spam messages.

---

## 📊 Dataset Used
The dataset is taken from Kaggle:

👉 SMS Spam Collection Dataset  
Source: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

### Dataset Details:
- Total messages: ~5500
- Columns:
  - `v1` → Label (spam/ham)
  - `v2` → Message text

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Kaggle API

---

## 🤖 Machine Learning Model Used

- Algorithm: **Multinomial Naive Bayes**
- Type: Supervised Learning
- Domain: Natural Language Processing (NLP)

---

## ⚙️ Project Workflow

### 1. Data Collection
- Dataset downloaded from Kaggle using Kaggle API

### 2. Data Preprocessing
- Converted text to lowercase
- Removed punctuation and numbers
- Cleaned raw SMS messages

### 3. Exploratory Data Analysis (EDA)
- Spam vs Ham distribution visualization
- Message length analysis
- Confusion matrix visualization

### 4. Feature Extraction
- Converted text into numerical form using **CountVectorizer**

### 5. Model Training
- Trained using Multinomial Naive Bayes classifier

### 6. Model Evaluation
- Accuracy calculation
- Classification report
- Confusion matrix

### 7. Real-time Prediction
- Input message from user
- Predict whether message is spam or not

---

## 📈 Visualizations

The project includes:

- 📊 Spam vs Ham distribution graph
- 📉 Message length distribution histogram
- 🔥 Confusion matrix heatmap

---

## 📌 Project Features

✔ Automatic dataset download from Kaggle  
✔ Text preprocessing using NLP  
✔ Machine Learning classification model  
✔ Real-time message prediction  
✔ Data visualization for insights  
✔ Interactive input system  

---

## 🚀 How to Run the Project

### Step 1: Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn kaggle
````

---

### Step 2: Setup Kaggle API

1. Go to Kaggle → Account → Create API Token
2. Download `kaggle.json`
3. Place it in:

```
~/.kaggle/kaggle.json
```

---

### Step 3: Run Python file or Jupyter Notebook

```bash
python spam_detector.py
```

OR run in JupyterLab.

---

## 🧪 Example Predictions

### Input:

```
Congratulations! You won a free iPhone. Click now!
```

### Output:

```
Spam
```

---

### Input:

```
Hey, are we meeting today at 5 PM?
```

### Output:

```
Ham
```

---

## 📊 Results

* Model Accuracy: ~95% (varies slightly)
* Good performance on text classification
* Fast real-time predictions

---

## 🧠 Learning Outcomes

* Understanding NLP preprocessing
* Working with real-world datasets
* Building classification models
* Evaluating ML models using metrics
* Data visualization techniques

---

## ⚠️ Limitations

* Model may misclassify complex spam messages
* Requires clean dataset for best performance
* Not deployed in production environment

---

## 🔮 Future Improvements

* Use TF-IDF instead of CountVectorizer
* Use Deep Learning (LSTM / BERT)
* Deploy using Flask or Streamlit
* Add real-time SMS API integration

---

## 👨‍💻 Author

DSBSA Mini Project
Student Project – Machine Learning & Data Science

---

## 📜 License

This project is for educational purposes only.
