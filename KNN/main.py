import matplotlib.pyplot as plt
from numpy import *
import operator

# test source
def createDataSource():
    group = array([[1.1, 1.0], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# KNN find the closest k's samples, more types's group is result
def classify(inX, datasource, labels, k):
    datasize = datasource.shape[0]
    diffMat = tile(inX, (datasize, 1)) - datasource
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    f = open(filename)
    arraylists = f.readlines()
    numberoflines = len(arraylists)
    returnMat = zeros((numberoflines, 3))
    classLabelVector = []
    index = 0
    for line in arraylists:
        line = line.strip()
        listfromline = line.split('\t')
        returnMat[index, :] = listfromline[0:3]
        classLabelVector.append(label2num(listfromline[-1]))
        index += 1
    return returnMat, classLabelVector


def label2num(x):
    if x == "largeDoses":
        return 3
    elif x == "didntLike":
        return 1
    else:
        return 2


if __name__ == '__main__':
    datingMat, datingLabel = file2matrix('data/datingTestSet.txt')
    print(datingMat)
    print(datingLabel[0:20])
    group, labels = createDataSource()
    result = classify([0, 0], group, labels, 3)
    fig = plt.figure()
    plt.title("KNN's Data")
    ax = fig.add_subplot(111)
    ax.scatter(datingMat[:, 0], datingMat[:, 1], 15.0 * array(datingLabel), 15 * array(datingLabel))
    plt.show()
    print(result)
