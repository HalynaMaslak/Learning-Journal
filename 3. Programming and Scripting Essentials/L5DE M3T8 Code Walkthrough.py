# Initialize PySpark
APP_NAME = "Week 2 - Key Value Spark Problems"
import re
def getKBDOC(stringy):
    return re.search(r'KBDOC-[0-9]*',stringy).group()


# If there is no SparkSession, create the environment
try:
  sc and spark
except NameError as e:
  import findspark
  findspark.init()
  import pyspark
  import pyspark.sql
    
  sc = pyspark.SparkContext()
  spark = pyspark.sql.SparkSession(sc).builder.appName(APP_NAME).getOrCreate()



print("PySpark initiated...")

#Sort data by address and attach via tuple
input = "00210 43.005 -710\n0211 43.0058 -72\n00233 44 -73"
print(input)
value = input.split("\n")
print(value)
rdd = sc.parallelize(value)
output = rdd.map(lambda line: (line.split(' ')[0], (line.split(' ')[1], line.split(' ')[2])))
print(output.collect())
#split data
order_data = "00001 sku010:sku933:sku022\n00002 sku912:sku331"
splited = order_data.split("\n")
 
rdd1 = sc.parallelize(splited)
#Split data with colons
rdd2 = rdd1.map(lambda line: (line.split(' ')[0], line.split(' ')[1].split(':')))
print(rdd2.collect())
#Flat map value data so that each set of data has its own line
rdd3 = rdd2.flatMapValues(lambda a: a)
print(rdd3.collect())
#An alternative method
seperate = rdd1.map(lambda lines: lines.split(' '))
flatvaluemap = seperate.flatMapValues(lambda value: value.split(':'))
print(flatvaluemap.collect())
#Data for this task
weblogs = "32.54.32.111 - 93332 \"GET /KBDOC-00157.html HTTP/1.0\"\n132.54.32.212 - 93332 \"GET /theme.css  HTTP/1.0\"\n132.54.32.212 - 25254 \"GET /KBDOC-00230.html  HTTP/1.0\""
kblist = "KBDOC-00157:Parallel Programming\nKBDOC-00230:Distributed Systems\nKBDOC-00221:HCI"
#Put data into an RDD
data = weblogs.split("\n")
Task3Rdd = sc.parallelize(data)
#Filter data so that only KBDOCs are present
rdd5 = Task3Rdd.filter(lambda line: 'KBDOC' in line.split(' ')[4])
#format the data
FormattedRdd = rdd5.map(lambda line: (getKBDOC(line.split(' ')[4]), line.split(' ')[2]))
print(FormattedRdd.collect())
#Get the new data into an RDD
Task3Rdd2 = sc.parallelize(kblist.split("\n"))
FormattedT32 = Task3Rdd2.map(lambda line: (line.split(':')[0],line.split(':')[1]))
print(FormattedT32.collect())
#Join the data
Result = FormattedRdd.join(FormattedT32)
print(Result.collect())
#Format the data again
FormatedResult = Result.map(lambda lines: (lines[1][0], lines[1][1]))
print(FormatedResult.collect())

#Group the data
group_map = FormatedResult.groupByKey().mapValues(list).collect()
group_col = group_map
print(group_col)