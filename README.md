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

[Imagem 1](1.%20Data%20Platform%20Architecture%20and%20OLTP%20Database/1-createtable.png)

I performed a similar operation with another database in MongoDB. I imported a file into it, performed queries, created an index to improve query performance and exported the database.

3-mongoimport.png

4-create-index.png

5-mongo-query-mobiles2.png

I also designed and created a star schema for a database which was supposed to hold 
ecommerce data on PostgreSQL. Then I performed several queries on the database, from 
simple select queries to groupingsets, cubes, rollups and created a materialized view.

6-softcartRelationships.png

7-groupingsets.png

8-cube.png

9-mqt.png

I imported a dataset into IBM Cognos Dashboards and created dashboards such as a bar graph to
show mobile phone sales in each quarter, a line graph to show sales for each month
of 2022, and a pie chart to show sales for three product categories.

10-barchart.png

11-linechart.png

12-piechart.png

I automated the process of retrieving the latest records from a MySQL table and 
inserting them into a PostgreSQL data warehouse. Below are the Python functions 
that fetch the records, insert them and the output I got after executing the script. 


## Get in touch:

- [LinkedIn](https://www.linkedin.com/in/ericmidt/)
- [GitHub](https://github.com/ericmidt)
