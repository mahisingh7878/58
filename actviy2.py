num=int(input("enter a number") )

def print_factors(x):


    print("the factors  ",x,"are:")
    for i in range(1,x+1):
        if x% i ==0:
            print(i)
print_factors(num)

            