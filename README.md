# Data Wrangling: Olist Marketplace Database



## A. Background
Marketplace is a platform to connect both buyers and sellers to do transactions between these two parties. The sellers can sell their products while buyers can buy the available products. Nowadays, we use a marketplace due to efficiency in shopping. The sellers can sell anything as long as the products fulfil the conditions given by the marketplace. The buyers can buy their needs from various shops.
In order for the marketplace to improve its service, analysing those transactions between buyers and sellers is essential. The objective focused on how customer preferences can help the marketplace in gaining more transactions.

**Note:** The data values used in this project are mainly in Portuguese while the feature names are in English



## B. Objectives
### I. Learning Objectives
This project is built to implement data wrangling skills by using the Pandas Library in Python and JOIN query in SQL. The highlighted steps in this project are cleaning and manipulating the data.
### II. Analysis Objectives
This project aims to analyse customer preferences in order to improve Olist marketplace service. The objectives which will be analysed are:
1. What are the top 10 best-selling product categories in the Olist marketplace?
2. What is the most-used payment type for transactions in the Olist marketplace?
3. What are the names of 5 cities where most of Olist marketplace customers reside?



## C. Dataset
This project used the Olist database which contains various details regarding the customer, seller, product, and transactions done in the Olist marketplace.
![image](https://github.com/novitaaryanti/olist_marketplace_wrangling_project/assets/138101831/16df03e7-7e3d-4b3d-a737-a3eb84c69e29)
The Olist database consists of several datasets including:
1. Olist Customers (`olist_order_customer_dataset`)
2. Olist Geolocation (`olist_geolocation_dataset`)
3. Olist Order Items (`olist_order_items_dataset`)
4. Olist Order Payment (`olist_order_payments_dataset`)
5. Olist Order Review (`olist_oder_reviews_dataset`)
6. Olist Orders (`olist_orders_dataset`)
7. Olist Products (`olist_products_dataset`)
8. Olist Seller (`olist_sellers_dataset`)
9. Product Category Name Translation (`product_category_name_translation`)

The datasets used for this project are:
1. Olist Order Items
2. Olist Products
3. Product Category Name Translation
4. Olist Order Payment
5. Olist Orders
6. Olist Customers

> Due to the limited file size from GitHub, the database is not added to this repository



## D. Workflow
This program contains two modules, which are `wrangling.py` and `data_wrangling_analysis.ipynb`:
1. Module `wrangling.py` includes several functions which will be used for extracting, cleaning, wrangling, and manipulating the data:
   - Function `open_database()` to open the database and get the dataset list.
   - Function `open_dataset()` to open all datasets for inspection purposes.
   - Function `read_query_dataset()` to extract and join relevant datasets from the database.
   - Function `translate_category_to_english()` to manually translate the remaining original product categories which haven't had the English translation.
   - Function `text_normalization()` to do simple normalization in order to remove unrelated characters.
   - Function `compare_column_consistency()` to compare the number of columns to check their consistency.
   - Function `create_plot()` to create a plot from the relevant data.
2. Notebook `data_wrangling_analysis.ipynb` where all the wrangling and analysing processes are done.

### 1. Exploring and extracting Data from Database (Data Wrangling)
Use functions `open_database()`, `open_dataset()`, and `read_query_dataset()` in order to connect the database, open the datasets, and extract relevant data features from the dataset
### 2. Data Cleaning
Each objective requires different approaches to data cleaning. The highlighted processes of data cleaning from this project are handling missing data, handling inconsistent format, and handling duplicate data.
### 3. Data Manipulation
Grouping data using relevant features in order to gain insight for objective analysis purposes.
### 4. Plot Graph
Plotting the graph which suits the objective
### 5. Analysis
Analysing the objective to gain business recommendations in order to improve the service of the Olist marketplace and gain more customers to do more transactions.



## E. Result & Conclusions
The analysis result and conclusions are already explained in my Medium story titled [**Data Wrangling Project: Customer Preferences Analysis from Marketplace**](https://medium.com/@novitaaryanti25/data-wrangling-project-customer-preferences-analysis-from-marketplace-564cfe24b484)



## F. Future Work
This database can be used to gain more objective insights.
