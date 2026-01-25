# Taking total amount as input from the user
Amount =int(input("please Enter Amount for Withdraw"))


# calculating the number of notes of defferent denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10


print("notes of 100 ropee" , note_1)
print("note of 50 rupee" ,note_2)
print("note of 10 ropee" , note_3)