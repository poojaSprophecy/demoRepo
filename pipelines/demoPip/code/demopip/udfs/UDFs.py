from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.transpiler import ABIUtil, BigDecimal, ScalaUtil, getContentAsStream, call_spark_fcn, substring_scala
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
    ScalaUtil.initializeUDFs(spark)

def addtenGenerator():
    n = 10

    @udf(returnType = IntegerType())
    def func(value: int):
        return n + value

    return func

addten = addtenGenerator()
