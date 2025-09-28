# Smartphone Market Analysis — Web Scraping, EDA & Feature Engineering

##  Overview
This project focuses on building a structured smartphone dataset by **scraping Smartprix**, cleaning and standardizing the data, engineering new features (including **PPI: Pixels Per Inch**), and conducting exploratory data analysis (EDA).  
The goal was to identify **key price drivers** and uncover **market insights** in the smartphone industry.

---

##  What I Did

### 🔹 Web Scraping
- Automated data collection using **Selenium** to fetch HTML pages.  
- Parsed product specifications (price, RAM, storage, display, etc.) with **BeautifulSoup**.

### 🔹 Data Wrangling
- Cleaned and standardized raw data with **pandas** and **NumPy**.  
- Handled missing values, inconsistent units, and duplicate entries.  

### 🔹 Feature Engineering
- Created a new metric **PPI (Pixel Per Inch)** to better capture display sharpness.  

### 🔹 Exploratory Data Analysis (EDA)
- Conducted **univariate & bivariate analysis**, **correlation analysis**, and built visualizations using **matplotlib** & **seaborn**.  
- Surfaced patterns to identify **features most correlated with price**.

---

## 🔑 Key Insights
- **Top price drivers**: Processor speed, display resolution, storage, and RAM showed the strongest positive correlations with price.  
- **PPI (pixel density)**: Higher display sharpness generally associated with costlier phones.  
- **Ratings & 5G/NFC features**: Positively linked with higher prices and customer perception.  
- **Expandable storage**: Negatively correlated — phones with memory card slots tend to be budget-friendly models.  
- **Camera megapixels**: Surprisingly weak predictor of price compared to hardware specs like RAM and processor.  
