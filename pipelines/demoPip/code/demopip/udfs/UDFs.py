from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)
n = 10

def registerUDFs(spark: SparkSession):
    spark.udf.register("addten", addten)

@udf(returnType = IntegerType())
def addten(value: int):
    return n + value
