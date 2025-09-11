# %%
from util import create_spark_session

spark = create_spark_session()

data = spark.range(0, 100)
data.write.format("delta").mode("overwrite").save("./book/chapter02/deltaData")
print(f"The number of partitions is: {data.rdd.getNumPartitions()}")
