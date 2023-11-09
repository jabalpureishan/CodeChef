from sys import stdin
input = stdin.readline

def problem(length,k,string):
    return string.count(k*"0")

def takeinput():
    TestCases = int(input())
    while(TestCases>0):
        TestCases -= 1
        #length = int(input())
        
        #array = list(map(int, input().split()))
        length,k = map(int, input().split())
        string = input()
        print(problem(length,k,string))

takeinput()