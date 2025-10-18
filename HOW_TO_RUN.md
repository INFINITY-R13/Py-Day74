# 🧱 LEGO Analysis Project - How to Run

This project analyzes LEGO datasets to explore the history and evolution of LEGO products from 1949 to 2021.

## 📋 Prerequisites

Make sure you have Python installed with the required packages:
```bash
pip install pandas matplotlib jupyter
```

## 🚀 Running the Project

### Method 1: Quick Analysis (Recommended for beginners)
```bash
python run_analysis.py
```
This runs a summary analysis and shows key insights.

### Method 2: Full Interactive Jupyter Notebook (Recommended)
```bash
python -m jupyter notebook
```
1. Your browser will open automatically
2. Click on `Lego_Analysis_for_Course.ipynb`
3. Click "Cell" → "Run All" to execute all analysis

### Method 3: JupyterLab (Modern interface)
```bash
python -m jupyter lab
```

### Method 4: Python Script
```bash
python Lego_Analysis_for_Course.py
```

## 📊 What You'll Discover

- **LEGO Colors**: 135 unique colors (107 opaque, 28 transparent)
- **Historical Growth**: From 5 sets in 1949 to 840 sets in 2019
- **Largest Set**: "The Ultimate Battle for Chima" with 9,987 parts
- **Themes Analysis**: Which themes have the most sets
- **Complexity Evolution**: How LEGO sets have grown over time

## 📁 Project Structure

```
Py-Day74/
├── data/
│   ├── colors.csv      # LEGO colors data
│   ├── sets.csv        # LEGO sets data
│   └── themes.csv      # LEGO themes data
├── Lego_Analysis_for_Course.ipynb  # Main analysis notebook
├── run_analysis.py     # Quick analysis script
└── HOW_TO_RUN.md      # This file
```

## 🔧 Troubleshooting

If you get import errors:
```bash
pip install pandas matplotlib jupyter
```

If Jupyter doesn't start:
```bash
python -m jupyter notebook
```

## 📈 Key Analysis Questions Answered

1. How many different colors does LEGO produce?
2. What were the first LEGO sets ever released?
3. Which LEGO set has the most parts?
4. How has LEGO's product offering grown over time?
5. Which themes are most popular?

Enjoy exploring 70+ years of LEGO history! 🎉