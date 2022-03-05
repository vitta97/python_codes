## A function which is used to create the nested dictionaries from the data

## Approach 1

# when it comes to UDF in pyspark our parallelisum will comes to bottle neck of the given data
def dict_separator(x):
    x = re.findall("\'(.*?)\'", str(x))
    final_str = ""
    key, value = [], []
    for i in range(0, len(x) - 1, 2):
        key.append(x[i])
    for i in range(1, len(x), 2):
        value.append(x[i])
    for i, j in zip(key, value):
        final_str += "'" + i + "'" + ":" + "'" + j + "'" + "||"
    return final_str[:-2]

udf_df = udf(dict_separator, ArrayType(StringType()))
lead_1_entity_temp_rdd.select(col("agent_name"), \
    udf_df(col("agent_name")).alias("cusomter_name") )


## 2nd approach

## when we go with RDD and map functions we can control our parallelisum of the data in pyspark

#This is the function which is used to generated nested dictionaries from the data
def dict_separator(x):
    x = re.findall("\'(.*?)\'", str(x))
    final_str = ""
    key, value = [], []
    for i in range(0, len(x) - 1, 2):
        key.append(x[i])
    for i in range(1, len(x), 2):
        value.append(x[i])
    for i, j in zip(key, value):
        final_str += "'" + i + "'" + ":" + "'" + j + "'" + "||"
    return final_str[:-2]

lead_1_entity_temp_rdd = lead_1_entity.select("ownership_entity").rdd
lead_1_entity_temp_new = lead_1_entity_temp_rdd.map(lambda x: (dict_separator(x),))
my_temp = lead_1_entity_temp_new.toDF(["ownership_entity"])

## 3rd approach

## Collect list and collect set function can be used to acheive the parallellsium in pyspark

lead_1_entity_temp_rdd = lead_1_entity_temp_rdd.groupby('loan_id').agg(collect_list(df["agent_name"]).alias('customer_name'))
