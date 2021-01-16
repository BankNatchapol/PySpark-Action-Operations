from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("collect").setMaster("local[*]")
    sc = SparkContext(conf = conf)
   
    primesRdd = sc.textFile('in/prime_nums.text')
   
    flatRdd = primesRdd.flatMap(lambda line : line.split('\t'))
    flatFlatRdd = flatRdd.flatMap(lambda text : list(text))
    count = flatFlatRdd.countByValue()
    
    print("Count : ", dict(count))
    
