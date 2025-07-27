# 🔋 World Energy Consumption Dashboard
-------------------

An interactive data analysis dashboard that visualizes global energy consumption patterns using real-world data from Kaggle's World Energy Consumption dataset.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![Pandas](https://img.shields.io/badge/pandas-v2.0+-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Features

- **Comprehensive Energy Analysis**: Track consumption across coal, gas, oil, nuclear, and renewables
- **Interactive Time Series**: Dynamic energy consumption trends over decades
- **Energy Mix Visualization**: Pie charts showing country-specific energy portfolios
- **Top Consumers Ranking**: Horizontal bar charts of highest energy-consuming nations
- **Renewable Growth Tracking**: Dedicated analysis of clean energy adoption
- **Automated Insights**: AI-generated key findings and growth rate calculations
- **Multi-country Comparison**: Side-by-side analysis of selected countries

## 📊 Dashboard Overview

### Key Metrics
- **Global Energy Consumption**: Total worldwide energy usage in TWh
- **Country Averages**: Mean consumption per nation
- **Renewable Share**: Percentage of clean energy in global mix
- **Coverage**: Number of countries analyzed

### Analysis Sections
1. **📈 Consumption Trends**: Time-series analysis of energy usage patterns
2. **🥧 Energy Mix**: Breakdown by energy source (coal, gas, oil, nuclear, renewables)
3. **🏆 Top Consumers**: Ranking of highest energy-consuming countries
4. **🌱 Renewable Growth**: Clean energy adoption trends over time
5. **💡 Smart Insights**: Automated identification of key patterns and leaders

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- World Energy Consumption dataset from Kaggle

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Kiwi-520/energy-consumption-dashboard.git
cd energy-consumption-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the dataset**
   - Visit [Kaggle Dataset](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption/data)
   - Download `World Energy Consumption.csv`
   - Place the file in the project root directory

4. **Run the application**
```bash
streamlit run energy_dashboard.py
```

5. **Access the dashboard**
   - Open your browser and go to `http://localhost:8501`
   - Select countries and time ranges for analysis

## 📋 Requirements

```txt
streamlit==1.28.0
pandas==2.0.3
plotly==5.16.1
numpy==1.24.3
```

## 🎯 Usage

### Getting Started
1. **Sample Data Mode**: If dataset not available, the app generates realistic sample data
2. **Real Data Analysis**: Download the Kaggle dataset for actual global energy data
3. **Country Selection**: Choose specific countries from the sidebar
4. **Time Range**: Select years for focused analysis
5. **Interactive Exploration**: Click through different visualizations and insights

### Dashboard Controls
- **Country Filter**: Multi-select dropdown for country comparison
- **Year Range Slider**: Focus on specific time periods
- **Energy Mix Selector**: Choose country and year for detailed energy breakdown
- **Top Consumers Year**: Select year for ranking analysis

### Key Insights Generated
- **🏆 Highest Consumer**: Country with maximum energy consumption
- **📈 Fastest Growing**: Nation with highest energy growth rate
- **🌱 Most Renewable**: Country with highest clean energy percentage

## 🏗️ Project Structure

```
energy-consumption-dashboard/
├── energy_dashboard.py        # Main application file
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── World Energy Consumption.csv  # Dataset (download from Kaggle)
└── .gitignore              # Git ignore file
```

## 🔧 Technical Implementation

### Data Processing
- **Pandas Operations**: Data cleaning, filtering, and aggregation
- **Time Series Analysis**: Year-over-year growth calculations
- **Energy Source Categorization**: Grouping fossil fuels vs renewables
- **Missing Data Handling**: Intelligent filling of missing values

### Visualization Engine
- **Plotly Express**: Interactive line charts, bar charts, and pie charts
- **Multi-subplot Layouts**: Coordinated visualizations
- **Color Schemes**: Consistent energy-themed color palettes
- **Responsive Design**: Adaptive layouts for various screen sizes

### Analytics Features
- **Growth Rate Calculations**: Compound annual growth rate (CAGR) computation
- **Renewable Percentage**: Real-time calculation of clean energy share
- **Country Rankings**: Dynamic sorting by consumption metrics
- **Statistical Insights**: Automated pattern recognition and key findings

## 📈 Supported Energy Sources

### Fossil Fuels
- **Coal Consumption**: Traditional coal-based energy
- **Natural Gas**: Gas-powered generation
- **Oil Consumption**: Petroleum-based energy

### Clean Energy
- **Nuclear**: Nuclear power generation
- **Hydroelectric**: Water-powered energy
- **Wind Power**: Wind turbine generation
- **Solar Energy**: Photovoltaic and thermal solar
- **Other Renewables**: Geothermal, biomass, and other clean sources

## 🌍 Dataset Coverage

- **Time Range**: 1965-2022 (varies by country)
- **Geographic Coverage**: 200+ countries and territories
- **Data Sources**: BP Statistical Review, EMBER, Energy Institute
- **Metrics**: Consumption in TWh, per capita usage, energy mix percentages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/energy-analysis`)
3. Commit your changes (`git commit -m 'Add energy efficiency analysis'`)
4. Push to the branch (`git push origin feature/energy-analysis`)
5. Open a Pull Request

### Contribution Ideas
- Add energy efficiency metrics
- Implement forecasting models
- Create carbon emissions correlation
- Add geographic heat maps
- Develop energy policy recommendations

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kiwi-520**
- GitHub: [@Kiwi-520](https://github.com/Kiwi-520)
- Project Link: [https://github.com/Kiwi-520/energy-consumption-dashboard](https://github.com/Kiwi-520/energy-consumption-dashboard)

## 🙏 Acknowledgments

- [Kaggle](https://www.kaggle.com/) and dataset contributors for comprehensive energy data
- [Streamlit](https://streamlit.io/) for the intuitive web app framework
- [Plotly](https://plotly.com/) for powerful interactive visualizations
- [BP Statistical Review](https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html) for historical energy data

## 📊 Data Sources

- **Primary**: World Energy Consumption Dataset (Kaggle)
- **Original Sources**: BP Statistical Review, EMBER, Energy Institute
- **Update Frequency**: Annual updates
- **Data Quality**: Verified and cross-referenced energy statistics

---

⭐ **Star this repository if you found it helpful for your energy analysis projects!**

🔗 **Live Demo**: [Coming Soon - Streamlit Cloud Deployment]
