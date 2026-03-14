# Amazon Product Data Analysis (SQL + Python + Power BI)

## Project Overview

This project performs end-to-end data analysis on an Amazon product dataset to uncover insights related to pricing, product ratings, discounts, and customer engagement.

The goal of this project is to demonstrate a complete data analytics workflow including data cleaning, exploratory analysis, and data visualization using SQL, Python, and Power BI.

## Tools & Technologies

* SQL (MySQL)
* Python (Pandas, NumPy, Matplotlib)
* Power BI
* CSV Dataset

## Dataset

The dataset contains Amazon product listings with the following attributes:

* Product ID
* Product Name
* Category
* Discounted Price
* Actual Price
* Discount Percentage
* Product Rating
* Rating Count

Total Records: ~1400 products

## Project Workflow

### 1. Data Cleaning (Python)

* Removed currency symbols and formatting issues
* Converted price columns into numeric values
* Handled missing values and inconsistent data types

### 2. Exploratory Data Analysis (Python)

Performed statistical analysis and visualization to understand:

* Price distribution
* Rating trends
* Category performance
* Relationship between discount and ratings

### 3. SQL Analysis

SQL queries were used to analyze product performance including:

* Top-rated products
* Most reviewed products
* Highest discount products
* Average rating by category
* Product price segmentation

### Example SQL Query

SELECT product_name, rating
FROM amazon_products
ORDER BY rating DESC
LIMIT 10;

### 4. Power BI Dashboard

An interactive Power BI dashboard was created to visualize:

* Product ratings
* Category performance
* Price distribution
* Top reviewed products

## Key Insights

* Products with higher review counts tend to maintain ratings above 4.0.
* Large discounts do not necessarily lead to higher product ratings.
* Most products fall within the medium price range.
* Certain categories consistently perform better in customer satisfaction.

## Future Improvements

* Sentiment analysis on product reviews using NLP
* Predictive modeling for product rating trends
* Customer segmentation analysis

## Project Structure

amazon-product-data-analysis
│
├── data
│   └── amazon.csv
│
├── python
│   └── analysis.ipynb
│
├── sql
│   └── analysis_queries.sql
│
├── powerbi
│   └── dashboard.pbix
│
└── README.md
