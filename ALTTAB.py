from collections import OrderedDict
def main():
    Tests = int(input(""))
    new = OrderedDict({})
    while(Tests>0):
        Tests -= 1
        string = input("")
        if string in new:
            new.pop(string)
            new[string]=""
        else:
            new[string] = ""
    new = tuple(new)
    output = ""
    for i in range(-1,-(len(new)+1),-1):
        output += new[i][-2:]
    print(output)
    
        

main()