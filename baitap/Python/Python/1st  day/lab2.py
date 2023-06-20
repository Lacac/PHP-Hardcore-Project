
string = input()

allow = ["u", "e", "o", "a", "i"]

for x in string:
    if(x not in allow):
        print(x.upper() , end="")
