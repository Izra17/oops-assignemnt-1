#!/usr/bin/env python
# coding: utf-8

# In[2]:


#answer 1:
class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle=average_of_vehicle


# In[11]:


#answer 2
class car(vehicle):
    def seating_capacity(self,capacity):
             return f" the{self.name_of_vehicle} has a seating capacity of {capacity}."
    


# In[13]:


car=car("car",200,20)
print(car.seating_capacity(5))


# In[9]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The {self.name_of_vehicle} has a seating capacity of {capacity}."

# Example usage:
car = Car("Car", 200, 30)
print(car.seating_capacity(5))


# In[1]:


#answer 3
# multiple inheritence is defined as the inehritence where a single child can inherit the propertites of two different classes.
# This means that a single child class can inherit attributes and behaviors from multiple parent classes.
class izra:
    def test(self,name,id):
        self.name=name
        self.id=id
        print(f"hello frndo {self.name} your id is {self.id}")


class what:
    def test2(self,house,insta_id):
        self.house=house
        self.insta_id=insta_id
        print(f"youradrress is {self.house} and your instaid is {self.insta_id}")
class hello(izra,what):
    pass


obj_hello=hello()
obj_hello.test("anam",8999)
obj_hello.test2(89,900)


# In[7]:


#answer4
#getter and setter methods are used to access and modify the attributes
#of a class respectively, while encapsulating the internal implementation details


class Hello:
    def __init__(self):
        self._my_attributes = None  # Initialize _my_attributes in __init__

    def get_attributes(self):
        return self._my_attributes

    def set_attributes(self, value):
        self._my_attributes = value

obj = Hello()
obj.set_attributes(42)
print(obj.get_attributes())  # Corrected method name


# In[8]:


#answer5
#Method overriding in Python occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. 
class Animal:
    def speak(self):
        print("Animal speaks generic sound")

class Dog(Animal):
    def speak(self):  
        print("Dog barks")

class Cat(Animal):
    def speak(self):  
        print("Cat meows")


dog = Dog()
cat = Cat()


dog.speak()  
cat.speak()  



# In[ ]:




