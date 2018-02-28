"""
This script will calculate Shannon Entropy.
"""
from math import log
import operator

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # Calculate number of occurances of each class.
    for featVec in dataSet:
        # array[-1] returns last value in the array.
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        
    shannonEnt = 0.0
    """
    1. Calculate probability of number of occurances of a class divided by total number of records.
    2. Negative Summation of probability * log(prob,2)
    """
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 0, 'yes'],
    [1, 1,0, 'yes'],
    [1, 0,0, 'no'],
    [0, 1,0, 'no'],
    [0, 1,1, 'no']
    ,[1, 0,1, 'maybe'] # This is just to create mizing of data to test how entropy changes. Higher the entropy, more the mixmatch/surprises.
    ]
    labels = ['no surfacing','flippers', 'Wings']
    return dataSet, labels


"""
"""
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

"""
This method will use the best feature that can be used to split the data set to create the tree.
1. Calculate the entropy.
2. Iterate through number of features.
    a. find unique values in the feature list.
    b. for every unique value,
        i. split the dataset
        ii. calculate entropy with 
"""
def chooseBestFeatureToSplit(dataSet):
    # Number of features = total number of columns - 1. Last one is class of that record.
    numFeatures = len(dataSet[0]) - 1
    # Calculate Entropy of the data set.
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    # Iterate through number of features in the data set.
    for i in range(numFeatures):
         # Below syntax will retrieve column values. e.g. for main data set above, featList will be 
          # for i = 0 : [1, 1, 1, 0, 0]
          # for i = 1 : [1, 1, 0, 1, 1]
         
        featList = [example[i] for example in dataSet]
          # Find unique value for featList. For i = 0 : uniqueVals = 1 and 0
        uniqueVals = set(featList)
        newEntropy = 0.0
        # Iterate through unique values. 1 and 0 in this case.
        for value in uniqueVals:
               """
                Split the data set. 
                    For i = 0 and value = 0 : splitDataSet(dataset, 0, 0)
                    For i = 0 and value = 1 : splitDataSet(dataset, 0, 1)
                    For i = 1 and value = 0 : splitDataSet(dataset, 1, 0)
                    For i = 1 and value = 1 : splitDataSet(dataset, 1, 1)
               """    
               subDataSet = splitDataSet(dataSet, i, value)
               prob = len(subDataSet)/float(len(dataSet))
               # Calculate new entropy
               newEntropy += prob * calcShannonEnt(subDataSet)
        """ 
            Calculate information gain for each feature. Chose the feature with maximum information gain.
            Calculate base entropy for main data set. then calculate new entropy after splitting the data set and find the information gain.
            Compare information gain for each split and use the feature which give maximum information gain.
        """
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): 
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

"""

"""
def createTree(dataSet,labels):
    # last attribute is the class for each record. so find the last attribute for each record.
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # Find best feature to split.    
    bestFeat = chooseBestFeatureToSplit(dataSet)
    # Find the label for that feature index from label list.
    bestFeatLabel = labels[bestFeat]
    # Create empty map for that best feature.
    myTree = {bestFeatLabel:{}}
    # Delete that label from label list.
    del(labels[bestFeat])
    # Find all the values for that best feature index in the data set.
    featValues = [example[bestFeat] for example in dataSet]
    # Find unique values of that feature.
    uniqueVals = set(featValues)
    for value in uniqueVals:
        # Create sublabels from 1 to n.
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet
              (dataSet, bestFeat, value),subLabels)
    return myTree

def displayTree(mytree) :
    for key in mytree:
        print (key);

mydata, labels = createDataSet();
mytree = createTree(mydata, labels);
displayTree(mytree);
print (mytree);