# Import libraries required for connecting to mysql
import mysql.connector

# Import libraries required for connecting to DB2 or PostgreSql
import psycopg2

# Connect to MySQL
connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='sales')

# Connect to DB2 or PostgreSql
dsn_hostname = '127.0.0.1'
dsn_user='postgres'        # e.g. "abc12345"
dsn_pwd =''      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port ="5432"                # e.g. "50000" 
dsn_database ="postgres"           # i.e. "BLUDB"

conn = psycopg2.connect(
   database=dsn_database, 
   user=dsn_user,
   password=dsn_pwd,
   host=dsn_hostname, 
   port= dsn_port
)

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
    try:
        cursor = conn.cursor()
        query = "SELECT MAX(rowid) FROM sales_data"
        cursor.execute(query)
        result = cursor.fetchone()
        last_rowid = result[0] if result[0] is not None else 0
        return last_rowid
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# Lists out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records returns a list of all records that have a rowid greater than 
# the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(row_id):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM sales_data WHERE rowid > {row_id}"
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()	

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Inserts the additional records from MySQL into PostgreSql data warehouse.
# The function insert_records inserts all the records passed to it into the sales_data table in PostgreSql.

def insert_records(records):
    try:
        cursor = conn.cursor()
        for record in records:
            query = f"INSERT INTO sales_data (rowid, product_id, customer_id, quantity) VALUES {record}"
            cursor.execute(query)
        conn.commit()
        print("Records inserted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
connection.close()

# disconnect from DB2 or PostgreSql data warehouse 
conn.close()

# End of program