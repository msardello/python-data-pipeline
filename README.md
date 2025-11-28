# 🧠 AI SE Assistant — Python Data Pipeline Project

A small, modular, and testable Sales Engineering Data Pipeline that loads opportunities from CSV, 
validates fields, performs analytics (win rate, proposal opportunities, pipeline by owner, top deals), and 
writes results to JSON.

## 🔬 This project demonstrates:

- Clean Python project structure
- Config-driven pipelines
- Data validation
- Modular functions
- Logging 
- Automated testing with pytest 
- Command-line execution
- Realistic SE-style data analysis

## 🚀 Features

- Config-driven execution using YAML 
- Safe CSV loading with validation 
- Analytics functions:
  - Proposal opportunities 
  - Win rate calculation 
  - Pipeline by owner 
  - Top N deals 
- JSON output writer 
- CLI support: choose input CSV, N for top deals, validate-only mode 
- pytest test suite 
- Clean, professional folder structure

## 📂 Project Structure
```plaintext
ai-se-assistant/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── opportunities.csv
│   ├── opportunities_sorted.csv
│   └── opportunities_proposals.csv
│
├── outputs/
│   ├── pipeline_results.json
│   └── pipeline.log
│
├── scripts/
│   ├── config.py
│   ├── data_pipeline.py
│   ├── opportunity_functions.py
│   ├── opportunity_summary.py
│   ├── opportunity_transform.py
│   ├── test_environment.py
│   └── utils.py
│
├── tests/
│   └── test_utils.py
│
├── venv/              ← ignored by git
├── .env               ← ignored by git
├── .gitignore
└── README.md
```

## ⚙️ Installation

1. Clone or download the repository
```
git clone https://github.com/YOUR_USERNAME/ai-se-assistant.git
cd ai-se-assistant
```

2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate     # on macOS
```
3. Install dependencies
```
pip install -r requirements.txt
```

## ▶️ Running the Pipeline

Basic run
```
python scripts/data_pipeline.py
```

Using a different input file
```
python scripts/data_pipeline.py --input data/opportunities.csv
```

Override top N deals
```
python scripts/data_pipeline.py --top 5
```
Validation-only mode
```
python scripts/data_pipeline.py --validate-only
```

## 📄 Configuration (config/config.yaml)
```yaml
input_csv: "data/opportunities.csv"
top_n: 3
output_dir: "outputs"
log_file: "pipeline.log"
required_columns:
  - Name
  - Owner
  - Stage
  - Amount
```
## 🧪 Running Tests
```
pytest
```

## 📊 Example Output (pipeline_results.json)
```json
{
  "proposal_opportunities": [
      { "Name": "ABC Deal", "Owner": "Marc", "Stage": "Proposal", "Amount": 50000 }
  ],
  "win_rate": 0.25,
  "pipeline_by_owner": {
    "Marc": 125000,
    "Sarah": 90000
  },
  "top_3_deals": [
    { "Name": "BigCo Expansion", "Amount": 120000 },
    { "Name": "TechCorp Renewal", "Amount": 90000 },
    { "Name": "Startup Pilot", "Amount": 75000 }
  ],
  "input_file": "data/opportunities.csv",
  "top_n": 3
}
```

## 🛣️ Roadmap (Next Steps)

- Add chart generation via matplotlib 
- Add API endpoint (FastAPI)
- Add database support (SQLite or PostgreSQL)
- Add more automated tests 
- Add real-world Salesforce sample exports 
- Build a Streamlit UI 
- Add CI/CD (GitHub Actions)

## 👤 Author

**Marc Sardello**  
Principal Solutions Engineer / Technical Pre-Sales Professional  

With a career spanning finance systems, enterprise planning, BI, big data, data preparation, analytics, and Quote-to-Cash architecture, I bring deep experience in understanding complex systems and translating them into practical, scalable technical solutions.  

Past roles include work across IBM (TM1 & Cognos), Microsoft (Advanced Analytics & Revolution R), Qlik, Datawatch, Unifi Software, Trifacta, and Salesforce Revenue Cloud.  

This project is part of my ongoing focus on sharpening Python, data engineering, and AI-enabled solution design skills to support the growth and evolution of my career. 
