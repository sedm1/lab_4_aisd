import colorama
from colorama import Fore, init
colorama.init()
init(autoreset=True)

AllWays = []
#main
def v(x, k):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 0:
                if k == 1:
                    print(Fore.BLUE + str(x[i][j]), end=' ')
                    AllWays.append([i, j])
                else:
                    AllWays.append([i, j])
            else:
                if k == 1:
                    print(str(x[i][j]), end=' ')
        if k == 1:
            print('')
