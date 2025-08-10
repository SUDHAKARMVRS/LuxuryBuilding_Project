# ==========================
# LUXURY HOUSING SALES - DATA CLEANING & SQL LOADING
# ==========================

import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# --------------------------
# 1. Load Raw Data
# --------------------------
def load_data(file_path):
    """Load the raw CSV file."""
    df = pd.read_csv('Luxury_Housing_Bangalore.csv')
    print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

# --------------------------
# 2. Data Cleaning
# --------------------------
def clean_data(df):
    """Clean and preprocess the dataset."""
    # Strip spaces and normalize text columns
    text_cols = ['Builder', 'Micro_Market', 'Configuration', 'Possession_Status',
                 'Sales_Channel', 'Buyer_Type', 'Booking_Status']
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.title()

    # Convert Ticket_Price_Cr to numeric
    df['Ticket_Price_Cr'] = (
        df['Ticket_Price_Cr']
        .astype(str)
        .str.replace('[₹,]', '', regex=True)
        .astype(float)
    )

    # Handle missing values
    df['Amenity_Score'] = df['Amenity_Score'].fillna(df['Amenity_Score'].mean())
    df['Booking_Status'] = df['Booking_Status'].replace({'nan': 'Unknown'})

    # Feature Engineering
    df['Price_per_Sqft'] = (df['Ticket_Price_Cr'] * 1e7) / df['Area_Sqft']
    df['Quarter_Number'] = pd.PeriodIndex(df['Purchase_Quarter'], freq='Q').quarter
    df['Booking_Flag'] = df['Booking_Status'].apply(lambda x: 1 if x.lower() == 'booked' else 0)

    return df

# --------------------------
# 3. Load into SQL
# --------------------------
def load_to_sql(df, table_name, db_url):
    """Load cleaned DataFrame into SQL database."""
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')
    print(f"Data successfully loaded into table: {table_name}")

# --------------------------
# 4. Main Execution
# --------------------------
if __name__ == "__main__":
    # File path (change only this if needed)
    file_path = "luxury_housing_raw.csv"

    # DB connection (PostgreSQL example)
    db_url = "postgresql://postgres:password@localhost:5432/luxury_housing"

    # Run Pipeline
    raw_df = load_data(file_path)
    clean_df = clean_data(raw_df)
    load_to_sql(clean_df, "luxury_housing_sales", db_url)

    print("✅ Pipeline completed.")
