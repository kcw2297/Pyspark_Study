from pyspark import SparkConf, SparkContext

sparkConfig = SparkConf().setAppName("WordCountLocal").setMaster("local")
sparkContext = SparkContext(conf=sparkConfig)

text_file = sparkContext.textFile("text.txt") # text 파일의 각줄은 RDD 객체의 요소로 변환됩니다.

# Map 함수 적용
mapped_values = text_file.\
            flatMap(lambda line: line.split(" ")). \
            map(lambda word: (word, 1))

# Reduce 함수 적용
word_counts = mapped_values.reduceByKey(lambda a, b: a + b)

# 저장합니다.
word_counts.saveAsTextFile("output_text")

for word, count in word_counts.collect():
    print(f"{word}: {count}")

sparkContext.stop()
