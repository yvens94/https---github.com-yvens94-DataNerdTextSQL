import sqlite3
import csv
# import pandas as pd 


##connect to sqlite

connection = sqlite3.connect("datanerd.db")


##Create a cursot object to insert record, create table, retrieve

cursor =connection.cursor()

# load the data into a Pandas DataFrame

# data=pd.read_csv('cleaned_datanerd.csv')

# # write the data to a sqlite table
# data.to_sql('DATANERD',cursor, if_exists='append', index=False)



# reading data from the CSV file

with open('cleaned_datanerd.csv', encoding='utf-8') as f:
    reader= csv.reader(f)
    data=list(reader)


##create the table
#drop it if it exists
cursor.execute("DROP TABLE IF EXISTS DATANERD")

table_info ="""

Create table DATANERD(
    
    company_name       varchar(225),
    location           varchar(225),
    job_platform       varchar(225),
    contract_type      varchar(225),
    work_from_home     varchar(225),
    salary             float64,
    skills             varchar(225),
    position_level     varchar(225), 
    job_role           varchar(225),
    industry           varchar(225));

    
""" 


cursor.execute(table_info)


#insert data into the table

for row in data:
    cursor.execute("INSERT INTO DATANERD (company_name, location, job_platform, contract_type, work_from_home, salary, skills, position_level , job_role, industry) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                   (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


# display record
    
print("The first tree executed records are")

data_verify = cursor.execute('''select * from DATANERD limit 3 ''').fetchall()

for row in data_verify:
    print(row)



  
  
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 0 TO company_name');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 1 TO location');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 2 TO job_platform');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 3 TO contract_type');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 4 TO work_from_home');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 5 TO salary');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 6 TO skills');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 7 TO job_role');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 8 TO industry');
# cursor.execute('ALTER  TABLE DATANERD RENAME COLUMN 9 TO state');


# # Retrieve the first row containing column names
# cursor.execute("SELECT * FROM DATANERD LIMIT 1")
# first_row = cursor.fetchone()

# # Extract column names from the first row
# column_names = [str(name) for name in first_row]

# # Construct SQL query to rename columns
# sql_query = "PRAGMA foreign_keys=off; BEGIN TRANSACTION; CREATE TABLE temp_table AS SELECT * FROM DATANERD; DROP TABLE DATANERD; CREATE TABLE DATANERD ({}); INSERT INTO DATANERD SELECT * FROM temp_table; DROP TABLE temp_table; COMMIT; PRAGMA foreign_keys=on;".format(",".join(column_names))

# # Execute the SQL query to rename columns
# cursor.executescript(sql_query)
   



##close the connection
    
connection.commit()
connection.close



