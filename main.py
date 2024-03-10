try:
    my_list =[1,2,3,4,5]
    try:
        s= input ("pls enter an int :  ")
        print(my_list[s])
    except ValueError :
        print ("pls give an integer")
    except Exception as e:
        print("A sudden error occured")
except IndexError :
    print("hello")

finally :
    print ("code execution completed")







