print("Half pyramid pattern of string (*):")
n = int(input("enter the number of arrow: "))

for i in range(n):

    for j in range(i+1):

        print("* ", end="")
    print()