def classic_fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            print ('FizzBuzz!')
        elif number % 5 == 0:
            print ("Buzz!")
        elif number % 3 == 0:
            print ('Fizz!')
        else:
            print (str(number))
        
        return print

classic_fizzbuzz(15)
'FizzBuzz!'

classic_fizzbuzz(13)
'13'

