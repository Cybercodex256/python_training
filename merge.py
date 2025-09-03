list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


def compOdd(*args):
    list_odd = []
    for num in args:
       
          #  if number %2 != 0:
          #      list_odd.append(number)
          list_odd+=[number for number in num if number% 2 != 0 ]
    return  list_odd

print(compOdd(list1,list2,[20,45,78,38,59,57,238,39]))


