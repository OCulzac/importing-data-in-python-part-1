""" Pandas for more complex querying
Here, you'll become more familiar with the pandas function read_sql_query() by using it to execute a more complex query: a SELECT statement followed by both a WHERE clause AND an ORDER BY clause.

You'll build a DataFrame that contains the rows of the Employee table for which the EmployeeId is greater than or equal to 6 and you'll order these entries by BirthDate. """

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    'SELECT * FROM Employee WHERE EmployeeID >= 6 ORDER BY BirthDate', engine)
    'SELECT * FROM Employee WHERE EmployeeID >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())
