from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

data = pd.read_csv('..\data\Logs_1.csv', sep=',')

df = spark.createDataFrame(data)
print(df.head())

spark = SparkSession.builder.getOrCreate()
sql_create_database = "Data"
result_create_db = spark.sql(sql_create_database)
sql_create_table = "Moodle"
result_create_table = spark.sql(sql_create_table)
spark.createDataFrame(data)
