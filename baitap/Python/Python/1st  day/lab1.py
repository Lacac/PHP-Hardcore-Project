
secret_number = 99 

while True:
    try:
        if(int(input("Guess the secret number: ")) == secret_number):
            print("Well done, muggle! You are free now.")
            break
        else: 
            print("Ha ha! You're stuck in my loop!")
    except:
            print("Ha ha! You're stuck in my loop!")