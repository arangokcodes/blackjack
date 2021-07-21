import tkinter as tk
import random
 
de_c_1 = random.randint(1, 13)
de_c_2 = random.randint(1, 13)
 
pl_c_1 = random.randint(1, 13)
pl_c_2 = random.randint(1, 13)
 
 #If a number is 11, 12, 13 it means its K Q J
 #and return it to 10
def royalConversion(cardnumber):
  if cardnumber > 10:
    cardnumber = 10

def calculateSum(playercards):
  sum = 0
  for i in playercards:
    sum = sum + i
  return sum

#Convert Ace from 11 to 1 if sum exceeds 21
def aceHandler(sumOfCards, playercards):
  if playercards[0] == 11 and playercards[1] == 11:
      playercards[0] == 1
  else:
    for i in playercards:
      if i == 1 and sumOfCards + 10 <= 21:
        playercards[playercards.index(i)] = 11
      elif i == 11 and sumOfCards > 21:
        playercards[playercards.index(11)] = 1
        break
      else:
        pass
      sumOfCards = calculateSum(playercards)
      return sumOfCards

 
royalConversion(de_c_1)
royalConversion(de_c_2)
royalConversion(pl_c_1)
royalConversion(pl_c_2)
 
plCards = [pl_c_1, pl_c_2]
dlCards = [de_c_1, de_c_2]

sum_of_pl_c = calculateSum(plCards)
sum_of_de_c = calculateSum(dlCards)

sum_of_pl_c = aceHandler(sum_of_pl_c, plCards)
sum_of_de_c = aceHandler(sum_of_de_c, dlCards)

print(sum_of_pl_c)
print(sum_of_de_c)

def drawCard():
    print("Click Draw !!!")
    hit_card = random.randint(1, 13)
    print(str(hit_card))
    royalConversion(hit_card)
    plCards.append(hit_card)
    tempsum = calculateSum(plCards)
    tempsum = aceHandler(tempsum, plCards)
    sum_of_pl_c = tempsum
    print(sum_of_pl_c)
    if sum_of_pl_c > 21:
        lbl_gamecon["text"] = "Bust"
    else:
        pass
    lbl_value["text"] = f"{sum_of_pl_c}"
    return sum_of_pl_c

def passToDealer():
    print("Clicked Stop !!!")
    sum_of_pl_c =  int(lbl_value["text"])
    sum_of_de_c = calculateSum(dlCards)
    while sum_of_de_c < random.randint(15, 18) and sum_of_de_c < sum_of_pl_c :
        de_hit_card = random.randint(1, 13)
    
        royalConversion(de_hit_card)
        if de_hit_card == 1:
          if sum_of_de_c >= 11 :
            sum_of_de_c = sum_of_de_c + de_hit_card
          elif sum_of_de_c < 11 :
            de_hit_card = 11
            sum_of_de_c = sum_of_de_c + de_hit_card
    
        else:    
            sum_of_de_c = sum_of_de_c + de_hit_card
    
        print("Dealer hit card ---> ",de_hit_card)
        print("Sum of dealer hand = ",sum_of_de_c)
    
    if sum_of_pl_c > 21:
      print("You busted because " , sum_of_pl_c , " > 21")
    elif sum_of_de_c > 21:
      lbl_gamecon["text"] = "Dealer busted you won"
      lbl_dealersum["text"] = sum_of_de_c
      print("Dealer busted because " , sum_of_de_c , " > 21")
    elif sum_of_de_c < sum_of_pl_c:
      lbl_gamecon["text"] = "You won"
      lbl_dealersum["text"] = sum_of_de_c
      print("You Win because " , sum_of_pl_c , " > " , sum_of_de_c)
    elif sum_of_pl_c < sum_of_de_c:
      lbl_gamecon["text"] = "You lost"
      lbl_dealersum["text"] = sum_of_de_c
      print("You Lost because " , sum_of_de_c , " > " , sum_of_pl_c)
    else:
      lbl_gamecon["text"] = "Draw"
      lbl_dealersum["text"] = sum_of_de_c
      print("Draw " , sum_of_de_c , " = " , sum_of_pl_c)  
 
######################## GUI ########################

window = tk.Tk()
window.title("Black Jack <3 ")


#Size arrangments of window
window.columnconfigure([0, 1, 2], minsize=250, weight=1)
window.rowconfigure([0, 1, 2], minsize = 250,weight=1)

label_one = tk.Label(
    text="Push a button to proceed")
label_one.config(font = ("Couirer","14"))
label_one.grid(row = 0, column = 1, sticky="nsew")

lbl_value = tk.Label(master=window, text=sum_of_pl_c)
lbl_value.grid(row=1, column=1)

lbl_gamecon = tk.Label(master=window, text=" ")
lbl_gamecon.grid(row=2, column=2)

lbl_dealer = tk.Label(master=window, text=" Dealer Sum ==>")
lbl_dealer.grid(row=2, column=0)

lbl_dealersum = tk.Label(master=window, text=" ")
lbl_dealersum.grid(row=2, column=1)

btn_draw = tk.Button(master=window, text="Draw",  command=drawCard) # Draw card not updating global value sum_of_pl_c
btn_draw.grid(row=1, column=0, sticky="nsew")

btn_increase = tk.Button(master=window, text="Stop", command=passToDealer)
btn_increase.grid(row=1, column=2, sticky="nsew")

window.mainloop()

#####################################################
