import random
import csv;
# This method will convert dataset into training data set and test data set.
# fileName: fully qualified file name.
# split: split ratio. e.g. 0.66
# trainingSet: Training set to be populated.
# testSet: Test set to be populated.
def loadDataSet(fileName, split, trainingSet=[], testSet=[]):
    with open(fileName) as csvFile:
        lines = csv.reader(csvFile);
        dataset = list(lines);
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y]);
            if random.random() < split:
                trainingSet.append(dataset[x]);
            else:
                testSet.append(dataset[x]);


trainingSet=[]
testSet=[]
loadDataSet('iris_data.csv', 0.66, trainingSet, testSet)
print ('Train: ' + repr(len(trainingSet)))
print ('Test: ' + repr(len(testSet)))