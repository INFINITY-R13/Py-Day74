# 🧱 LEGO Dataset Analysis Project
**Day 74 - Python Data Science Course**

*Aggregate & Merge Data with Pandas: Comprehensive Analysis of the LEGO Dataset*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 Overview

This project provides a comprehensive analysis of LEGO datasets spanning over 70 years (1949-2021). Using Python's powerful data analysis libraries, we explore the evolution of LEGO products, themes, colors, and complexity trends.

## 🎯 Key Questions Answered

- 🎨 **How many different colors does LEGO produce?**
- 🏗️ **What were the first LEGO sets ever released?**
- 📏 **Which LEGO set has the most parts?**
- 📈 **How has LEGO's product offering evolved over time?**
- 🎭 **Which themes are most popular?**
- 🔍 **Have LEGO sets become more complex over the years?**

## 📊 Key Findings

- **135 unique LEGO colors** (107 opaque, 28 transparent)
- **First sets released in 1949** (5 different gift sets)
- **Largest set**: "The Ultimate Battle for Chima" with **9,987 parts**
- **Exponential growth**: From 28 sets in 1955 to 840 sets in 2019
- **15,710 total sets** across 596 different themes

## 🗂️ Dataset Structure

| Dataset | Description | Records |
|---------|-------------|---------|
| `colors.csv` | LEGO color information with RGB values and transparency | 135 rows |
| `sets.csv` | Complete LEGO sets data with parts count and themes | 15,710 rows |
| `themes.csv` | LEGO themes hierarchy and relationships | 596 rows |

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas matplotlib jupyter
```

### Run Analysis

#### Option 1: Quick Summary (Recommended for beginners)
```bash
python run_analysis.py
```

#### Option 2: Full Interactive Analysis (Recommended)
```bash
python -m jupyter notebook
# Open Lego_Analysis_for_Course.ipynb
# Click "Cell" → "Run All"
```

#### Option 3: JupyterLab
```bash
python -m jupyter lab
```

#### Option 4: Python Script
```bash
python Lego_Analysis_for_Course.py
```

## 📁 Project Structure

```
Py-Day74/
├── 📊 data/
│   ├── colors.csv              # LEGO colors dataset
│   ├── sets.csv                # LEGO sets dataset
│   └── themes.csv              # LEGO themes dataset
├── 📓 Lego_Analysis_for_Course.ipynb  # Main analysis notebook
├── 🐍 run_analysis.py          # Quick analysis script
├── 🐍 Lego_Analysis_for_Course.py     # Converted Python script
├── 📋 HOW_TO_RUN.md           # Detailed running instructions
├── 🛡️ .gitignore              # Git ignore rules
└── 📖 README.md               # This file
```

## 🔧 Technical Skills Demonstrated

### Data Analysis
- **Data Loading & Exploration**: Reading CSV files, examining data structure
- **Data Cleaning**: Handling missing values and data types
- **Aggregation**: Using `groupby()`, `count()`, `nunique()` methods
- **Filtering**: Conditional filtering and sorting operations
- **Merging**: Combining datasets using pandas merge operations

### Visualization
- **Matplotlib**: Creating line charts, bar plots, and histograms
- **Data Storytelling**: Visualizing trends and patterns over time
- **Statistical Analysis**: Exploring distributions and correlations

### Python Libraries Used
- `pandas` - Data manipulation and analysis
- `matplotlib` - Data visualization
- `jupyter` - Interactive development environment

## 📈 Analysis Highlights

### Historical Evolution
- **1949**: LEGO's humble beginning with 5 gift sets
- **1955**: 28 sets released
- **2019**: Peak year with 840 sets released
- **Growth Rate**: 30x increase from 1955 to 2019

### Product Complexity
- **Smallest sets**: 0 parts (promotional items)
- **Largest set**: 9,987 parts (The Ultimate Battle for Chima)
- **Average complexity**: Increasing trend over decades
- **Theme diversity**: 596 different themes

### Color Palette
- **Total colors**: 135 unique colors
- **Transparency**: 79% opaque, 21% transparent
- **RGB data**: Complete color specifications available

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- **Pandas DataFrame operations**
- **Data aggregation and grouping**
- **Time series analysis**
- **Data visualization techniques**
- **Exploratory data analysis (EDA)**
- **Statistical summarization**
- **Jupyter Notebook development**

## 📚 Data Source

Dataset compiled from [Rebrickable](https://rebrickable.com/downloads/), which maintains comprehensive data on all LEGO pieces in existence.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Rebrickable** for providing comprehensive LEGO datasets
- **Python Data Science Community** for excellent libraries
- **LEGO Group** for 70+ years of creative building experiences

---

*Built with ❤️ for data science learning and LEGO enthusiasts*

**Happy Building! 🧱📊**