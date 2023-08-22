import math
def main():
    card_no_orgi = int(input("Enter yout card number please: -- "))
    validate_count(card_no_orgi)
    if card_number == 5:
      print("step 1 ","card has 5 number")
      number_seperat(card_no_orgi)
      print("step 4 after seperate",seperated_num)

    else:
      print("please enter valide number you gives only "+str(card_number)+" number")

def validate_count(a):
     global card_number
     card_number=len(str(a))
     return card_number
     

def number_seperat(a):
    #global last_number
    global afterlast_remove
    global seperated_num
    seperated_num = [int(x) for x in str(a)]
    print("step 2 seperated number",seperated_num)
    #last_number = seperated_num[-1]
    afterlast_remove = seperated_num.pop(-1)
    print("step 3 that last number",afterlast_remove)
    
    return seperated_num 
    
   




main()
    

    
