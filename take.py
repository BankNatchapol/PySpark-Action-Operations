from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("collect").setMaster("local[*]")
    sc = SparkContext(conf = conf)
   
    primesRdd = sc.textFile('in/prime_nums.text')
   
    flatRdd = primesRdd.flatMap(lambda line : line.split('\t'))
    take5 = flatRdd.take(5)
    
    print("Take 5 : ", take5)
    
