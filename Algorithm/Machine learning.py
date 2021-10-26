# KNN : K -Nearest Neighbor
import numpy as np
trainData = np.array([[23, 8], [26, 9], [21, 7], [23, 9],
                     [19, 11], [18, 9], [20, 10]])
labels = ['fish', 'fish', 'fish', 'fish', 'frog', 'frog', 'frog']
K = 3
testData = [20, 11]


def SolveStance(tData, Labels, testData):
    rData = []
    i = 0
    for DotValue in tData:
        ed = np.sqrt((DotValue[0]-testData[0])**2+(DotValue[1]-testData[1])**2)
        rData.append([ed, labels[i]])
        i += 1
    return rData


print(SolveStance(trainData, labels, testData))
# [[4.242640687119285, 'fish'], [6.324555320336759, 'fish'], [4.123105625617661, 'fish'], [3.605551275463989, 'fish'], [1.0, 'frog'], [2.8284271247461903, 'frog'], [1.0, 'frog']]


def SortSolve(rData):
    return sorted(rData)


print(SortSolve(SolveStance(trainData, labels, testData)))
# [[1.0, 'frog'], [1.0, 'frog'], [2.8284271247461903, 'frog'], [3.605551275463989, 'fish'], [4.123105625617661, 'fish'], [4.242640687119285, 'fish'], [6.324555320336759, 'fish']]


def GetKValues(sData, k):
    kData = sData[:k]
    print(kData)
    # [[1.0, 'frog'], [1.0, 'frog'], [2.8284271247461903, 'frog']]
    ClassCount = {}
    for item in kData:
        ClassCount[item[1]] = ClassCount.get(item[1], 0)+1
        # dict.get(key, default=None)
    rEnds = sorted(ClassCount.items())
    # dict.items() return key,values
    print(ClassCount, rEnds)  # {'frog': 3},[('frog', 3)]
    return rEnds[-1:]


StanceData = SolveStance(trainData, labels, testData)
ss = SortSolve(StanceData)
sKind, rate = GetKValues(ss, K)[0]
print('class:%s,accuracy:%d' % (sKind, 100*(rate/K)))


# NBC P(A|B)=P(AB)/P(B)=P(B|A)P(A)/P(B)
# Native Bayes Classifier
Datas = np.array([['A', 24, 'female', 'doctor', 1], ['A', 24, 'male', 'worker', 0], ['A', 65, 'male', 'farmer', 0], ['A', 65, 'female', 'worker', 0], ['A', 24, 'female', 'officer', 1], ['B', 25, 'male', 'government', 1], ['B', 15, 'female', 'student', 0], ['B', 16, 'male', 'student', 0], ['C', 34, 'female', 'teacher', 0], ['C', 35, 'male', 'worker', 0], ['C', 45, 'male', 'farmer', 0]])
Test = np.array(['A', 24, 'female', 'teacher'])


def NBC(trainData, labels, testData):
    C = {}
    for label in labels:
        if C.get(label) != None:
            C[label] += 1
        else:
            C[label] = 1
    print('The classification:', C)
    Clen = len(labels)
    Ptc = {}
    for k, c in C.items():
        c = int(c)
        Atcount = {}
        for records in trainData:
            if records[-1] == k:
                i = 0
                length = len(testData)
                while i < length:
                    if testData[i] == records[i]:
                        if Atcount.get(testData[i]) != None:
                            Atcount[testData[i]] += i
                        else:
                            Atcount[testData[i]] = 1
                    i += 1
        Pt = np.array(list(Atcount.values()))/c
        print(k,Atcount)
        v = 1
        for p in Pt:
            if p != 0:
                v *= p
        Ptc[k] = (c/Clen)*v
        print(Ptc)
        return max(Ptc, key=Ptc.get)
market = NBC(Datas, Datas[:, -1], Test)
print('data:', Test, 'classification:', market)
