from database import add_expense, get_expenses

exp_dict = {}
name = input("enter your name : ")
name_u = name.upper()
def show_menu():
  print("======Expense TRacker======"  )
  print(f"{name_u}"  " welcome to expense tracker")
  print("1 - debit ")
  print("2 - view record ")


categories = ["food", "travel", "shopping", "education", "other"]

def cateogry_exp():
   print("cateogory wise t")


def get_expense():
  print(exp_dict)



while True:
    show_menu()
    choice = int(input("enter choices"))
    if choice == 1:
     print("enter the following details")
     id = int(input("enter id "))
     amount = float(input("enter amount :"))
     date = input("enter date dd/mm :")
     category = input("enter category :")
     categoryl= category.lower()
     description = input("enter description :")
     add_expense(id,amount,category,date,description) 
     if categoryl not in  categories:
        print("invalid categary input")
    elif choice == 2:
     get_expense()
    else:
     print("invalid input")
    
     break

       


print(exp_dict)

amounts = [data["amount"] for data in exp_dict.values()]


am_food = []
am_tav =[]
am_edu =[]
am_sh = []
am_oth = []
for data in exp_dict.values():
   if data["category"] == "food":
     am_food.append(data["amount"])
   elif data["category"] == "travel":
      am_tav.append(data["amount"])
   elif data["category"] == "education":
          am_edu.append(data["amount"])
   elif data["category"] == "shopping":
         am_sh.append(data["amount"])
   elif data["category"] == "other":
          am_oth.append(data["amount"])



import numpy as np

total = np.sum(amounts)
average = np.mean(amounts)
print(total)
print(average)


print("the indivisual analysis you want")
print("1 food")
print("2 travel")
print("3 education")
print("4 shopping")
print("5 others")
options = int(input("enter your option"))

def show_food():
  total_food = np.sum(am_food)
  average_food = np.mean(am_food)
  per_food = (total_food/ total)*100
  print(total_food)
  print(average_food)
  print(per_food)


def show_trav():
  total_trav = np.sum(am_tav)
  average_trav = np.mean(am_tav)
  per_trav = (total_trav/ total) *100
  print(total_trav)
  print(average_trav)
  print(per_trav)

def show_edu():
  total_edu = np.sum(am_edu)
  average_edu = np.mean(am_edu)
  per_edu = (total_edu/total)*100
  print(total_edu)
  print(average_edu)
  print(per_edu)

def  show_sh():
  total_sh = np.sum(am_sh)
  average_sh = np.mean(am_sh)
  per_sh = (total_sh/total)*100
  print(total_sh)
  print(average_sh)
  print(per_sh)

def show_oth():
 total_oth = np.sum(am_oth)
 average_oth = np.mean(am_oth)
 per_oth = (total_oth/total)*100
 print(total_oth)
 print(average_oth)
 print(per_oth)

if options ==1:
   show_food()
elif options == 2 :
   show_trav()
elif options == 3:
   show_edu()
elif options == 4 :
   show_sh()
elif options == 5 :
   show_oth()




print("thnk you ")




  
  
