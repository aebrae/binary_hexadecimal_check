#!/usr/bin/python3

"""Checks if as a binary number(string) is equal to its hexadecimal equivalent""" """Method: User Input"""
"""E.g. '11110001' --> 'F1'""" 
def convertDectoHex(number):
        if number == 10:
                return 'A'
        elif number == 11:
                return 'B'
        elif number == 12:
                return 'C'
        elif number == 13:
                return 'D'
        elif number == 14:
                return 'E'
        elif number == 15:
                return 'F'
        return str(number)

def binaryCheck():
        while True:
                binary = input("Enter a binary number with the number of digits being divisible by 4 o>
                if binary == "exit":
                        break
                hex = input("Enter the hexadecimal equivalent to verify: ").upper()
                index = 0
                hexaString = ''
                while  index != len(binary):
                        binaryValue = 0
                        for x, digit in enumerate(binary[index:index+4]):
                                if x == 0 and digit =='1':
                                        binaryValue += 8
                                if x == 1 and digit == '1':
                                        binaryValue += 4
                                if x == 2 and digit == '1':
                                        binaryValue += 2
                                if x == 3 and digit == '1':
                                        binaryValue += 1
                                #print(x,digit)
                        #print(binaryValue)
                        hexaString += convertDectoHex(binaryValue)
                        index += 4
                #print(hexaString)
                if  hexaString == hex:
                        print("{} is equivalent to  {}".format(binary,hex))
                else:
                        print("The two numnbers are not a match.")
binaryCheck()
