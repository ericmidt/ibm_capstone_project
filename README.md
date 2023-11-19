# IBM Capstone Data Engineering Project
## Overview
This project explored several data engineering technologies, concepts and skills that I acquired while completing the IBM Data Engineering Professional Certificate.


### Data Platform Architecture and OLTP Database

Designed and implemented a data platform using MySQL as an OLTP database, and another using MongoDB.

### PostgreSQL Data Warehouse

Designed and implemented a data warehouse on PostgreSQL using a star schema and performed various queries.

### Data Analytics and IBM Cognos Dashboards
Loaded the data into IBM Cognos Analytics and created dashboards.

### ETL & Data Pipeline (Airflow, Python and Bash)
Automated the process of loading data from MySQL to a PostgreSQL data warehouse.
Used Airflow to create a pipeline that analyzes web server logs, extracts the required lines and fields, transforms and loads the data.

### Big Data Analytics with PySpark
Used PySpark and data from a webserver to analyze search terms, and loaded a pretrained sales forecasting model to predict the forecast for a future year based on given sales data.



Below is a summary of some of the tasks I performed and some of the screenshots I took during the project.



In the first section of the project, I created a table on MySQL for sales data. And 
then I inserted sales data from a sales_data.sql into the table. I also 
queried the table, performed operations and exported the data.

<p align="center">
  <img src="1.%20Data%20Platform%20Architecture%20and%20OLTP%20Database/1-createtable.png" alt="Imagem 1">
</p>

<p align="center">
  <img src="1. Data Platform Architecture and OLTP Database/6-exportdata.png" alt="Imagem 2">
</p>

I performed a similar operation with another database in MongoDB. I imported a file into it, performed queries, created an index to improve query performance and exported the database.

<p align="center">
  <img src="2. Querying Data in NoSQL Databases/1-mongoimport.png" alt="Imagem 3">
</p>

<p align="center">
  <img src="2. Querying Data in NoSQL Databases/4-create-index.png" alt="Imagem 4">
</p>

<p align="center">
  <img src="2. Querying Data in NoSQL Databases/7-mongo-query-mobiles2.png" alt="Imagem 5">
</p>

I also designed and created a star schema for a database which was supposed to hold 
ecommerce data on PostgreSQL. Then I performed several queries on the database, from 
simple select queries to groupingsets, cubes, rollups and created a materialized view.

<p align="center">
  <img src="3. PostgreSQL Data Warehouse/design & setup/4-softcartRelationships.png" alt="Imagem 6">
</p>

<p align="center">
  <img src="3. PostgreSQL Data Warehouse/reporting/5-groupingsets.png" alt="Imagem 7">
</p>

<p align="center">
  <img src="3. PostgreSQL Data Warehouse/reporting/7-cube.png" alt="Imagem 8">
</p>

<p align="center">
  <img src="3. PostgreSQL Data Warehouse/reporting/8-mqt.png" alt="Imagem 9">
</p>

I imported a dataset into IBM Cognos Dashboards and created dashboards such as a bar graph to
show mobile phone sales in each quarter, a line graph to show sales for each month
of 2022, and a pie chart to show sales for three product categories.

<p align="center">
  <img src="4. Data Analytics (Cognos Dashboard)/barchart.png" alt="Imagem 10">
</p>


<p align="center">
  <img src="4. Data Analytics (Cognos Dashboard)/linechart.png" alt="Imagem 11">
</p>


<p align="center">
  <img src="/4. Data Analytics (Cognos Dashboard)/piechart.png" alt="Imagem 12">
</p>

I automated the process of retrieving the latest records from a MySQL table and 
inserting them into a PostgreSQL data warehouse. Below are the Python functions 
that fetch the records, insert them and the output I got after executing the script. 

<p align="center">
  <img src="/5. ETL & Data Pipeline (Airflow)/ETL/get_latest_records.png" alt="Imagem 13">
</p>


<p align="center">
  <img src="/5. ETL & Data Pipeline (Airflow)/ETL/insert_records.png" alt="Imagem 14">
</p>


<p align="center">
  <img src="/5. ETL & Data Pipeline (Airflow)/ETL/synchronization.png" alt="Imagem 15">
</p>

I used Airflow to create a data pipeline that extracts specific IP addresses from a 
access log file and loads them into a destination file.

<p align="center">
  <img src="/5. ETL & Data Pipeline (Airflow)/Airflow/DAG.png" alt="Imagem 16">
</p>

<p align="center">
  <img src="/5. ETL & Data Pipeline (Airflow)/Airflow/dag_runs.png" alt="Imagem 17">
</p>

I used PySpark to load a sales prediction model, apply it to a sales data set,  
and predict the sales for the year 2023.

<p align="center">
  <img src="/6. Big Data Analytics with Spark/import_model.png" alt="Imagem 18">
</p>

<p align="center">
  <img src="/6. Big Data Analytics with Spark/predict_sales.png" alt="Imagem 19">
</p>


## Get in touch:

- [LinkedIn](https://www.linkedin.com/in/ericmidt/)
- [GitHub](https://github.com/ericmidt)
