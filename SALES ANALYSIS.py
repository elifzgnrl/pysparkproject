# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC sales dataframe
# MAGIC
# MAGIC /FileStore/tables/sales_csv.txt
# MAGIC
# MAGIC /FileStore/tables/menu_csv.txt
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Defined DF
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DateType

schema = StructType([
    StructField("product_id",IntegerType(),True),
    StructField("customer_id",StringType(),True),    
    StructField("order_date",DateType(),True),
    StructField("location",StringType(),True),
    StructField("source_order",StringType(),True)   
])

sales_df = spark.read.format("csv") \
    .schema(schema) \
    .option("header", "true") \
    .load("/FileStore/tables/sales_csv.txt")

sales_df.show()

display(sales_df)

# COMMAND ----------

# DBTITLE 1,deriving year, month, quarter
from pyspark.sql.functions import month, year, quarter

sales_df = sales_df.withColumn("order_year",year(sales_df.order_date))
display(sales_df)

# COMMAND ----------

sales_df = sales_df.withColumn("order_month",month(sales_df.order_date))
sales_df = sales_df.withColumn("order_quarter",quarter(sales_df.order_date))
display(sales_df)

# COMMAND ----------

# DBTITLE 1,menu dataframe
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DateType

schema=StructType([
    StructField("product_id",IntegerType(),True),
    StructField("product_name",StringType(),True),
    StructField("price",StringType(),True)
])

menu_df=spark.read.format("csv").option("inferschema","true").schema(schema).load("/FileStore/tables/menu_csv.txt")
display(menu_df)

# COMMAND ----------

# DBTITLE 1,Total Amount Spent By Each Customer
total_amount_spent = (sales_df.join(menu_df,'product_id').groupBy('customer_id').agg({'price':'sum'}).orderBy('customer_id'))
display(total_amount_spent)

# COMMAND ----------

# DBTITLE 1,Total Amount Spent By Each Food Category
total_amount_spent_by_each_category=(sales_df.join(menu_df,'product_id').groupBy('product_name').agg({'price':'sum'}).orderBy('product_name'))
display(total_amount_spent_by_each_category)

# COMMAND ----------

# DBTITLE 1,Total Amount Of Sales In Each Month
total_amount_of_sales_each_month=(
    sales_df
    .join(menu_df,'product_id')
    .groupBy('order_month')
    .agg({'price':'sum'})
    .orderBy('order_month')
    )
display(total_amount_of_sales_each_month)

# COMMAND ----------

# DBTITLE 1,Yearly Sales
yearly_sales=(sales_df.join(menu_df,'product_id').groupBy('order_year').agg({'price':'sum'}).orderBy('order_year'))
display(yearly_sales)

# COMMAND ----------

# DBTITLE 1,Quaterly Sales
quaterly_sales=(sales_df.join(menu_df,'product_id').groupBy('order_quarter').agg({'price':'sum'}).orderBy('order_quarter'))
display(quaterly_sales)

# COMMAND ----------

# DBTITLE 1,How Many Times Each Product Purchased
from pyspark.sql.functions import count 

coast_df=(sales_df.join(menu_df,'product_id').groupBy('product_id','product_name').agg(count('product_id').alias('total_product')).orderBy('total_product',ascending=False).drop('product_id'))
display(coast_df)

# COMMAND ----------

# DBTITLE 1,Top 3 Ordered Items
from pyspark.sql.functions import count

top_3_ordered_items=(sales_df.join(menu_df,'product_id').groupBy('product_id','product_name').agg(count('product_id').alias('total_product')).orderBy('total_product',ascending=False).drop('product_id').limit(3))
display(top_3_ordered_items)

# COMMAND ----------

# DBTITLE 1,Top Ordered Items
from pyspark.sql.functions import count

top_ordered_items=(sales_df.join(menu_df,'product_id').groupBy('product_id','product_name').agg(count('product_id').alias('total_product')).orderBy('total_product',ascending=False).drop('product_id').limit(1))
display(top_ordered_items)

# COMMAND ----------

# DBTITLE 1,Frequency Of Customer Visited To Restaurant
from pyspark.sql.functions import countDistinct

frequency_df = (
    sales_df
    .filter(sales_df.source_order == 'Restaurant')
    .groupBy('customer_id')
    .agg(countDistinct('order_date').alias('order_frequency'))
    .orderBy('order_frequency', ascending=False)
)

display(frequency_df)


# COMMAND ----------

# DBTITLE 1,Total Sales By Each Country
from pyspark.sql.functions import sum

total_amount_spent_by_each_country = (
    sales_df
    .join(menu_df, 'product_id')
    .groupBy('location')
    .agg(sum('price').alias('total_amount_spent'))
    .orderBy('total_amount_spent')
)

display(total_amount_spent_by_each_country)


# COMMAND ----------

# DBTITLE 1,Total Sales By Order_Source
total_sales_by_order_source=(
    sales_df
    .join(menu_df,'product_id')
    .groupBy('source_order')
    .agg(sum('price').alias('total_sales_by_order_source'))
    .orderBy('total_sales_by_order_source')
)
display(total_sales_by_order_source)