# oil
# from _typeshed import Self


def oil(n, distance):
    i = 0
    count = 0
    for one in distance:
        count += one
        if count > n:
            print('%dkm start fuel filling' % (one))
            count = one
            i += 1
    return i


n = 300
dis = [150, 180, 120, 100, 280, 160, 50, 60, 20, 140, 130]  # dis<300
num = oil(n, dis)
print('the minimum filling times:%d' % (num))
# --------------------------------------------------
# knapsack problem
# the largest volume of greedy algorithms


def FreeSpace(free, goods):
    return free-goods


def Greedy():
    goods_values = [20, 20, 25, 25, 45, 39, 28, 20, 10]
    goods_volumes = [3, 1, 2, 4, 1, 2, 3, 8, 2]
    bag_volume = 20
    print('Bag volume is:', bag_volume)
    Enter_records = []
    sort_volumes = goods_volumes.copy()
    sort_volumes.sort()  # from lowest to highest
    while sort_volumes:  # not None
        maxVolume = sort_volumes.pop(-1)  # return the last item
        Free = FreeSpace(bag_volume, maxVolume)
        if Free >= 0:
            bag_volume = Free  # free space of bag
            print('Mount volume of objects:', maxVolume)
            Enter_records.append(goods_values[goods_volumes.index(maxVolume)])
    if Enter_records != None:
        print('total value of goods in bag:%dRMB' % (sum(Enter_records)))


Greedy()
# --------------------------------------------------


def Density(g_values, g_volumes):
    dens = []
    for i in range(len(g_volumes)):
        dens.append(round(g_values[i]/g_volumes[i], 2))
    return dens


def GreedyDens():
    g_values = [4, 5, 7, 9, 11, 12, 15, 21, 23]
    g_volumes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bag_volume = 30
    enterrecords = []
    sortdens0 = Density(g_values, g_volumes)
    sortdens = sortdens0.copy()
    sortdens.sort()
    print(sortdens0, sortdens)
    while sortdens:
        max_val = sortdens.pop(-1)
        bag_free_space = FreeSpace(
            bag_volume, g_volumes[sortdens0.index(max_val)])
        if bag_free_space >= 0:
            bag_volume = bag_free_space
            print('objects:', sortdens0.index(max_val)+1)
            enterrecords.append(g_values[sortdens0.index(max_val)])
    if enterrecords != None:
        print('total value of goods in bag:%dRMB' % (sum(enterrecords)))


GreedyDens()
# --------------------------------------------------
# minimum spanning tree(MST)
# kruskal


def kruskal_Tree(nodes, edges):
    Mst = []
    n = len(nodes)
    i = 0
    sort_Glist = sorted(edges, key=lambda one: one[2])  # sorted:new list
    print('sorted:\n', sort_Glist)
    for one in sort_Glist:
        if not((one[0] in Mst and one[1] in Mst) or (one[1] in Mst and one[0] in Mst)):
            Mst.append(one)
            i += 1
        if i == n-1:
            break
    return Mst


nodes = ['A', 'B', 'C', 'D', 'E', 'F']
nodes_list = [('A', 'B', 1), ('A', 'C', 6), ('A', 'D', 6), ('B', 'D', 3), ('B', 'F', 4),
              ('B', 'E', 5), ('B', 'C', 4), ('C', 'E', 3), ('D', 'F', 2), ('E', 'F', 3)]
Tree = kruskal_Tree(nodes, nodes_list)
print('result:\n', Tree)
# sorted:
#  [('A', 'B', 1), ('D', 'F', 2), ('B', 'D', 3), ('C', 'E', 3), ('E', 'F', 3), ('B', 'F', 4), ('B', 'C', 4), ('B', 'E', 5), ('A', 'C', 6), ('A', 'D', 6)]
# result:
# [('A', 'B', 1), ('D', 'F', 2), ('B', 'D', 3), ('C', 'E', 3), ('E', 'F', 3)]
# --------------------------------------------------
# minimum spanning tree
# prim


def FindMinEdge(Nodes, row, edge, mst):
    n = len(edge)  # node corresponds to the number of sides
    j = 0  # initial j
    s_edge = sorted(edge)  # sort edges
    e_min = s_edge[0]
    while j < n:
        if edge[j] == e_min:
            a, b = Nodes[row], Nodes[j]
            if not ([a, b, e_min] in mst or [b, a, e_min] in mst):
                return j  # return index
            else:
                if s_edge[0] == s_edge[1]:
                    j += 1
                    continue
                j -= 1
                del(s_edge[0])
                e_min = s_edge[0]  # next
        j += 1
    return -1


def prim(nodes, edges):
    Mst = []
    i = 0
    n = len(nodes)
    for one in edges:  # 'A', 'B', 'C', 'D', 'E', 'F'
        index = FindMinEdge(nodes, i, one, Mst)
        # start node:'A',index=1,1
        a, b, w = nodes[i], nodes[index], edges[i][index]
        Mst.append([a, b, w])  # 'A','B',1
        i += 1  # next loop 'B'
        if i == n-1:
            break
    return Mst


f = float('inf')  # initialized to infinity
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges_list = [[f, 1, 6, 6, f, f],
              [1, f, 4, 3, 5, 4],
              [6, 4, f, f, 3, f],
              [6, 3, f, f, f, 2],
              [f, 5, 3, f, f, 3],
              [f, 4, f, 2, 3, f]]
r = prim(nodes, edges_list)
print(r)
# --------------------------------------------------
# huffman tree
# 1.sort nodes
# 2.new ele=list[0]+list[1];append new ele
# 3.del list[0],list[1];


def node_sort(R):
    return sorted(R, key=lambda one: one[1])


def HuffmanTree(Records):
    newHT = []
    sort_nodes = node_sort(Records)
    print('first sort nodes\n', sort_nodes)
    length = len(sort_nodes)
    if length == 1:
        print('only one node HuffmanTree:', sort_nodes)
        return sort_nodes
    newHT.append(sort_nodes[0])
    newHT.append(sort_nodes[1])
    new_parentNode = (sort_nodes[0][0]+sort_nodes[1]
                      [0], sort_nodes[0][1]+sort_nodes[1][1], 1)
    newHT.append(new_parentNode)
    if length == 2:
        return newHT
    while True:
        sort_nodes = sort_nodes[2:]
        sort_nodes.append(new_parentNode)
        sort_nodes = node_sort(sort_nodes)
        print('newHT:\n', newHT)
        print('next sort:\n', sort_nodes)
        length = len(sort_nodes)
        if length == 2:
            new_parentNode = (sort_nodes[0][0]+sort_nodes[1][0],
                              sort_nodes[0][1]+sort_nodes[1][1], sort_nodes[1][2]+1)
            newHT.append(new_parentNode)
            return newHT
        else:
            flag = True
            if (len(sort_nodes[0][0]) == 1 and len(sort_nodes[1][0]) == 1) and flag:
                if new_parentNode[1] > sort_nodes[1][1]:
                    level = new_parentNode[2]
                    pos = newHT.index(new_parentNode)
                    new_parentNode = (
                        sort_nodes[0][0]+sort_nodes[1][0], sort_nodes[0][1]+sort_nodes[1][1], level+1)
                    newHT.insert(
                        pos, (sort_nodes[0][0], sort_nodes[0][1], level))
                    newHT.insert(
                        pos+1, (sort_nodes[1][0], sort_nodes[1][1], level))
                else:
                    level = new_parentNode[2]-1
                    if new_parentNode[1] <= sort_nodes[0][1]:
                        level += 1
                        new_parentNode = (
                            sort_nodes[0][0]+sort_nodes[1][0], sort_nodes[0][1]+sort_nodes[1][1], level+1)
                        newHT.append(
                            (sort_nodes[0][0], sort_nodes[0][1], level))
                        newHT.append(
                            (sort_nodes[1][0], sort_nodes[1][1], level))
                        newHT.append(new_parentNode)
                        flag = False
                    if flag:
                        try:
                            index = newHT.index(sort_nodes[0])
                            newHT.insert(
                                index+1, (sort_nodes[1][0], sort_nodes[1][1], sort_nodes[0][2]))
                            new_parentNode = (
                                sort_nodes[0][0]+sort_nodes[1][0], sort_nodes[0][1]+sort_nodes[1][1], sort_nodes[0][2]+1)
                            newHT.append(new_parentNode)
                        except Exception:
                            try:
                                index = newHT.index(sort_nodes[1])
                                if sort_nodes[0][1] >= sort_nodes[1][1]:
                                    index += 1
                                newHT.insert(index, (sort_nodes[0][
                                             0], sort_nodes[0][1], sort_nodes[1][2]))
                                new_parentNode = (
                                    sort_nodes[1][0]+sort_nodes[0][0], sort_nodes[1][1]+sort_nodes[0][1], sort_nodes[1][2]+1)
                                newHT.append(new_parentNode)
                            except Exception:
                                pass


Records = [('A', 2, 0), ('B', 3, 0), ('C', 3, 0),
           ('D', 4, 0), ('E', 7, 0), ('F', 6, 0)]
h_tree = HuffmanTree(Records)
print('result:\n', h_tree)
# --------------------------------------------------
# choice of currencies


def Find_Money(Consume):
    Select_money = []
    if Consume <= 0:
        print('error')
        return []
    Moneys = [[10, 5], [5, 2], [50, 8], [20, 3], [100, 4], [2, 11], [1, 7]]
    sort_moneys = sorted(Moneys, key=lambda one: one[0], reverse=True)
    one_money = sort_moneys[0]  # [100,4]#[50,8]
    while sort_moneys:
        if Consume < one_money[0]:  # 561<100
            sort_moneys = sort_moneys[1:]
            one_money = sort_moneys[0]
            continue
        i = 1
        while i <= one_money[1]:  # 1<4 # 1<8
            Consume = Consume-one_money[0]  # 461,161 # 61
            print(i, Consume)  # 1, 461-->4,161
            if Consume < one_money[0] or i == one_money[1]:
                Select_money.append([one_money[0], i])  # 100,4
                if Consume == 0:
                    return Select_money
                sort_moneys = sort_moneys[1:]
                print('new sort', sort_moneys)
                if sort_moneys != None:
                    one_money = sort_moneys[0]  # 50
                    break
                else:
                    print('not enough money,difference:%d' % (Consume))
                return Select_money
            i += 1
    return Select_money


consume = 561
select_end = Find_Money(consume)
if select_end != []:
    print('consume:%d' % (consume))
    print(select_end)
