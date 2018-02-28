import operator;
import calculateDistance;

#Calculate distance between test instance and each instance of training set.
# Sort it in ascending order.
def getNeighbours(trainingSet, testInstance, k):
    distances = [];
    length = len(testInstance) - 1;
    for x in range (len(trainingSet)):
        dist = calculateDistance.calculateDistance(testInstance, trainingSet[x], length);
        distances.append((trainingSet[x], dist));
    distances.sort(key=operator.itemgetter(1))
    neighbours = [];
    for x in range(k):
        neighbours.append(distances[x][0]);
    return neighbours;

trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
testInstance = [5, 5, 5]
k = 1
neighbours = getNeighbours(trainSet, testInstance, 1)
print(neighbours)