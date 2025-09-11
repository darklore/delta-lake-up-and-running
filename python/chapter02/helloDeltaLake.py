# %%
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

# Create a builder with the Delta extensions
builder = (
    SparkSession.builder.appName("MyApp")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)

# Create a Spark instance with the builder
# As a result, we now can read and write Delta files
spark = configure_spark_with_delta_pip(builder).getOrCreate()
print(f"Hello, Spark version: {spark.version}")

# Create a range, and save it in Delta format to ensure
# that our Delta extensions are indeed working
df = spark.range(0, 10)
df.write.format("delta").mode("overwrite").save(
    "./book/chapter02/helloDeltaLake",
)

# %%
