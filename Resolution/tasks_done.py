import os
import time
import random



def decToBin(value):
    arr = []
    if value < 0:
        raise Exception
    integer = int(value)
    while (integer // 2) >= 0:
        temp = integer % 2
        integer = integer // 2
        arr.append(temp)
        if integer == 0:
            break
    integer = int(("".join(str(i) for i in arr))[::-1])
    print(integer)
    return integer

def charFreq(arg):
    dictionary = {}
    for i in arg:
        if i not in dictionary.keys():
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    print (dictionary)
    return dictionary


def return_str(arg):
    print ('"Hello, ' + str(arg) + '!"')
    return '"Hello, ' + str(arg) + '!"'

def summ(arr):
    sum = 0
    for i in arr:
        sum +=i
    print (sum)
    return sum

def multiply(lst):
    mlt = 1
    for i in lst:
        mlt *=i
    print (mlt)
    return (mlt)

def reverse(string):
    return string[::-1]

def isPalindrome(string):
    string = string.lower()
    rvs_str = reverse(string)
    if list(string) == list(rvs_str):
        return True
    else:
        return False

def histogram(arr):
    print ("```")
    temp = []
    for i in arr:
        time.sleep(2)
        if i < 0:
            print("```")
            raise Exception
        else:
            print (i*'*')
            temp.append(i*'*')       
    print ("```")
    return temp

def caesarCipher(string, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in string:
        result += alphabet[(alphabet.index(i) + key) % len(alphabet)]
    print ('Result: ' + result)
    return result



def diagonalReverse(lst):
    arr = []
    tmp = []
    for i in range(len(lst)):
        for j in lst:
            arr.append(j[i])
    for k in range(len(lst)):
        tmp.append(arr[:len(lst)])
        arr = arr[len(lst):]
    print (tmp)
    return tmp


def game(a,b):
    rand = random.randint(a, b)
    print (rand)
    while True:
        try:
            c = int(input('Choose your int number: '))
        except ValueError:
            print("Not integer value")
            break
        else:
            if int(c) < 0:
                print ('You must choose int. Try again!')
                continue 
            elif rand == int(c):
                print ('Congratulate')
                return int(c)
            else:
                print ('Try again!')
                continue


def balanced_str(string):
    opening = ("[")
    closing = ("]")
    dictionary = dict(zip(opening, closing))
    arr = []
    if string[0] == closing or string[-1] == opening:
        return False
    for i in string:
        if i == opening:
            arr.append(dictionary[i])
        elif i == closing:
            if not arr:
                return False
            if arr[-1] == i:
                arr.pop() 
            else:
                return False            
    return True


def main():
    decToBin(100)
    #game(1,10)
    #diagonalReverse([[1,2,3], [4,5,6,'',4,10], [7,8,9,9]])
    #caesarCipher("abczyw", 4)
    #print(isPalindrome(12345))
    #reverse(1234567)
    #decToBin(121)
    #charFreq("abbabcbdbabdbdbabababcbcbahhbhloll")
    #temp = balanced_str("[]][[]")
    #if balanced_str("[[][]]") == True:
    #    print("Balanced")
    #else:
    #    print("Not balanced")
    
if __name__ == "__main__":
    main()
