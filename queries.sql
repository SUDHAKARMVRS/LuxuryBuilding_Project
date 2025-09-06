 #1.
SELECT purchase_year_quarter, quarter_number, micro_market, COUNT(*) AS booking_count
FROM dbo.luxury_housing_cleaned
GROUP BY purchase_year_quarter, quarter_number, micro_market
ORDER BY quarter_number, micro_market;

#2.
SELECT developer_name,
       SUM(ticket_price_cr) AS total_ticket_sales,
       AVG(ticket_price_cr) AS avg_ticket_size
FROM dbo.luxury_housing_cleaned
GROUP BY developer_name
ORDER BY total_ticket_sales DESC;

#3.
SELECT amenity_score,
       COUNT(DISTINCT project_name) AS project_count,
       1.0 * SUM(CASE WHEN transaction_type = 'Primary' THEN 1 ELSE 0 END) / COUNT(*) AS primary_share
FROM dbo.luxury_housing_cleaned
GROUP BY amenity_score
ORDER BY amenity_score;

#4.
SELECT micro_market, transaction_type, COUNT(*) AS cnt
FROM dbo.luxury_housing_cleaned
GROUP BY micro_market, transaction_type;

#5.
SELECT configuration, COUNT(*) AS booking_count
FROM dbo.luxury_housing_cleaned
GROUP BY configuration
ORDER BY booking_count DESC;

#6.
SELECT sales_channel, transaction_type, COUNT(*) AS cnt
FROM dbo.luxury_housing_cleaned
GROUP BY sales_channel, transaction_type;

#7.
SELECT developer_name, purchase_year_quarter, quarter_number,
       SUM(ticket_price_cr) AS total_ticket_sales
FROM dbo.luxury_housing_cleaned
GROUP BY developer_name, purchase_year_quarter, quarter_number
ORDER BY developer_name, quarter_number;

#8.
SELECT possession_status, buyer_type, COUNT(*) AS cnt
FROM dbo.luxury_housing_cleaned
GROUP BY possession_status, buyer_type;

#9.
SELECT micro_market, COUNT(*) AS project_count
FROM dbo.luxury_housing_cleaned
GROUP BY micro_market
ORDER BY project_count DESC;

#10.
SELECT TOP 5 developer_name,
       SUM(ticket_price_cr) AS total_revenue,
       1.0 * SUM(CASE WHEN transaction_type = 'Primary' THEN 1 ELSE 0 END) / COUNT(*) AS primary_share
FROM dbo.luxury_housing_cleaned
GROUP BY developer_name
ORDER BY total_revenue DESC;

#11.
SELECT micro_market,
       MAX(price_per_sqft) AS max_price_per_sqft,
       MIN(price_per_sqft) AS min_price_per_sqft,
       AVG(price_per_sqft) AS avg_price_per_sqft
FROM luxury_house
GROUP BY micro_market
ORDER BY avg_price_per_sqft DESC;

#12.
SELECT developer_name,
       SUM(ticket_price_cr) AS total_revenue,
       1.0 * SUM(CASE WHEN transaction_type = 'Primary' THEN 1 ELSE 0 END) / COUNT(*) AS primary_share,
       1.0 * SUM(CASE WHEN transaction_type = 'Secondary' THEN 1 ELSE 0 END) / COUNT(*) AS secondary_share

FROM luxury_house
GROUP BY developer_name
ORDER BY total_revenue DESC;

#13.
SELECT micro_market, COUNT(*) AS project_count
FROM  luxury_house
GROUP BY micro_market
ORDER BY project_count DESC;

#14.
SELECT possession_status, buyer_type, COUNT(*) AS cnt
FROM luxury_house
GROUP BY possession_status, buyer_type
ORDER BY possession_status;

#15.
SELECT sales_channel, transaction_type, COUNT(*) AS cnt
FROM luxury_house
GROUP BY sales_channel, transaction_type;

#16.
SELECT transaction_type,
       SUM(ticket_price_cr) AS total_revenue_cr,
       COUNT(*) AS total_qty,
       ROUND((100.0 * SUM(ticket_price_cr) / (SELECT SUM(ticket_price_cr) FROM luxury_house))::numeric, 3) AS revenue_percentage
FROM luxury_house
GROUP BY transaction_type
ORDER BY revenue_percentage DESC;

#17.
SELECT quarter_number,SUM(ticket_price_cr) AS total_revenue FROM luxury_house
GROUP BY quarter_number
ORDER BY quarter_number ASC;
