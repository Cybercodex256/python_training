income=int(input("Income tax:"))
def calcIncometax(income):
    sum=0    
    if income <= 10000 :
         tax1=income*0/100
         sum+=tax1
         income=income-tax1
    if income <= 10000:
         tax2=income*0.1
         sum+=tax2
         income=income-tax2
    if income > 20000:
          tax3=income*0.2
          sum+=tax3
    print(sum)
     
calcIncometax(income)


