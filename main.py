import pymssql
import pandas as pd

mssql_dict = dict()

mssql_dict["server"] = "capdstest.database.windows.net"
mssql_dict["database"] = "DSTest"
mssql_dict["user"] = "candidate"
mssql_dict["pwd"] = "P)pE8J%XYVdv)4k_K%8]v@f)"

conn = pymssql.connect(mssql_dict["server"], mssql_dict["user"],
                       mssql_dict["pwd"], mssql_dict["database"])

sqlstr = '''
select UserId from dbo.Activity
'''

with conn.cursor() as cursor:
    cursor.execute(sqlstr)
    data = cursor.fetchall()
    column_names = [item[0] for item in cursor.description]
    df = pd.DataFrame(list(data), columns=column_names)

print(df.head())
