from pyspark import SparkContext, SparkConf

def minimum(x, y):
    if x < y: 
        return x 
    else:
        return y

def maximum(x, y):
    if x > y: 
        return x 
    else: 
        return y

def total(x, y):
    return x + y

if __name__ == "__main__":
    conf = SparkConf().setAppName("reduce").setMaster("local[*]")
    sc = SparkContext(conf = conf)
   
    primesRdd = sc.textFile('in/prime_nums.text')
   
    flatRdd = primesRdd.flatMap(lambda line : line.split('\t')).map(lambda x : int(x))
    
    minimum = flatRdd.reduce(minimum)
    maximum = flatRdd.reduce(maximum)
    total = flatRdd.reduce(total)
   
    print("Minimum : ", minimum)
    print("Maximum : ", maximum)
    print("Total   : ", total)
    
