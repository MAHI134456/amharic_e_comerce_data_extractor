# Amharic E-commerce Data Extractor


## Project Overview

The Amharic E-commerce Data Extractor is a Python-based project designed to extract, process, and analyze e-commerce data, with a focus on supporting Amharic language content. This tool aims to provide insights into e-commerce trends, customer behavior, and product performance in Amharic-speaking markets.

The project is currently in the setup phase, with the development environment configured and initial dependencies installed.


## Current Progress





- Python Environment Setup: A virtual Python environment has been created to ensure dependency isolation and reproducibility.

- Version Control Configuration: A .gitignore file has been added to exclude unnecessary files (e.g., virtual environment files, cache, and temporary files) from version control.

- Continuous Integration: A GitHub Actions workflow (.github/workflows/CI.yml) has been set up to automate testing and ensure code quality on every push or pull request.

- Dependencies Installed:

    - pandas: For data manipulation and analysis.
    - matplotlib: For creating visualizations and plots.
    - seaborn: For enhanced data visualization with a focus on statistical graphics.


## Project Structure

```bash
   Amharic-Ecommerce-Data-Extractor/
├── .github/
│   └── workflows/
│       └── CI.yml
├── .gitignore
├── README.md
└── env/

```

## Setup Instructions
To set up the project locally, follow these steps:
 1. Clone the Repository:```bash git clone https://github.com/MAHI134456/Amharic-Ecommerce-Data-Extractor.git cd Amharic-Ecommerce-Data-Extractor```

 2. Create a Virtual Environment:```bash python -m venv venv```

 3. Activate the Virtual Environment: 
    - On Windows:```bash env\Scripts\activate```
    - On macOS/Linux:```bash source venv/bin/activate```

 4. Install Dependencies:```bash pip install pandas matplotlib seaborn```

 5. Verify Installation: Run the following command in Python to confirm the libraries are installed:
     ```bash import pandas import matplotlib import seaborn print("Dependencies installed successfully!")```
