# Normalization
# Min-Max
# x'=(x-minA)/(maxA-minA)
import hashlib
import numpy as np
import matplotlib.pyplot as plt
Data = np.array([[0.2, 0.9, 29], [0.9, 0.1, 100], [0.5, 0.5, 30]])


def Min_Max(data):
    min = 0
    max = 1
    C = data[:, 2]  # 29,100,30
    min = np.min(C)  # 29
    max = np.max(C)  # 100
    for one in data:
        one[2] = (one[2]-min)/(max-min)
    print('transform matrix:\n', data)
    return data


def ShowData(Data, ShowD1):
    length = len(Data)
    X = np.ones(Data.shape[0])
    plt.figure('Normalization')
    plt.subplot(121)  # plt.subplot(nrows, ncols, index)
    for i in range(length):
        plt.scatter(X*(i+1), Data[:, i])
    plt.subplot(122)
    for i in range(length):
        plt.scatter(X*(i+1), ShowD1[:, i])
    plt.show()


ShowData(Data, Min_Max(Data.copy()))
# -------------------------------------------------
# Z-score standardization
# z=(x-x')/σ
# x'=1/n*∑x
# σ=（1/n*∑(xi-x')(xi-x'))0.5
Data = np.array([[0.2, 0.9, 29], [0.9, 0.1, 100], [0.5, 0.5, 30]])


def ZScore(data):
    x_mean = np.mean(data[:, 2])
    length = len(data[:, 2])
    vari = np.sqrt((np.sum((data[:, 2]-x_mean)**2))/length)
    print('vari:\n', vari)
    data[:, 2] = (data[:, 2]-x_mean)/vari
    print('Z-Score standardization matrix:\n', data)
    return data


def ShowData(Data, ShowD1):
    length = len(Data)
    X = np.ones(Data.shape[0])
    plt.figure(1)
    plt.subplot(121)
    for i in range(length):
        plt.scatter(X*(i+1), Data[:, i])
    plt.subplot(122)
    for i in range(length):
        plt.scatter(X*(i+1), ShowD1[:, i])
    plt.show()


ShowData(Data, ZScore(Data.copy()))
# --------------------------------------------------------
# Decimal scaling
# x'=x/10k


def DecimalS(data):
    C = np.abs(data[:, 2])
    max = int(np.sort(C)[-1])
    k = len(str(max))
    print('the absolute value of the maximum number of digits:\n', k)
    data[:, 2] = data[:, 2]/(10**k)
    print('Decimal scaling standardization matrix:\n', data)
    return data


def ShowData(Data, ShowD1):
    length = len(Data)
    X = np.ones(Data.shape[0])
    plt.figure(1)
    plt.subplot(121)
    for i in range(length):
        plt.scatter(X*(i+1), Data[:, i])
    plt.subplot(122)
    for i in range(length):
        plt.scatter(X*(i+1), ShowD1[:, i])
    plt.show()


ShowData(Data, DecimalS(Data.copy()))
# --------------------------------------------------------
# Hash
records = [[1, 5], [8, 29], [15, 20], [17, 21], [31, 60]]
SAddress1 = {'192.168.1.1': 5}
SAddress2 = {'192.168.1.2': 10}
SAddress3 = {'192.168.1.3': 15}
SAddress4 = {'192.168.1.4': 20}
n = 20
for one in records:
    if one[0] % n <= SAddress1['192.168.1.1']:
        SAddress1[one[0]] = one[1]
    elif one[0] % n <= SAddress2['192.168.1.2']:
        SAddress2[one[0]] = one[1]
    elif one[0] % n <= SAddress3['192.168.1.3']:
        SAddress3[one[0]] = one[1]
    elif one[0] % n <= SAddress4['192.168.1.4']:
        SAddress4[one[0]] = one[1]
print(SAddress1)
print(SAddress2)
print(SAddress3)
print(SAddress4)
# --------------------------------------------------------
# consistent hashing


class CHash(object):
    def __init__(self, nodes=None, v_num=2):
        self._v_num = v_num
        self._vNode_IP = {}
        self._vNodeAdd = []
        for node in nodes:
            self.addNode(node)
        print('\nResult of virtual node hash values in ascending order:\n', self._vNodeAdd)

    def addNode(self, node):
        for i in range(self._v_num):
            vNodeStr = '%s%s' % (node, i)
            key = self._gen_key(vNodeStr)
            print('virtual node string', vNodeStr, 'hash value:', key)
            self._vNode_IP[key] = node
            self._vNodeAdd.append(key)
            self._vNodeAdd.sort()

    def delNode(self, node):
        for i in range(self._v_num):
            vNodeStr = '%s%s' % (node, i)
            key = self._gen_key(vNodeStr)
            del self._vNode_IP[key]
            self._vNodeAdd.remove(key)

    def dataNode(self, data):
        if self._vNodeAdd:
            key = self._gen_key(data)
            for node_key in self._vNodeAdd:
                if key <= node_key:
                    return self._vNode_IP[node_key]
            return self._vNodeAdd[self._vNodeAdd[0]]
        else:
            return None

    @staticmethod
    def _gen_key(key_str):
        hashValue = hashlib.sha1(key_str.encode('utf-8')).hexdigest()
        return hashValue


C_H = CHash(['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4'])
data = ['BIG', 'THREE', 'CAT']
print('Normal address:')
print(data[0]+'IP address:', C_H.dataNode(data[0]))
print(data[1]+'IP address:', C_H.dataNode(data[1]))
print(data[2]+'IP address:', C_H.dataNode(data[2]))
print('Node out of distributed system:')
C_H.delNode('192.168.1.2')
print(data[0]+' IP address:', C_H.dataNode(data[0]))
print(data[1]+' IP address:', C_H.dataNode(data[1]))
print(data[2]+' IP address:', C_H.dataNode(data[2]))

# --------------------------------------------------------
# Euclidean Algorithm


def gcd(a, b):
    if a % b == 0:
        return b
    c = gcd(b, a % b)
    return c


print(gcd(100, 13))
# --------------------------------------------------------
# Extended Euclidean Algorithm


def e_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = e_gcd(b, a % b)
        x, y = y, (x-(a//b)*y)
        return x, y, q


x, y, q = e_gcd(50, 20)
print('x=%d,y=%d,MOD=%d' % (x, y, q))
# --------------------------------------------------------
# RSA
# m*x mod n = (m mod n)*(x mod n) mod n
# print(2014**2000)
def Montgomery(a,b,c):
    if b==1:
        print('MOD %d,POW %d,Exponential %d'%(a%c,a,b))
        return a%c
    r=Montgomery(a,b>>1,c)%c
    if b%2==0:
        print('MOD %d,POW %d,Exponential %d'%((r*r)%c,a,b))
        return (r*r)%c
    else:
        print('MOD %d,POW %d,Exponential %d'%((a*(r*r))%c,a,b))
        return (a*(r*r))%c
a=2
b=9
c=10
v=Montgomery(a,b,c)
print(v)
