# 60DaysOfLearning2025

I'll be using this repo to document my **#60DaysOfLearning** journey, where I can track my progress, stay consistent, and reflect along the way.I'll start from learning OOP in python.

---

## Day 1/60

**Object Oriented Programming** is a programming paradigm that organizes software design around objects, which represent real-world entities.



### Key Ideas of OOP
- **Classes**
- **Object**
- **Encapsulation**
- **Inheritance**
- **Polymorphism**
- **Abstraction**



### Class

A **class** is a blueprint or template for creating objects. It defines **attributes** (properties) and **methods** (behaviours) that objects will have.

**Components of Class:**
- **Attributes**: Data members that store the state or properties of the object.
- **Methods**: Functions inside a class that define the behaviour of the object.
- **Constructor**(`__init__`): A special method used to initialize attributes when an object is created.


### Object

An object is an instance of a class. It represents a real-world entity with specific **properties** (attributes) and **behaviours** (methods).

---

## Day 2/60

### Inheritance
Inheritance is a feature of OOP that allows one class (child/derived class) to acquire attributes and methods from another class (parent/base) class. It  helps establish a hierarchical relationship between classes.

### Key ideas of Inheritance
- `super()` <br>
A function used to call a method or constructor from the parent class.
- Method Overriding <br>
When a method in the child class has the same name as one in the parent class, the child's method overrides the parent's method.

### Types of Inheritance
- Single Inheritance
- Multiple Inheritance
- Multi-Level Inheritance
- Hierarchical Inheritance 
- Hybrid Inheritance

### Single Inheritance
Single Inheritance is a scenario where there is only one Base(parent) class and only one Derived (Child) class.

### Multiple Inheritance
In multiple Inheritance a single child (derived) class is derived from two parent(base) class.

---

## Day 3/60
- In multiple inheritance, if both parent classes have a method with the same name, however, if we want to call a specific method from one of the parent classes, we can do it by explicitly calling the method from the parent class, passing self as an argument.

### Multi-Level Inheritance
Mutli-Level Inheritance is the type of inheritance in which a class inherits from a class, which itself inherits from another class.__(Grandparent--Parent--Children)classe__
- We can directly access method of Grandparent class from child class method by calling it explicitly by using the `name of grandparent-class.method`

__or__
- We can acess the method of grandparent class from method of parent class using `super()` method; and method of child using `super()` method.

### Hierarchical Inheritance
Hierarchical Inheritance is the type of inheritance in which a single class is inherited by multiple derived classes.

---
## Day 4/60
### Hybrid Inheritance

Hybrid Inheritance is a blend of multiple inheritance types.In hybrid inheritance, the classes are derived from more than one base class, creating a complex inheritance structure.

### Encapsulation
Encapsulation combines two things:
- Data (Attributes): Properties that hold the state of the object
- Methods: Functions that define the behaviour of the object

### Access Specifiers in python 

__Public Attributes:__
- Accessible from anywhere
- No Special Syantax required(default).

__Protected Attributes:__
- Indicated by `_attribute` (single underscore)
- A Convention: Indented for internal use only but still accessible

__Private Attributes:__
- Indicated by `__attribute` (double underscore)
- Python uses name mangling to make this attributes harder to access directly.

__Getter and Setter:__

A getter and setter are methods used to access and update the attributes of class.
- _Getter_: The getter method is used to retrieve the value of private attribute. it allows controlled acess to the attribute
- _Setter_: The setter method is used to set or modify the value of a private attribute. It allows us to control how the value is updated, enabling validation or modification of data before it's actually assigned.

There is also an buit-in property to simplify the creating of getters and setters.

---
## Day 5/60
__Property Decorator__
- an pythonic way to define getters and setters and.
- Works like property() but uses decorator for cleaner code.

__Name Mangling__
- Python uses Name Mangling to make private attributes harder to access but not impossible. You can access them using `_ClassName_attribute`
- Generally, this method is not recommended cause it voilates the purpose of encapsulation

__Public Method__
- Methods that can be accessed from anywhere, including outside the class.(default methods)
- Name Convention: Public Methods do not use any special prefix

__Protected Method__
- Methods intended for internal use by the class and it's related code. However, they can still be accessed by from outside the class.
- Naming Convention: Protected Methods starts with a single underscore (`_`)

*Acessing Private Method*
- Using  Public Methods that Internally calls Private Methods, This ensures that private methods remains hidden while serving their indented purpose.
---

