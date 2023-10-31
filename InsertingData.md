# Inserting Data into Databases.
### ***Key tasks:***
* Connected to an RDS instance via MySQL client to run SQL commands.
* Created a new database and tables to store sample country and city info.
* Used SHOW DATABASES and SHOW TABLES to verify creation.
* Altered a table column using ALTER TABLE to fix a typo.
* Dropped the sample tables and database with DROP TABLE and DROP DATABASE
* Ran queries at each step to check database and table statuses

### ***What I learned***:

1. Important to have a process to spin up and tear down test databases/tables.
1. Value of using SHOW, DESCRIBE, and other SQL commands to inspect objects.
1. How to modify tables on the fly without needing to start over.
1. Be cautious dropping databases and tables as data loss can occur.
1. Features like foreign keys and constraints add more complexity.


# Lab 269: Insert, Update, and Delete Data in a Database
### ***Key tasks:***
* Connected to an RDS MySQL instance and accessed a sample database.
* Inserted new rows into a table using the INSERT statement.
* Updated existing rows in a table using the UPDATE statement.
* Deleted rows from a table using the DELETE statement.
* Imported data into tables from an SQL script file.
* Verified results after each operation by querying the tables.

### ***What I learned:***
1. How to add, modify and remove data in SQL tables.
1. The importance of WHERE clauses to target specific rows.
1. Caution needed with UPDATE and DELETE to avoid unintended changes.
1. Benefits of importing data via SQL scripts vs manual INSERTs.
1. Querying tables to validate changes occurred as expected.