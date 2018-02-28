import operator;
def findMaxMemberCount(neighbours):
    classVotes = {};
    for x in range (len(neighbours)) :
        response = neighbours[x][-1];
        if response in classVotes:
            classVotes[response]+=1;
        else :
            classVotes[response] = 1;
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True);
    return sortedVotes[0][0];

neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = findMaxMemberCount(neighbors)
print(response)        