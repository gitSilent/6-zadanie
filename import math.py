kolvo_strok = int(input("Введите количество строк массива "))
massiv = []
for i in range(kolvo_strok):
    row=[]
    row = input("Введите элементы строки через пробел... ").split()
    massiv.append(row)
for i in range(kolvo_strok):
    print(massiv[i])

print("A)")
for i in range(len(massiv)):
    sum_stroki = 0
    for j in range(len(massiv[i])):
        sum_stroki = sum_stroki + int(massiv[i][j]) 
    
    print("Сумма элементов",i+1,"строки равна ", sum_stroki)

print("Б)")

#print(len(max(massiv)))
for i in range(len(massiv[0])):
    j = 0
    j = j + i
    sum_stolbca = 0
    for h in range (len(massiv)):
        sum_stolbca = sum_stolbca + int(massiv[h][j])
    print("Сумма элементов",i+1,"столбца равна ", sum_stolbca)
    
    