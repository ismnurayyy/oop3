
# Bir classdan istifadə edərək 2 metod yazın.
# İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın  və onu bir listə əlavə edin ( bu şəkildə olacaq: mylist=[1,2,3,4,5])
# Daha sonra bir metod daha yazın. Bu metodda isə bizim bir argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin 
# dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə bərabərdirsə həmin rəqəmlərin indexlərini qaytarın. Əgər belə
# rəqəmlər yoxdursa -1 cavabı qaytarın. 

# Əlavə olaraq argumentləri hansı metodunuzda istifadə etmək istədiyiniz barəsində sərbəstsiniz və əlavə arqumentlərdən istifadə edəbilərsiniz.

class reqemler:
    
    def __init__(self):
        self.mylist = []

    def reqemelaveet(self,newlist):
        self.mylist.extend(newlist)

    def hedef_reqem(self,hedef_reqem):
        indeks = []
        for i in range(len(self.mylist)):
            for j in range(i+1,len(self.mylist)):
                if(self.mylist[i] + self.mylist[j] == hedef_reqem):
                    indeks.append((i,j))
        if indeks:
            return indeks
        else:
            return -1      

list1 = reqemler()
list1.reqemelaveet([1,2,3,4,5,6,7])

print(list1.hedef_reqem(7))


