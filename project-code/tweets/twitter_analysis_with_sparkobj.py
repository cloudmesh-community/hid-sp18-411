from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF
from pyspark.ml.classification import LogisticRegression
import pyspark as ps
import pandas
import matplotlib.pyplot as plt


def start_spark_sentiment_analysis(hashtag):
    sc = ps.SparkContext('local[*]')
    sqlContext = ps.SQLContext(sc)

    tokenizer = Tokenizer(inputCol="Tweets", outputCol="words")
    remover = StopWordsRemover(inputCol="words", outputCol="base_words")
    hashingTF = HashingTF(numFeatures=10000, inputCol="base_words", outputCol="features")
    lr = LogisticRegression(featuresCol="features", labelCol="Sentiment", elasticNetParam=0.8, regParam=0.001,
                            family="multinomial")

    pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, lr])

    partsDF = pandas.read_csv("./usr/local/static/tweet_sentiment.csv")
    datasize = partsDF.shape[0]
    trainSet = partsDF.sample(frac=0.5, replace=False)

    trainSet = sqlContext.createDataFrame(trainSet)
    partsDF = sqlContext.createDataFrame(partsDF)
    lrModel = pipeline.fit(trainSet)

    lrResult = lrModel.transform(partsDF)

    avg = round(lrResult.where('Sentiment == prediction').count() / datasize, 2)
    neutral = round(lrResult.where('prediction==0').count(), 2)
    supportive = round(lrResult.where('prediction==1').count(), 2)
    Against = round(lrResult.where('prediction==2').count(), 2)

    print("\n\n\n\n\n|----------------------##----------------------|")
    print("Accuracy=\t", avg, "%")
    print("Neutral=\t", neutral, "%")
    print("Supportive=\t", supportive, "%")
    print("Against=\t", Against, "%")

    frequencies = [int(supportive), int(neutral), int(Against)]

    freq_series = pandas.Series.from_array(frequencies)

    x_labels = ['Positive Tweets', 'Neutral Tweets', 'Negative Tweets']
    title = 'Sentimental Analysis on Twitter Data ' + hashtag
    # Plot the figure.
    plt.figure(figsize=(14, 10))
    ax = freq_series.plot(kind='bar', color="green")
    ax.set_title(title, fontsize=24, weight='bold')
    ax.set_xlabel('Sentiment', fontsize=18, weight='bold')
    ax.set_ylabel('Frequency', fontsize=18, weight='bold')
    ax.set_xticklabels(x_labels, fontsize=18, weight='bold', rotation=0)

    plt.savefig("./usr/local/static/result.png")
