
# 🏙️ Luxury Housing Sales Analysis  

---

## 📌 Overview
This project analyzes the **luxury housing market** to uncover sales trends, buyer preferences, and builder performance. Using **Python, SQL, and Power BI**, the project provides **interactive dashboards and insights** that support strategic decision-making.  

### 🔑 Key Highlights  
- **Top Builders** → Ranked by revenue & booking success.  
- **Buyer Insights** → Preferences, comments, and purchase patterns.  
- **Market Trends** → Ticket price analysis across micro-markets.  
- **Dashboards** → Sales, Buyer, and Market performance visualized in Power BI.  

---

## ⚙️ Technical Details (For Developers)  

### 📂 Dataset  
Includes project details: builder, price, configuration, locality, scores (amenity, infra, connectivity), buyer type, comments, and booking status.  

### 🛠 Tools & Technologies  
- **Python** → Data cleaning, analysis, visualization (Pandas, Plotly, Seaborn).  
- **SQL (PostgreSQL/MySQL)** → Data queries & transformations.  
- **Power BI** → Dashboards & storytelling.  

### 📊 Core Analyses  
- Builder-wise revenue & bookings.  
- Buyer segmentation (NRI vs Non NRI).
- Buyer wise transactions.
- Primary vs Secondary transactions.
- Configuration demand among buyers.

## 🚀 Project Workflow

### 📥 Data Ingestion

 - Source: Luxury_Housing_Bangalore.csv
 - Loaded into Python using Pandas.

### 🧹 Data Cleaning (Python)

- Removed currency symbols from Ticket_Price_Cr.
- Handled missing values (mean/median imputation).
- Normalized text fields (lowercase, trimmed spaces).
- Standardized Configuration (e.g., 3bhk,3BHK → 3 BHK).
- Corrected invalid Unit_Size_Sqft.

### 🛠️ Feature Engineering
  
 - Price_per_Sqft = (Ticket_Price_Cr * 1e7) / Unit_Size_Sqft
 - Quarter_Number extracted from Purchase_Quarter.
 - Booking_Flag → 1 if Primary Booked, else 0.

### 🗄️ SQL Storage
 - Cleaned dataset pushed into PostgreSQL.
 - Table: luxury_housing_sales.

### 📊 Power BI Visualization
 - Direct connection to PostgreSQL.
 - Built visuals: KPIs, Bar/Line/Scatter/Donut charts.
 - DAX measures created for revenue, price, amenity, booking conversion.
  
## 🚀 How to Run  

**Install dependencies**

  pip install -r requirements.txt

**Run Python analysis**

  python Lux_Hou_Sal.py
  
**Open the Power BI file**  

`  Lb.pbix`  

# 📈 **Sample Insights**
- 50% of revenue comes from top 5 builders out 0f 11.
- 5BHK units dominate sales in premium micro-markets.
- Under-construction projects have higher booking conversion vs ready-to-move.
- NRI and Non NRI both had a equal level of buying percentage.Non NRI slighltly higher sid by 1%.


# 📷 **Screenshots**
<img width="1272" height="713" alt="Screenshot 2025-08-18 203421" src="https://github.com/user-attachments/assets/2123a2ba-14de-4cab-b3cb-034a70597b8c" />
<img width="1235" height="688" alt="Screenshot 2025-09-06 120156" src="https://github.com/user-attachments/assets/5f10eced-7b73-44ff-83a9-751f5ef09a69" />
<img width="1239" height="693" alt="Screenshot 2025-09-06 115923" src="https://github.com/user-attachments/assets/bbd4b662-5b93-445a-8a36-4e3786927263" />
<img width="1257" height="694" alt="Screenshot 2025-08-18 203455" src="https://github.com/user-attachments/assets/ba0cc5c2-9904-4a5b-b634-3adbdc666417" />





---

## 👨‍💻 Author  
**Sudhakar M**  
📧sudhakar.mvrs@gmail.com| 🌐 (https://www.linkedin.com/in/sudhakar-m-657ba787/) 
