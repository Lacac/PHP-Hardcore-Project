class Animal:
    age = int()
    gender =str()

    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def isMammal(self):
        return True

    def mate(self):
        return True

    def __str__(self):
        return f'gender: {self.gender}, age:{self.age}'

class Duck(Animal):
    breakColor = "yellow"

    def __init__(self, age, gender):
        super().__init__(age, gender)

    def isMammal(self):
        return False

    def swim(self):
        print("Hey, i can swim .... like other duck in this world")

    def quack(self):
        print('quack ... quack ... quack')

    def __str__(self):
        return f'I am a {self.gender} {self.breakColor} duck and i {self.age} year old.'

class Fish(Animal):
    sizeInFt = int()
    canEat = bool()

    def __init__(self, age, gender, sizeInFt, canEat):
        super().__init__(age, gender)
        self.sizeInFt = sizeInFt
        self.canEat = canEat

    def isMammal(self):
        return False

    def swim(self):
        print('what do you expect the fish to do? ofcourse ... swimming')

    def __str__(self):
        if(self.canEat):
            return f'I am a {self.gender} fish, i\'m {self.age} year old and i {self.sizeInFt}\' long. And... you can eat me :('
        else:
            return f'I am a {self.gender} fish, i\'m {self.age} year old and i {self.sizeInFt}\' long. And... you can\'t eat me :)'

class Zebra(Animal):
    is_wild = bool()

    def __init__(self, age, gender, is_wild):
        super().__init__(age, gender)
        self.is_wild = is_wild
    
    def isMammal(self):
        return True

    def run(self):
        print('I can run very fast and you can\'t catch me :))')
    
    def __str__(self):
        if(self.is_wild):
            return f'I am a {self.gender} Zebra, i\'m {self.age} year old. And i\'m wild'
        else:
            return f'I am a {self.gender} Zebra, i\'m {self.age} year old. And i\'m a housetrained Zebra'


Marty = Zebra(2, "male", True)
Nemo = Fish(1, "male", 4, False)
Little_Quacker = Duck(2, "female")

Little_Quacker.swim()
print(Little_Quacker.isMammal())