
def main():
    #Describes the program
    print('Enter two integers and I will tell you the relationship they satisfy.')

    #User imput
    firstInteger = int(input('Enter first integer: '))
    secondInteger = int(input('Enter second integer: '))

    #EQUAL
    if firstInteger == secondInteger:
        print( str(firstInteger) + ' IS equal to ' + str(secondInteger))
    else:
        print( str(firstInteger) + ' ISNT equal to ' + str(secondInteger))

    #LESS THAN
    if firstInteger < secondInteger:
        print( str(firstInteger) + ' IS less than ' + str(secondInteger))
    else:
        print( str(firstInteger) + ' ISNT less than ' + str(secondInteger))

    #LESS THAN OR EQUAL
    if firstInteger <= secondInteger:
        print( str(firstInteger) + ' IS less than or equal to ' + str(secondInteger))
    else:
        print( str(firstInteger) + ' ISNT less than or equal to ' + str(secondInteger))

    #GREATOR THAN
    if firstInteger > secondInteger:
        print( str(firstInteger) + ' IS greator than ' + str(secondInteger))
    else:
        print( str(firstInteger) + ' ISNT greator than ' + str(secondInteger))

    #GREATOR THAN OR EQUAL
    if firstInteger >= secondInteger:
        print( str(firstInteger) + ' IS greator than or equal to ' + str(secondInteger))
    else:
        print( str(firstInteger) + ' ISNT greator than or equal to ' + str(secondInteger))
    #Play again while loop
    restart=input("Do you want to compare two more numbers? [y/n]")    
    if restart == "y" or restart=="yes":
        main()
    else:
       exit()

#All the current "called" code
main()
