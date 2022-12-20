from random import randint as rint
class SortingList:
    def __init__(self, n):
        self.uniq = []
        self.not_uniq = []
        self.list_basic = [1,2,3,4,5,6,7,8,9]
        self.n = n
        self.R(self.n)
    def sorting(self, number):
        for i in number:
            if i not in self.uniq:
                self.uniq.append(i)
            else:
                self.not_uniq.append(i)
        print(self.uniq)
        print(self.not_uniq)
        print(self.list_basic)
    def R(self, shit):
        arr = []
        for i in range (shit):
            arr.append(rint(1, 10))
        return arr

class N_Matrica():
    def __init__(self):
        n = int(input("Ievadi skaitli n = kollonu un rindu skaitu: "))
        self.r = SortingList(n)
        self.matrica(n)
    def matrica(self,m):
        arr = []
        for i in range(m):
            arr.append(self.r.R(shit=m))

        shit_map_i = 0
        shit_sum = 0

        for item in (arr):

            shit_sum += item[shit_map_i]
            print(item)

            shit_map_i += 1

        if shit_sum > 0:
            print("sum: ", shit_sum)


xd = N_Matrica()
xd.matrica(-1)
