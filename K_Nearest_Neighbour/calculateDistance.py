import math
# This method will calculate distance between two points.
# Formula for calculating distance between two points is 
# sqrt((x1 - x2)^2 + (y1-y2)^2 + (z1-z2)^2 ...)
def calculateDistance(instance1, instance2, length):
    distance = 0;
    for x in range(length):
        distance += pow(instance1[x] - instance2[x], 2);
    return math.sqrt(distance);    

#data1 = [2, 2, 2, 'a']
#data2 = [4, 4, 4, 'b']
#distance = calculateDistance(data1, data2, 3);
#print ("Distance between two points: " + repr(distance));