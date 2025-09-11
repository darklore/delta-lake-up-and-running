# %%
from util import create_spark_session

spark = create_spark_session()

data = spark.range(0, 100)
data.write.format("parquet").mode("overwrite").save(
    "./book/chapter02/parquetData",
)
print(f"The number of partitions is: {data.rdd.getNumPartitions()}")

# %%
