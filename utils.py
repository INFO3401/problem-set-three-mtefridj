import pandas as pd
import matplotlib.pyplot as plt

def helloWorld():
    print("hello world")
def localandCleanData(filename):
    credit_db = pd.read_csv(filename)
    fixed_db = credit_db.fillna(0)
    return fixed_db
def computePDF(feat, dataset):
    pdf_series = dataset[feat]
    pdf = pdf_series.plot.kde()
    plt.show()
def visualDistribution(feat, dataset):
    dataset.hist(column=feat)
    plt.xlabel('Not logged')
    plt.show()
def viewLogDistribution(feat, dataset):
    min_point = dataset[feat].min()
    max_point = dataset[feat].max()
    min_point = round(min_point)
    max_point = round(max_point)
    bin_size = (max_point - min_point) / 3
    if bin_size < 1:
        bin_size = 3
    if bin_size > 100:
        bin_size = 20
    dataset.hist(column=feat, bins= int(bin_size))
    plt.xlabel('Log')
    plt.yscale('log')
    plt.show()
def computeProbability(feature, bin, data):
    count = 0
    for i,datapoint in data.iterrows():
        if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
            count += 1
    totalData = len(data)
    prob = count / totalData
    return prob
def computeDefaultRisk(feature, bin, data, target):
    count = 0
    for i,datapoint in data.iterrows():
        if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:
            if datapoint[target] == 1:
                count += 1
    totalData = len(data)
    comb_prob = count / totalData
    single_prob = computeProbability(feature,bin,data)
    if single_prob == 0:
        single_prob = .000001
    total_prob = comb_prob/ single_prob
    return total_prob