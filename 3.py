import w
m = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
    [1,0,0,0,1,1,1,1,0,1,1,0,1,0,1],
    [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
w.v(m, 0)
for y in range(len(m)):
    if m[y][14] == 0:
        (w.AllWays).remove([y,14])
def d(d):
    for i in range(len(d)):
        (w.AllWays).remove(d[i])
#Убираем все те, у которых 3 клетки путстые
dele = []
def RemoveThirdItem():
    for i in range(len(w.AllWays)):
        k = 0
        if m[w.AllWays[i][0] + 1][w.AllWays[i][1]] == 1:
            k += 1
        if m[w.AllWays[i][0] - 1][w.AllWays[i][1]] == 1:
            k += 1
        if m[w.AllWays[i][0]][w.AllWays[i][1] + 1] == 1:
            k += 1
        if m[w.AllWays[i][0]][w.AllWays[i][1]- 1] == 1:
            k += 1
        if k >= 3:
            m[w.AllWays[i][0]][w.AllWays[i][1]] = 1
            dele.append([w.AllWays[i][0],w.AllWays[i][1]])
RemoveThirdItem()

#Удаляем ненужные
d(dele)
dele = []
#Прповеряем на наличие 3 нижних или 3 верхних
for i in range(len(w.AllWays)):
    if ((m[w.AllWays[i][0] - 1][w.AllWays[i][1] - 1] == 0) and (m[w.AllWays[i][0] - 1][w.AllWays[i][1] ] == 0) and (m[w.AllWays[i][0] - 1][w.AllWays[i][1] + 1] == 0)) or ((m[w.AllWays[i][0] + 1][w.AllWays[i][1] - 1] == 0) and (m[w.AllWays[i][0] + 1][w.AllWays[i][1] ] == 0) and (m[w.AllWays[i][0] + 1][w.AllWays[i][1] + 1] == 0)):
        if [w.AllWays[i][0],w.AllWays[i][1]] not in dele:
            m[w.AllWays[i][0]][w.AllWays[i][1]] = 1
            dele.append([w.AllWays[i][0],w.AllWays[i][1]])
d(dele)
for i in range(len(m)):
    RemoveThirdItem()


print(w.AllWays) #для вывода индексов пути
print(w.v(m, 1)) #для вывода пути
    