import animal
class Visitor:                        # Visitor class
    def __init__(self,name,age):
        self.name=name
        self.age=age
  
    
    def feed(self,animal:animal,food):    # Intercation between visitor and animal (Feed)
        if animal.is_awake==False:
            print("Do not distrub,animal is sleeping.")
        else:
            if animal.dangerLvl < 4:          # Checking danger level and appropriate food 
                if food==animal.food:
                    animal.eat()
                    print("Thanks for feeding ")
                    animal.makeSound()              # Animal reacts by making sounds
                else: 
                    print("Food is not correct.")
            else:
                print("Not allowed to feed,It's dangerous")

   
    
    def pat(self,animal:animal):           # Intercation between visitor and animal (Pat)
        if animal.is_awake==False:
            print("Do not distrub,animal is sleeping.")
        else:
            if self.age>10 and animal.dangerLvl <4 :
                print("You can pat!")
            elif animal.dangerLvl ==1 and animal.size == "small"and animal.is_awake==True:
                print("You can pat!")
            else:
                print("Not safe to pat")
    
    

        

    