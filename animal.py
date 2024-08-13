class Animal:                # Base class Animal
    def __init__(self, name:str, age:int, specie:str, size:str, position:str, dangerLvl:int, environment:str,is_awake:bool ):
        self.thirst = 10
        self.hunger=5
        self.calories = 20
        self.sleepHr= 9
        self.energylvl = self.thirst + self.calories+ self.sleepHr
        self.name = name
        self.age = age
        self.specie = specie
        self.size = size #big, small, medium
        self.dangerLvl = dangerLvl #1(harmless) - 5 (dangerous)
        self.environment = environment
        self.position = position #cage, habitat, water
        self.is_awake=is_awake   # random generating value(True or False)
  
    def __str__(self):
       return f"Specie:{self.specie}    Age:{self.age}  DangerLevel:{self.dangerLvl}\nYou can found me in :{self.position}   Awake:{self.is_awake}" 

    def eat(self):                 # Eat increases energy level
        if(self.size == 'big'):    # Energy Level= Eat+Drink+sleep 
            self.calories += 2
        if(self.size == 'medium'):
            self.calories += 4
        if(self.size == 'small'):
            self.calories += 6

    def sleep(self):
        self.sleepHr+=2           
        

    def drink(self):              # Drink increases energy level
        if(self.size == 'big'):   # Energy Level= Eat+Drink+sleep 
            self.thirst += 2
        if(self.size == 'medium'):
            self.thirst += 4
        if(self.size == 'small'):
            self.thirst += 6
    
    def makeSound(self):
        print("Animal sound")

    def play(self, animal):       # Intercation (Play) between animals
        if(animal.dangerLvl>3 or self.dangerLvl>3 and self.specie != animal.specie):
            print("Too dangerous to play")
        else:
            print("It's play time!")   # Play decrease energy level
            self.calories -= 3
            self.thirst -= 4
            self.sleepHr -= 2
            animal.calories -= 3
            animal.thirst -= 4
            animal.sleepHr -= 4

    

class Herbivore(Animal):    # Derived Class of Animal
  
  def __init__(self, name:str, age:int, specie:str, size:str, position:str, dangerLvl:int, environment:str, food:str,sound:str,is_awake:bool):
    super().__init__(name, age, specie, size, position, dangerLvl, environment,is_awake)
    self.food = food
    self.sound = sound
  
  def __str__(self):
     return f"{super().__str__()}\nI eat greens and my fav. food is {self.food}\n All day long a say '{self.sound}'"

  def eat(self):
    print(f"I eat {self.food}")
    super().eat()
    print("Total Calories: ",self.calories)
    print("Total Energy: ",self.energylvl)

  def makeSound(self):
     print(self.sound)  

class Carnivore(Animal):      # Derived class of Animal
  
  def __init__(self,name:str, age:int, specie:str, size:str, position:str, dangerLvl:int, environment:str, food:str,sound:str,is_awake:bool):
    super().__init__(name, age, specie, size, position, dangerLvl, environment,is_awake)
    self.food=food
    self.sound=sound
  
  def __str__(self):
     return f"{super().__str__()}\nI eat dead corpses and my fav. food is {self.food}\nAll day long a say'{self.sound}'"
       
  def eat(self):
    print("I eat {self.food}")
    super().eat()

  def makeSound(self):
     print(self.sound)  

  def hunt(self,animal):     # Intercation (Hunt) between animals
       if self.dangerLvl>animal.dangerLvl and self.hunger>3 and self.food=="meat":
          print(f"{self.specie} hunts/eat {animal.specie}") 
          self.hunger-=5
          self.calories+=50
       else:
          print("Can't hunt---either not hungry,or not like meat or not able to hunt")
          
  
  