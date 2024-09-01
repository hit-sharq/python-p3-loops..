
#!/usr/bin/env python3

def happy_new_year():
    i= 10
    while i>-1:
        if(i>0):
            print(i)
        else:
            print("Happy New Year!")
        i-=1

    pass

def square_integers(int_list):
    int_list = [num*num for num in int_list]
    return int_list
    pass

def fizzbuzz():
    for i in range(1,101):
        if(i%5 == 0 and i%3 == 0):
           print("FizzBuzz")  
        elif(i%3 == 0):
            print("Fizz")
        elif(i%5 == 0):
            print("Buzz")
        else:
            print(i)
    pass
