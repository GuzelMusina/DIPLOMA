from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

data = pd.read_csv('..\data\Logs_1.csv', sep=',')

df = spark.createDataFrame(data)
print(df.head())