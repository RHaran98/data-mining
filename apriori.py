from itertools import combinations


def get_one_itemsets(tdb,ms):
    freq = {}
    for t in tdb:
        for i in t:
            freq[i] = freq.get(i, 0) + 1
    l = []
    for i in freq:
        if freq[i] >= ms:
            l.append(i)
    return [tuple(l)]


def get_count(items,tdb):
    c = 0
    for t in tdb:
        for i in items:
            if i not in t:
                break
        else :
            c+=1
    return c


def candidate_gen(L,k):
    items = []
    for s in L:
        for i in s:
            if i not in items:
                items.append(i)
    C = list(combinations(items,k))
    return C


def prune(C,tdb,ms):
    l = []
    for items in C:
        f = get_count(items, tdb)
        print(items,f)
        if f >= ms:
            l.append(items)
    return l


def apriori(tdb,ms):
    L = [[],get_one_itemsets(tdb,ms)]
    k = 2
    while len(L[k-1]) != 0:
        C = candidate_gen(L[k-1],k)
        L.append(prune(C,tdb,ms))
        k += 1
    return L[k-2]



tdb = []
#tdb = [[1,2],[2,3],[1,4],[3,4],[2,3,4]]
ms = int(input("Enter minimum support count : "))
file_name = input("Enter database file : ")

with open(file_name,'r') as f:
    for line in f:
        line = line.strip()
        tdb.append(line.split(','))
print(tdb)


fis = apriori(tdb,ms)
print("The frequent itemsets are : ",fis)