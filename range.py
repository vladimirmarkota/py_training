#FizzBuzz: from 1 to 50. if its divided by 3 and 5 print fizzbuzz, if its 3 fizz, 5 buzz, other int vlaue

range(1,50)

for i in range(1,50):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
            print("Fizz")
    elif i % 5 == 0:
                print("Buzz")
    else: print(i)






