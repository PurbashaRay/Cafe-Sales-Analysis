## Cafe-Sales-Analysis<br><br>
### Project Overview <br>

This project focuses on analyzing and visualizing sales performance for a Cafe business. The objective is to provide meaningful insights into sales, profit, and customer purchasing behavior using data analytics tools.
The dataset was cleaned and prepared using Python, ensuring all sensitive customer information was anonymized at the earliest stage of data processing. The cleaned data was then used to build interactive dashboards in Power BI.

### 🎯 Objectives<br>
- Analyze sales and profit performance by store<br>
- Calculate profit using a 50% markup (as per cafe business requirement)<br>
- Understand customer buying patterns<br>
- Identify popular products and purchase frequency<br>
- Analyze payment methods used by customers<br>
- Recommend effective data visualization techniques<br>

## 🛠️ Tools & Technologies
- **Python**
  - Data cleaning and preprocessing
- **Power BI**
  - Data visualisation and dashboard creation

## 🔐 Data Cleaning & Preparation

- Removed sensitive data (card numbers)
- Anonymised customer names into `cust_xxx`
- Created a new calculated column Profit (Profit = 50% markup on sales)
- Created a DAX calculated column in Power BI to extract the month from the Date/Time field.

## 📈 Visualisations (Power BI)
- Bar charts → Sales & Profit by product/store
- Line charts → Sales & Profit trends over time
- Donut charts → Payment method distribution
- KPI cards → Total sales,profit & item sold

## 📊 Dashboard<br>

![Image](https://github.com/PurbashaRay/Cafe-Sales-Analysis/blob/7b228943302f0ae21c7be44d2ca60e206f473556/image/overview.png)



## 💡 Key Insights

- Woking is the best-performing branch, followed by Guildford, Epsom, and Redhill.

- August 2024 recorded the highest sales and profit. There was a sharp decline in September, with October and November remaining low and stable, followed by a strong recovery in December.

- Macchiato is the most popular product, followed by Espresso, Americano, and Latte, while Mocha is the least popular.

- Products such as Americano, Latte, and Mocha show very low or negligible sales across most branches.

## 🚀 Recommendations

- Treat Woking as a benchmark and replicate the successful strategies in other branches .
- For mid preforming branches like Guilford and Epsom consider targeted promotion and local campaigns.
- For Redhill branch investigate the cause for low sales . Introduce promotions, campaigns, revisit staffing.
- Consider branch specific menu optimisations :
 - Woking- Stock heavily on Macchiato and Espresso
 - Epsom- Focus on Latte-based promotions
 - Guildford and Redhill -Review product mix and reduce low-demand items

## 📌 Future Improvements

- Integrate real-time or automated data updates using APIs or scheduled refreshes
- Perform customer segmentation (e.g., frequent vs occasional buyers)
- Add predictive analysis to forecast future sales and demand
- Enhance dashboards with interactive filters and drill-through features
- Include additional metrics such as customer lifetime value and average order value
- Expand analysis to multiple business types for comparison
- Improve data quality checks and validation processes
- Incorporate external factors (e.g., seasonality, holidays) for deeper insights

