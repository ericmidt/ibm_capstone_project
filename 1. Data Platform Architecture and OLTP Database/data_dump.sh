#!/bin/bash

# MySQL Connection Details
MYSQL_HOST="127.0.0.1"
MYSQL_USER="root"
MYSQL_PASSWORD="MTgwOTEtZXJpY3Nj"
MYSQL_DB="sales"

# Output File
OUTPUT_FILE="sales_data.sql"

# MySQL Dump Command
mysqldump -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DB sales_data > $OUTPUT_FILE

echo "Data exported to $OUTPUT_FILE"