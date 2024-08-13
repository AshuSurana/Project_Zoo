from animal import Carnivore
from animal import Herbivore
from visitor import Visitor
import random

zebra = Herbivore(name='foo', age=6, specie='Zebra', size='medium', position='cage 11', dangerLvl=2, environment='savanna', food='grass',sound="Neigh-Neigh",is_awake=random.choice([True, False]))
tiger = Carnivore(name='bar', age=5, specie='Tiger', size='medium', position='cage 5', dangerLvl=5, environment='savanna', food='meat',sound="roarrrr",is_awake=random.choice([True, False]))
rabbit=Herbivore(name='clover', age=3, specie='Rabbit', size='small', position='cage 2', dangerLvl=1, environment='savanna', food='carrot',sound="nurf nurf",is_awake=True)
elephant=Herbivore(name='tim', age=5, specie='Elephant', size='big', position='cage 12', dangerLvl=2, environment='savanna', food='leaves',sound="Trumph Trumph",is_awake=True)
lion=Carnivore(name='king', age=6, specie='Lion', size='medium', position='cage 7', dangerLvl=5, environment='savanna', food='meat',sound="roarrr",is_awake=True)


visitor_name=input("Enter your name: ")
visitor_age=int(input("Enter your age:"))
visitor=Visitor(visitor_name,visitor_age)     # Creating object of visitor class


print("------------------")      # Intercative interface for visitors
choice=int(input("Enter your Choice:\n1:To get info about an animal\n2:To feed an animal\n3:To pat an animal "))
print("---------------------")
animal_choice=(input("Enter animal name in which you are intersed:\nt:Tiger  z:Zebra  r:Rabbit   e:Elephant  l:Lion \n"))
print("---------------------")
animal={
    "t":tiger,
    "z":zebra,
    "r":rabbit,
    "e":elephant,
    "l":lion
}

# Display all the info about sepcific animal
if choice==1:                    
    tmpvar = animal.get(animal_choice)
    print(tmpvar)
    #print(type(tmpvar))
    print("-----------------")
# Feeding a chossen animal depending on conditions and increase energy level   
elif choice==2:                    
    food=input("What do you want to feed: ")
    visitor.feed(animal.get(animal_choice),food)
    print("----------------------")
# Patting a choosen animal depending on condition(age of visitor,size of animal,dangerlevel,animal awake or not)
# Animal react by making happy sounds
elif choice==3:                 
    visitor.pat(animal.get(animal_choice))
    #print(animal.get(animal_choice).is_awake)
    if animal.get(animal_choice).is_awake == True and animal.get(animal_choice).dangerLvl <4 :
            print(f"Happy {animal.get(animal_choice).specie} sound likes : ")
            animal.get(animal_choice).makeSound()
            print("--------------------------") 

       
   
#print(tiger)
#tiger.eat()
#visitor2.pat(tiger)

#visitor2.feed(rabbit,"carrot")
#visitor2.pat(rabbit)

#print(zebra)
#zebra.eat()
#visitor1.feed(zebra,"meat")
#visitor1.pat(zebra)
#zebra.play(zebra)
#zebra.makeSound()
#lion.hunt(zebra)

