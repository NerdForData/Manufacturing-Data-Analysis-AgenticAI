# Manufacturing-Data-Analysis-AgenticAI
This code resolves the data silos issue and builds an agentic AI which handles the data ingestion and integration, schema, data anomaly detection, data visualization and report generation.  

# Agentic AI Prototype for Manufacturing Data Integration

This repository demonstrates how AI agents can unify manufacturing data silos from **ERP production data** and **CMM measurement data**. The solution reflects an ML engineering approach with modular design, schema reasoning, integration, analysis, and anomaly detection.

---

## Contents

- `prototype.ipynb`: Jupyter notebook showing the full pipeline with code and plots.  
- `schema_agent.py`: Embedding-based schema reasoning for column matching.  
- `integration_agent.py`: Data unification logic across ERP and CMM datasets.  
- `analysis_agent.py`: Pass/fail summary, defect traceability, and anomaly detection.  
- `data_ingest.py`: CSV loading and cleaning functions.  
- `utils.py`: Helper utilities for column normalization.  
- `streamlit_app.py`: Interactive dashboard for uploading CSVs and visualizing analysis.  
- `unified_dataset_sample.csv`: Example unified dataset linking ERP lots with CMM measurements.  
- `analysis_report.md`: Markdown report with summary statistics, defect traceability, and anomaly counts.  
- `requirements.txt`: Project dependencies.

---

## Datasets

The prototype uses two simulated CSV files:

1. **`production_data.csv`**  
   ERP/MES-style dataset capturing production lots, machines, operators, and timestamps.

2. **`cmm_data.csv`**  
   CMM dataset with part-level measurements, tolerance limits, and pass/fail status.

---

## Objectives Achieved

- Performed **schema reasoning** using embeddings (local SentenceTransformers model).  
- Built an automated pipeline for **data integration**, linking ERP lots with CMM results.  
- Generated an **analysis report** with:  
  - Overall pass/fail rates,  
  - Defect traceability to production lots,  
  - Anomaly detection using IsolationForest.  
- Delivered a **Streamlit dashboard** for interactive visualization.  
- Organized code into **modular agent classes** for clarity and reusability.  

---

## Pipeline Steps

### 1. Schema Matching
- Implemented in `schema_agent.py`.  
- Uses **sentence-transformer embeddings** to propose matches between ERP and CMM columns (e.g., `part_id` ↔ `component_id`).  

### 2. Data Cleaning
- Implemented in `data_ingest.py`.  
- Standardizes column names, trims whitespace, and handles missing values.

### 3. Data Integration
- Implemented in `integration_agent.py`.  
- Joins ERP and CMM data on normalized keys.  
- Produces a **unified dataset** with production metadata attached to each CMM record.

### 4. Analysis
- Implemented in `analysis_agent.py`.  
- Produces:  
  - **Pass/fail summary** (% passed, % failed),  
  - **Defects by lot** (traceability),  
  - **Anomaly detection** using IsolationForest.

### 5. Report Generation
- Sample outputs saved in `analysis_report.md`.  
- A helper script (`generate_report.py`) can regenerate the report from the unified dataset.

### 6. Streamlit Dashboard
- `streamlit_app.py` allows file upload and shows:  
  - Unified dataset preview,  
  - Fail rate by feature,  
  - Overall pass/fail pie chart.  

---

## Design Choice

- **Embeddings for schema reasoning**: Chosen to flexibly map semantically similar column names between ERP and CMM datasets without manual renaming. A local transformer model was used to avoid API costs.  
- **IsolationForest for anomaly detection**: Selected because it works well for high-dimensional numeric data, is unsupervised, and robust against outliers.  
- **Agent-based modularity**: Each step (schema, integration, analysis) is encapsulated in its own agent, making the pipeline easier to maintain, extend, and test.  
- **Streamlit (optional)**: Added to demonstrate how results could be visualized interactively. 
---

## How to Run

I ran the commands in virtual environment (recommended) to avoid conflicts. 

###  Install Requirements
```bash
pip install -r requirements.txt
```

###  Run Notebook
```bash
jupyter notebook prototype.ipynb
```

###  Run Report Generation
```bash
python generate_report.py
```

This produces `analysis_report.md` in the project folder.

### Launch Dashboard (Streamlit)
```bash
streamlit run streamlit_app.py
```

- **`unified_dataset_sample.csv`** → Example merged dataset.  
- **`analysis_report.md`** → Pass/fail summary, defect traceability, anomaly counts.  
- **Notebook visualizations** → Inline plots for fail rates and anomalies - it has little bit detailed visualizations.  
- **Optional dashboard** → Interactive Streamlit UI.
