import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Load Data
def load_data(file_path):
    """Load the raw CSV file."""
    lxdf = pd.read_csv(file_path)
    return lxdf

# Data frame Creation
def data_frame(data):
    data_frame = pd.DataFrame(data)
    return data_frame

def clean_data(lxdf): 
    # Lowercase column names
    lxdf.columns = lxdf.columns.str.strip().str.lower()

    # Convert Ticket_Price_Cr to numeric
    lxdf['ticket_price_cr'] = (
        lxdf['ticket_price_cr']
        .astype(str)
        .str.replace('₹', '', regex=False)
        .str.replace('Cr', '', regex=False)
        .str.strip()
        .astype(float)
        .round(2)
    )

    # Handle missing values
    lxdf['amenity_score'] = lxdf['amenity_score'].fillna(lxdf['amenity_score'].mean())
    # Convert to float (invalid parsing becomes NaN)
    lxdf['ticket_price_cr'] = pd.to_numeric(lxdf['ticket_price_cr'], errors='coerce')
    lxdf['unit_size_sqft'] = pd.to_numeric(lxdf['unit_size_sqft'], errors='coerce')

    # Replace negative values with NaN
    lxdf.loc[lxdf['ticket_price_cr'] < 0, 'ticket_price_cr'] = np.nan
    lxdf.loc[lxdf['unit_size_sqft'] < 0,'unit_size_sqft']= np.nan

    # Fill NaN with median
    lxdf['ticket_price_cr'] = lxdf['ticket_price_cr'].fillna(lxdf['ticket_price_cr'].median())
    lxdf['unit_size_sqft'] = lxdf['unit_size_sqft'].fillna(lxdf['unit_size_sqft'].median())

    # Clean configuration
    lxdf['configuration'] = lxdf['configuration'].str.strip().str.upper()
    lxdf['configuration'] = lxdf['configuration'].str.replace(r'(\d)(BHK)', r'\1 BHK', regex=True)

    # Market names 
    lxdf['micro_market'] = lxdf['micro_market'].str.strip().str.title()
    lxdf['buyer_comments'] = lxdf['buyer_comments'].fillna('No Comments Provided.')
    # Price per sqft
    lxdf['price_per_sqft'] = (lxdf['ticket_price_cr'] * 1e7) / lxdf['unit_size_sqft'] 

    # Quarter number
    lxdf['quarter_number'] = pd.PeriodIndex(lxdf['purchase_quarter'], freq='Q').quarter 

    # Replace invalid sqft & fill median
    lxdf.loc[lxdf['unit_size_sqft'] <= 0, 'unit_size_sqft'] = np.nan
    lxdf['unit_size_sqft'] = lxdf.groupby('configuration')['unit_size_sqft'].transform(
        lambda x: x.fillna(x.median())
    )
    # Decimal ratio reduction
    lxdf[['connectivity_score',
          'amenity_score','locality_infra_score']] = (lxdf[['connectivity_score','amenity_score',
                                                            'locality_infra_score']].astype('float64').round(2))


    # Normalize selected text columns
    text_cols = ['property_id', 'micro_market', 'project_name', 'developer_name',
                 'transaction_type', 'buyer_type', 'purchase_quarter',
                 'possession_status', 'sales_channel', 'nri_buyer', 'buyer_comments'] 
    for col in text_cols:
        if col in lxdf.columns:
            lxdf[col] = lxdf[col].astype(str).str.strip()

    # Booking flag: assume booked if purchase_quarter is not null/empty
    lxdf['booking_flag'] = lxdf['purchase_quarter'].apply(lambda x: 0 if pd.isna(x) or x.strip() == '' else 1)

    return lxdf


# Load Data to SQL
def load_to_sql(lxdf, table_name, db_url):
    """Load cleaned DataFrame into SQL database."""
    engine = create_engine(db_url)
    lxdf.to_sql(table_name, con=engine, index=False, if_exists='replace')

# Main execution
if __name__ == "__main__":
    file_path = "Luxury_Housing_Bangalore.csv"
    db_url = 'postgresql://postgres:sugana@localhost:5432/LuxHou_Project'

    df_raw = load_data(file_path)
    df_clean = clean_data(df_raw)
    load_to_sql(df_clean, "luxury_house", db_url)
    print("It Works.")