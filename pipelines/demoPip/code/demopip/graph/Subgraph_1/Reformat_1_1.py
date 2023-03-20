from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from demopip.config.ConfigStore import *
from demopip.udfs.UDFs import *

def Reformat_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("first_name"), 
        col("last_name"), 
        col("phone"), 
        col("email"), 
        col("country_code"), 
        col("account_open_date"), 
        col("account_flags"), 
        col("customer_id"), 
        col("order_status"), 
        col("order_category"), 
        col("full_name"), 
        addten(lit(2)).alias("test_col")
    )
