from pyspark.sql import SparkSession
from random import randrange

spark = SparkSession.builder.appName("Mindbox_task_n3").getOrCreate()


def get_bridge_table_rows():
    product_id = randrange(1, 21)
    if product_id % 2 == 0:
        response = (product_id, randrange(1, 11))
    else:
        response = (product_id, None)
    return response


categories_rows = [(x + 1, f'Category_{x + 1}') for x in range(10)]
goods_rows = [(x + 1, f'Product_{x + 1}') for x in range(20)]
bridge_table_rows = [get_bridge_table_rows() for x in range(50)]


categories_table = spark.createDataFrame(categories_rows, ['id', 'category_title'])
goods_table = spark.createDataFrame(goods_rows, ['id', 'product_title'])
bridge_table = spark.createDataFrame(bridge_table_rows, ['product_id', 'category_id'])

final_table = (goods_table.join(other=bridge_table,
                                on=goods_table.id == bridge_table.product_id,
                                how='left').join(other=categories_table,
                                                 on=bridge_table.category_id == categories_table.id,
                                                 how='left').select(['product_title', 'category_title']))

final_table.orderBy('category_id', 'product_id', ).show(truncate=True)
