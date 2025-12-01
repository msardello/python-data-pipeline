# 🧠 Unified Python Data Pipeline + FastAPI API

A clean, modular, professional-grade data pipeline that loads and validates opportunity
data, computes basic analytics (win rate, pipeline by owner, top deals), and exposes both:  
- a CLI tool, and
- A FastAPI backend

Both powered by one shared engine: pipeline_core.py

This is an ongoing project for me, which is built to demonstrate Python engineering patterns used in analytics 
and automation.


---

## 🚀 Features

### 🔄 Unified Pipeline Engine (pipeline_core.py)
Both the CLI and API use a single, shared execution path:
- Consistent filtering
- Consistent validation
- Consistent summary output
- Consistent defaults

### 🧪 Validated CSV Loading
- Safe CSV loader
- Required column validation
- Config-driven (YAML)

### 📊 Analytics Functions
- Win rate
- Pipeline by owner
- Top N deals
- Total opps & total pipeline summary

### 🧰 Command Line Interface
``` zsh
python -m scripts.data_pipeline --top 3
python -m scripts.data_pipeline --validate-only
python -m scripts.data_pipeline --min-amount 50000 --stage Proposal
```

### 🌐 FastAPI Backend
Endpoints:
- GET /health
- GET /pipeline
- POST /pipeline/custom

### 🛠 Clean Folder Structure
Modern Python project layout with separation of concerns.

### 🗃 Examples Archive
Older scripts preserved for reference inside examples/.

---

## 📂 Project Structure
```plaintext
python-data-pipline/
│
├── api/
│   └── main.py                 # FastAPI app
│
├── config/
│   └── config.yaml             # User-editable settings
│
├── data/
│   └── opportunities.csv       # Sample dataset
│
├── outputs/
│   ├── pipeline_results.json   # CLI output
│   └── pipeline.log            # Log file
│
├── scripts/
│   ├── pipeline_core.py        # Shared engine for API + CLI
│   ├── pipeline_api.py         # API wrapper
│   ├── data_pipeline.py        # CLI wrapper
│   ├── config.py               # Loads YAML + env vars
│   ├── utils.py                # Validation + safe CSV load
│   └── opportunity_functions.py# Core analytics
│
├── examples/
│   ├── opportunity_summary.py
│   ├── opportunity_transform.py
│   ├── validated_summary.py
│   └── test_environment.py
│
├── tests/
│   └── test_utils.py           # pytest examples
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. Clone the repo
``` zsh
git clone https://github.com/msardello/python-data-pipeline.git
cd python-data-pipeline
```

2. Create a virtual environment
``` zsh
python3 -m venv venv
source venv/bin/activate     # on macOS
```

3. Install dependencies
``` zsh
pip install -r requirements.txt
```

---

## 🖥️ Command Line Usage (CLI)

Important: Always use python -m to ensure correct imports.

### Validate only
``` zsh
python -m scripts.data_pipeline --validate-only
```

### Top 3 Deals
``` zsh
python -m scripts.data_pipeline --validate-only
```

### Filter by stage and amount
``` zsh
python -m scripts.data_pipeline --min-amount 50000 --stage Proposal
```

### Output
Results are saved to:
``` zsh
outputs/pipeline_results.json
```

---

## 🌐 FastAPI API Usage

### Start the Server
``` zsh
uvicorn api.main:app --reload
```

### Test in Browser
- [Health check](http://127.0.0.1/:8000/health)
- [Default pipeline](http://127.0.0.1:8000/pipeline)
- [API docs (Swagger)](http://127.0.0.1:8000/docs)

---

## 🔧 API Examples
### POST /pipeline/custom
Example Body:
``` json
{
  "csv_path": "data/opportunities.csv",
  "top_n": 3,
  "min_amount": 50000,
  "stage": "Proposal"
}
```

---

## 📄 Configuration (config/config.yaml)
``` yaml
default_csv: "data/opportunities.csv"
default_top_n: 3

paths:
  output_dir: "outputs"

validation:
  required_columns:
    - Name
    - Owner
    - Stage
    - Amount
```

---

## 🧪 Tests (pytest)
``` zsh
pytest
```
test_utils.py demonstrates safe CSV loading and validation checks.

---

## 📜 Roadmap
- Add charts via matplotlib
- Add SQLite/Postgres output option
- CI/CD with GitHub Actions
- Docker packaging
- Expand pytest coverage
- Sales Cloud / CRM export ingestion

---

## 👤 Author

Created by Marc Sardello  
Learning, experimentation, and exploration in Python, data engineering, and automation with a focus on clean 
structure and testability.

---
