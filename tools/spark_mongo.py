# coding:utf-8
__author__ = 'dangsh'
# create by 张霄港(dangsh) 2018 4 16
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.rdd import  StorageLevel

spark = SparkSession.builder.appName('hy88_company').getOrCreate()
# sc = SparkContext(spark.sparkContext)
sc = spark.sparkContext

rdd = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://192.168.14.90/final_field.hy88").load().rdd
rdd.persist(StorageLevel(True, True, False, False))
rdd = rdd.map(lambda x:(x.com_url,)).filter(lambda x:x != None)
rdd = rdd.distinct()

spark.createDataFrame(rdd, ['_id']).write.format("com.mongodb.spark.sql.DefaultSource").mode("ignore").option("uri", "mongodb://192.168.14.90/hy88.spark_company_url").save()