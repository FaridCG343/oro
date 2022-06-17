#trabajpo de erika y fariks

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]


def sumando(x,y,m,n):
    if x >= m or y >= n or y<0:
        return 0
    print(x,y)
    maximo= max(gold[x][y]+sumando(x+1,y,m,n),
                gold[x][y]+sumando(x+1,y+1,m,n),
                gold[x][y]+sumando(x+1,y-1,m,n))
    return maximo

m = len(gold)
n = len(gold[0])
total = []
for i in range(len(gold)):
    total.append(sumando(i,0,m,n))
maximoT=max(total)
print(maximoT)
