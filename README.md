# Credit Approval ML System (End-to-End MLOps)

![CI](https://github.com/Ingle-Santosh/credit-approval-mlops/actions/workflows/ci.yml/badge.svg)
![DVC](https://img.shields.io/badge/DVC-Data%20Versioned-blue)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-orange)
![GitHub Repo Size](https://img.shields.io/github/repo-size/Ingle-Santosh/credit-approval-mlops)
![License](https://img.shields.io/github/license/Ingle-Santosh/credit-approval-mlops)

An **industry-grade, end-to-end machine learning system** for predicting **credit approval priority (P1–P4)** using banking and bureau data.  
This project demonstrates **production-ready ML engineering and MLOps practices** including reproducible pipelines, experiment tracking, CI/CD, and model deployment.

---

## 📌 Business Problem

Financial institutions need to **evaluate loan applicants efficiently while managing credit risk**.

Given:
- Internal banking attributes (trade lines, loan history)
- External bureau data (delinquencies, enquiries, credit score)
- Demographic and financial information

We aim to **predict the applicant’s approval priority**:
- **P1** – Highest approval priority  
- **P4** – Lowest approval priority / high risk  

This is framed as a **multi-class classification problem**.

---

## 🎯 Objectives

- Build a **reproducible ML pipeline** from raw data to deployment
- Apply **industry-standard feature engineering & validation**
- Track experiments and models using **MLflow**
- Version data and pipelines using **DVC**
- Expose predictions via **FastAPI** and **Streamlit**
- Enable **CI/CD automation** with GitHub Actions

---

## 🧠 ML & MLOps Stack

| Category | Tools |
|--------|------|
| Language | Python |
| ML | Scikit-learn |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Pipeline Orchestration | DVC Pipelines |
| API | FastAPI |
| UI | Streamlit |
| CI/CD | GitHub Actions |
| Version Control | Git |
| Packaging | setup.py |
| Testing | Pytest, Tox |

---

## 📁 Project Structure

```

credit-approval-mlops/
│
├── .github/
│   └── workflows/
│       ├── ci.yml                    # CI pipeline (tests, linting)
│       └── model_training.yml        # Automated retraining workflow
│
├── data/
│   ├── raw/                          # Raw input data (DVC tracked)
│   ├── interim/                      # Intermediate datasets
│   ├── processed/                    # Final model-ready data
│   └── .gitignore                    # Prevent data from being committed
│
├── notebooks/
│   ├── 01_eda.ipynb                  # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb  # Feature experiments
│   └── 03_model_experiments.ipynb    # Model selection & baselines
│
├── src/
│   ├── components/                  # Core ML pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py     # End-to-end training orchestration
│   │   └── prediction_pipeline.py   # Inference pipeline
│   │
│   ├── entity/                      # Config & artifact schemas
│   ├── utils/                       # Logging, common utilities
│   └── exception.py                 # Custom exception handling
│
├── api/                             # FastAPI inference service
├── app/                             # Streamlit UI for predictions
│
├── models/                          # Saved production models
├── artifacts/                       # MLflow artifacts & runs
├── reports/                         # Evaluation reports & figures
├── tests/                           # Unit & integration tests
├── logs/                            # Centralized logging
│
├── dvc.yaml                         # DVC pipeline definition
├── params.yaml                      # Model & pipeline parameters
├── requirements.txt                 # Dependencies
├── setup.py                         # Package configuration
├── Makefile                         # Command shortcuts
├── LICENSE
└── README.md

````

---

## 🔄 End-to-End Workflow

1. **Data Ingestion**
   - Load internal & external datasets
   - Merge using `PROSPECTID`
   - Store raw data using DVC

2. **Data Validation**
   - Schema checks
   - Missing values & type validation
   - Data drift readiness

3. **Data Transformation**
   - Encoding categorical features
   - Scaling numerical features
   - Feature engineering

4. **Model Training**
   - Multi-class classification (P1–P4)
   - Cross-validation
   - Hyperparameter tuning
   - Experiment tracking with MLflow

5. **Model Evaluation**
   - Accuracy, F1-score
   - Confusion matrix
   - Model comparison via MLflow

6. **Model Deployment**
   - REST API using FastAPI
   - Interactive UI using Streamlit

7. **CI/CD**
   - Automated testing
   - Pipeline validation on push/PR

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Ingle-Santosh/credit-approval-mlops.git
cd credit-approval-mlops
````

### 2️⃣ Create Environment & Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run DVC Pipeline

```bash
dvc repro
```

### 4️⃣ Start FastAPI

```bash
uvicorn api.main:app --reload
```

### 5️⃣ Start Streamlit App

```bash
streamlit run app/app.py
```

---

## 📊 MLflow Tracking

```bash
mlflow ui
```

Track:

* Experiments
* Metrics
* Model versions
* Artifacts

---

## 🧪 Testing

```bash
pytest
tox
```

---

## 🧩 Key Highlights

* Fully reproducible ML pipeline
* Clear separation of concerns (data, features, models, pipelines)
* Production-style error handling & logging
* CI-enabled quality checks
* Realistic banking domain problem
* End-to-end deployment included