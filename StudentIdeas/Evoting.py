from os import system as exe
import sqlite3
db=sqlite3.connect("votes.db")
cu=db.cursor()
#cu.execute("create table votes(candidate , votes )")


contestants =["Yoweri","Bobi","political vundutulutu"]
#for candidate in contestants:
#   cu.execute("insert into votes values(?,?)",(candidate ,0))

yoweri_votes =0
Bobi_votes=0
politicalvun_votes =0

while True:
    for row in cu.execute("select * from votes"):
            print(row)
            print("_____________________")
    print("------------ E-voting Program ------------") 
    print("Select your candidate:")
    print("1.Yoweri")
    print("2.Bobi")
    print("3.Political Vundutulutu")
    choice=int(input("Enter your preffered candidate:"))
    match(choice):
        case 1:
             yoweri_votes+=1 
             cu.execute("insert into votes values(?,?)",(contestants[0],yoweri_votes))
            
        case 2:
             Bobi_votes+=1
             cu.execute("insert into votes values(?,?)",(contestants[1],Bobi_votes))
        case 3:
             politicalvun_votes+=1
             cu.execute("insert into votes values(?,?)",(contestants[2],politicalvun_votes))
        case 4:
              print("Thank you for voting.")
              cu.close()
              break
    exe("clear")
    print(f"Yower: {yoweri_votes}\n")
    print(f"Bobi: {Bobi_votes}\n")
    print(f"political Vundutulutu: {politicalvun_votes}\n")
   
