from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("collect").setMaster("local[*]")
    sc = SparkContext(conf = conf)
   
    primesRdd = sc.textFile('in/prime_nums.text')
   
    flatRdd = primesRdd.flatMap(lambda line : line.split('\t')).map(lambda x : int(x))
    end_with_1 = flatRdd.filter(lambda x : x % 10 == 1)
    end_with_3 = flatRdd.filter(lambda x : x % 10 == 3)
    end_with_5 = flatRdd.filter(lambda x : x % 10 == 5)
    end_with_7 = flatRdd.filter(lambda x : x % 10 == 7)
    end_with_9 = flatRdd.filter(lambda x : x % 10 == 9)
    all_nums = flatRdd.count()

    print("Peime that end with")
    print("1   : ", end_with_1.count(), end_with_1.collect())
    print("3   : ", end_with_3.count(), end_with_3.collect())
    print("5   : ", end_with_5.count(), end_with_5.collect())
    print("7   : ", end_with_7.count(), end_with_7.collect())
    print("9   : ", end_with_9.count(), end_with_9.collect())
    print("all : ", all_nums)
    
