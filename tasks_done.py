import os
import time

def return_str(arg):
    print ('"Hello, ' + str(arg) + '!"')

def sum(arr):
    sum = 0
    for i in arr:
        sum +=i
    #print (sum)
    return sum

def multiply(lst):
    mlt = 1
    for i in lst:
        mlt *=i
    #print (mlt)
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
    for i in arr:
        time.sleep(2)
        print (i*'*')       
    print ("```")

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
    print tmp
    return tmp


def main():
    diagonalReverse(([1,2,3], [4,5,6], [7,8,9]))

if __name__ == "__main__":
    main()
