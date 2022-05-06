import pymssql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mssql_dict = dict()

mssql_dict["server"] = "capdstest.database.windows.net"
mssql_dict["database"] = "DSTest"
mssql_dict["user"] = "candidate"
mssql_dict["pwd"] = "P)pE8J%XYVdv)4k_K%8]v@f)"

# Connect to SQL
conn = pymssql.connect(mssql_dict["server"], mssql_dict["user"],
                       mssql_dict["pwd"], mssql_dict["database"])


def generate_dataframe(sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
        column_names = [item[0] for item in cursor.description]
        df = pd.DataFrame(list(data), columns=column_names)
    return df


def plot_avg_revenue(sql):
    df = generate_dataframe(sql)
    df = df.pivot(index="YearQuarter",
                  columns="DayName",
                  values="AvgRevenue")
    plt.cla()
    Time = df.index

    plt.figure(figsize=(7, 10))
    ax1 = plt.subplot(711)
    plt.plot(Time, df.Monday, label='Monday')
    plt.legend(loc='upper right')
    plt.tick_params('x', labelbottom=False)

    plt.subplot(712, sharex=ax1, sharey=ax1)
    plt.plot(Time, df.Tuesday, label='Tuesday')
    plt.legend(loc='upper right')
    plt.tick_params(axis='x', labelbottom=False)

    plt.subplot(713, sharex=ax1, sharey=ax1)
    plt.plot(Time, df.Wednesday, label='Wednesday')
    plt.legend(loc='upper right')
    plt.tick_params('x', labelbottom=False)

    plt.subplot(714, sharex=ax1, sharey=ax1)
    plt.plot(Time, df.Thursday, label='Thursday')
    plt.legend(loc='upper right')
    plt.tick_params('x', labelbottom=False)

    plt.subplot(715, sharex=ax1, sharey=ax1)
    plt.plot(Time, df.Friday, label='Friday')
    plt.legend(loc='upper right')
    plt.tick_params('x', labelbottom=False)

    plt.subplot(716, sharex=ax1, sharey=ax1)
    plt.plot(Time, df.Saturday, label='Saturday')
    plt.legend(loc='upper right')
    plt.tick_params('x', labelbottom=False)

    plt.subplot(717, sharex=ax1, sharey=ax1)
    plt.plot(Time, df.Sunday, label='Sunday')
    plt.legend(loc='upper right')
    plt.tick_params('x', labelbottom=True)

    plt.xlim(0, 5.0)
    plt.show()
    plt.savefig('AverageRevenue')


sql_avg_renvenue = '''
                select
                    'Y' + CAST(YEAR(Date) AS varchar) + 'Q'
                        + CAST(DATEPART(quarter, Date) AS varchar) AS YearQuarter,
                    CAST(DATENAME(weekday, Date) AS varchar) AS DayName,
                    ROUND(AVG(CAST(Revenue AS float)), 2) AS AvgRevenue
                from dbo.Activity
                group by
                    'Y' + CAST(YEAR(Date) AS varchar) + 'Q'
                        + CAST(DATEPART(quarter, Date) AS varchar),
                    CAST(DATENAME(weekday, Date) AS varchar)
                order by
                    'Y' + CAST(YEAR(Date) AS varchar) + 'Q'
                        + CAST(DATEPART(quarter, Date) AS varchar)
                '''


plot_avg_revenue(sql_avg_renvenue)
