class Person:
    name = "Ivan"
    age = 10
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    def _set(self, name, age):
        self.name = name
        self.age = age    
    

class Student(Person):
    course = 1

igor = Student("Игорь", 21)
igor.course = 2
#igor._set("Игорь", 21)
print(igor.name + " " + str(igor.age)+ " " + "курс: "+str(igor.course))

vlad = Person("Влад", 36)
#vlad._set("Влад", 36)
print(vlad.name + " "+str(vlad.age)) # why str? bcoz age is int type

ivan = Person("Иван", 20)
#ivan._set("Иван", 20)
print(ivan.name+" "+str(ivan.age)) #if print without "" and +, output will be in braces, like ('Ivan', '20')


