#OOPS-Object Oritented Programming Structure

#Object-Everything is an object(properties-attributes,function-methods)
#Class-Is a blueprint of the object-class contains the attributes and functions of the object as well as the different types of objects

class Student():
    def __init__(self,name,age,grade,favColor,hobby):
        self.name=name
        self.age=age
        self.grade=grade
        self.favColor=favColor
        self.hobby=hobby
        self.intro=""
    
    def showDetails(self):
        print("The details of the student are:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grade",self.grade)
        print("Favorite Color:",self.favColor)
        print("Hobbies:",self.hobby)
    
    def introStudent(self):
        self.intro=input("Please introduce yourself:")
        print(self.intro)

#Object-Instance of a Class
#__init__ function gets called automatically when an object is created
s1=Student("Ipek","16","11th grade","light blue","playing volleyball")

#To Call the User Defined Function- object_name.function_name()

s1.showDetails()
s1.introStudent()

s2=Student("Zoya","16","11th grade","pink","playing badminton")
s2.showDetails()
s2.introStudent()

s3=Student("Sam","13","7th grade","yellow","baking")
s3.showDetails()
s3.introStudent()