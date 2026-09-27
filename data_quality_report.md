 PharmEasy Regional Pulse – Data Quality Report

The raw PharmEasy order data contained some data quality issues that needed to be fixed before doing any analysis. I cleaned the data step by step and checked that the final dataset was complete and ready for further analysis.

 Data Quality Issues and Fixes

 1. Duplicate Rows – Uniqueness

The raw dataset contained exact duplicate rows. I removed these duplicate records so that the same order would not be counted more than once.

 fixed:Removed 59 exact duplicate rows.

Data quality dimension: Uniqueness

2. Inconsistent Region Names – Consistency

Some region names had extra spaces or different capitalization, such as hyderabad, HYDERABAD, and Hyderabad. These values referred to the same region but were written differently.

I removed unnecessary spaces and converted the region names to title case so that they followed a consistent format.

 fixed:Normalized the region column.

Data quality dimension: Consistency

3. Missing Category Values – Completeness and Accuracy

Some orders did not have a category value. However, every product in the dataset belongs to one specific category.

I created a product-to-category lookup using the rows where the category was already available. I then used this lookup to fill the missing category values.

 fixed:Filled all missing category values using the product name.

Data quality dimensions:Completeness and Accuracy

 4. Missing Profit Values – Completeness

Some orders were missing their profit_inr value. Instead of removing these orders, I calculated the average profit margin for each category.

I then used the category's average profit margin and the order's sales value to calculate the missing profit.

fixed: Filled missing profit values using the category-specific average profit margin.

Data quality dimension:Completeness

5. Required Columns – Validity

I also checked whether all the columns required for the analysis were present in the cleaned dataset.

The`validate_schema() function checks for missing columns and returns either validated or blocked_schema.

fixed: Added schema validation before using the cleaned data.

Data quality dimension:Validity

6. Monthly Data – Timeliness

The dataset contains order records for April, May, and June 2026. The cleaning pipeline processes this monthly order data so that it can be used for month-to-month regional performance analysis.

Data quality dimension: Timeliness

7. Data Needed for Analysis – Relevance

The important order and regional fields were retained because they are needed for the regional performance analysis. These include region, category, sales, profit, quantity, and order information.

Data quality dimension:Relevance

Final Result

After cleaning the raw data:

- 59 duplicate rows were removed.
- 2100 clean rows remained.
- Region names were standardized.
- Missing category values were filled.
- Missing profit values were filled.
- The cleaned dataset was checked using schema validation.
- The final dataset was saved as' orders_clean.csv'.
