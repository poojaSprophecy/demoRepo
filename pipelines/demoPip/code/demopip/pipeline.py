from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demopip.config.ConfigStore import *
from demopip.udfs.UDFs import *
from prophecy.utils import *
from demopip.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_customers = customers(spark)
    df_Subgraph_1 = Subgraph_1(spark, df_customers, df_orders)
    df_Filter_1 = Filter_1(spark, df_Subgraph_1)
    customer_orders(spark, df_Filter_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/demoPip")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/demoPip")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
