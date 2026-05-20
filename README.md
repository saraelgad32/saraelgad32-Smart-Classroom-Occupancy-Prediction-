# Python Project

## Description
This project is a Python-based application for data processing and prediction.

## Project Structure
```
PYTHON_PROJECT/
├── data/               # Training and prediction data files
├── src/                # Source code modules
├── templates/          # HTML templates (if web-based)
├── app.py              # Main application entry point
├── train_script.py     # Model training script
└── .gitignore          # Git ignore rules
```

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/saraelgad32/YOUR_REPO_NAME.git
cd PYTHON_PROJECT
```

### 2. Create a virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run the main application
```bash
python app.py
```

### Train the model
```bash
python train_script.py
```

## Data Files
- `data/datatraining.txt` - Training dataset
- `data/prediction_audit.csv` - Prediction audit data

## Requirements
- Python 3.7+

## Notes
- Virtual environment (`.venv/`) and cache (`__pycache__/`) are excluded from Git
- Model files in `models/` are not tracked

## Authors
Oualid Dersaoui  
Aya Baali  
Assia Bouhali
Sara Elgad

## License
This project is for educational/personal use.
