from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from demopip.config.ConfigStore import *
from demopip.udfs.UDFs import *

def customers(spark: SparkSession) -> DataFrame:
    return spark.read\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/poojas@prophecy.io/CustomersDatasetInput.csv")
