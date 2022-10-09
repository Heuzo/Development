entered_list = input("Введите список чисел, разделенных пробелом: ").split()
list1 = [int(i) for i in entered_list]
list2 = []

for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)
