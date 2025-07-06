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
## Day 6/60

Solved Inheritance and Encapsulation based questions, which helped me understand concept more cleary.

---

## Day 7/60

### Polymorphism
The terms "Polymorphism" means "many form".<br>
Polymorphism is a key concept in OOP, which allows objects of different class to respond to the same method call in different ways. It simplies code and and enhances flexiblity by enabling a single interface to represent different underlying forms(data types). 

### Types of Polymorphism:-

__Compile-Time Polymorphism:__
- Achieved using method overloading and operator overloading
- Allows Methods/Operators to behave differently based on their inputs

__Run-Time Polymorphism:__
- Achieved using method overiding
- The behaviour of a method is determined at runtime based on object's type.

### Method Overloading

Method Overloading allows a class to define multiple methods with the same name but different argument lists.It enables method to behave differently based on the number or type of arguments passed.

Python does not support traditional method overloading like other programming language such as  Java or C++. In python:
- The latest defined method with the same name will overwrite the earlier ones
- However, we can achieve similar behaviour using default arguments, variable lenghts arguments(`*args`and `**kwargs`) or type checking

__Type Checking__

Type Checking in Python refers to verifying the data type of variables, object  or a value, either at runtime or (optionally) during static analysis.

---
## Day 8/60

### Operator Overloading
- Operating overloading in python allows us to define custom behaviour for standard operators (like +,-,*).Which they are used with objects of user-defined classes. It is implemented by overriding special methods, also known as dunder(double underscore) methods.

- Python uses special methods (dunder methods) to implement operator behaviour. These methods are predefined in python and can be overriden in classes.

### Overloading built-in methods
- Overloading built-in methods allows us to redefine the behaviour of python's built-in functions when used with objects of custom classes. This is achieved by overriding special methods (dunder methods) in class.

*Why over-load built-in Methods*?
- Custom Behaviour
- Intiutive Use
- Enhanced Functionality

### Duck Typing in Python
- Duck Typing is a programming concept in Python where the type or class of an object is less important than the methods and properties it defines.The term originates from saying:
*"If it Looks Like a duck, swims like a duck, and quacks like a dog, then it is a dog".*

- In Python, this means that an object's suitability for a task is determined by whether it has necessary methods or attributes, rather than it's specific types.

---
## Day 9/60

### Polymorphism with inheritance (Method Overiding)

- Polymorphism with inheritance, achieved through method overiding, allows a subclass to redefine or extend the behaviour of a method defined in it's parent class. This enables objects of different classes to respond differently to the same method call.
- The method in the subclass should have the same name, parameters and return type as the one in the parent class.

### Abstraction

Abstraction is the process of hiding implementation details and exposing only the essential functionality to the user. Focues on __"What"__ an object does, not __"how"__ it does.

#### Abstraction is Achieved Through

__1. Abstract Classes:__
- Classes that act as blueprints
- Can't be instantiated directly

__2. Abstract Methods:__
- Methods that are declared but not implemented in the abstract class.
- Must be implemented by subclasses.

__3. Key Python Tools:__
- abc module (Abstract Base Class)
- @abstractmethod decorator
---

## Day 10/60

__Abstract Class__

- An abstract class is a blueprint for other classes.It defines the structure but does not provide full implementation

- Abstract classes cannot be instantiated directly. They are designed to be inherited by subclasses.

- They help enforce a contract for the derived classes to implement specific methods.

__Abstract Method__

- An abstract method is a method declared in an abstract class but without any implementation.

- It serves as a placeholder, mandating a subclasses to provide their own implementation. 

- Abstract methods are defined using the @abstractmethod decorator.
---

## Day 11/60
__Solved Abstraction Based Question__

---

## Day 12/60
### Metaclasses

The classes that generate other classes are defined as metclasses, as well as the classes that inherit directly from type.

__Now what is type?__<br>
The Exact class that is used for class instantiation is called type.

__MetaClass Usecases__
- Class Verification
- Prevent Inheriting the attributes
- Dynamic Generation of classes 
--- 

## Day 13/60

- Solved tow usecases of MetaClass i.e Prevent Inheriting the attributes and Dynamic Generation of classes 

---

##  Day 14/60

Revisiting everything I’ve learned so far in Object-Oriented Programming using Python:



###  Core OOP Concepts
- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class, with its own data and behaviors.
- **Constructor (`__init__`)**: Initializes object properties.
- **Attributes & Methods**: Define the state and behavior of objects.



### Inheritance
- Enables a class to inherit attributes and methods from another class.
- Types: Single, Multiple, Multilevel, Hierarchical, Hybrid.
- Used `super()` and method overriding to extend or modify parent behaviors.



### Encapsulation
- Bundles data and methods into one unit.
- Controlled access using:
  - Public (`name`)
  - Protected (`_name`)
  - Private (`__name`)
- Implemented getters, setters, and used `@property` for clean access control.


### Polymorphism
- Objects can behave differently based on context.
- Achieved through:
  - Method Overriding
  - Method Overloading (using `*args`, `**kwargs`)
  - Operator Overloading with dunder methods (`__add__`, `__str__`, etc.)
- Embraced Duck Typing: "If it quacks like a duck..."



### Abstraction
- Hides internal implementation and shows only what’s necessary.
- Used abstract classes and methods via `abc` module and `@abstractmethod`.



###  Metaclasses
- Built logic that runs when classes are created.
- Enforced custom rules (e.g., no class can have both `foo` and `bar`).
- Dynamically generated classes and controlled their instantiation.

---

##  Day 15/60
Since, oop in python is finished from today, i'll start learning Requests Library from python.

### Requests Libaray
The request library is the defacto standard for making HTTP Requests in Python.It abstracts the complexities of making requests behind a beautiful, simple API so that we can, focus on interacting with services and consuming data in our application.

__*Requests Library demans familarity with HTTP mehtods and Status codes so i revised them too:-*__

__HTTP Methods:__
- GET
- PUT
- POST
- HEAD
- DELETE
- OPTIONS
- PATCH

__Status Code:-__
- Information responses (`100 - 199`)
- Sucessful responses (`200-299`)
- Redirectional messages (`300-499`)
- Client Error responses (`400-499`)
- Server Error responses (`500-599`)
---
##  Day 16/60
### Covered Today:
__How to send:__
- `GET, POST, PUT, DELETE, HEAD`

__How to:__
- Send and format data
- Handle response objects: `.json(), .text, .headers, .status_code, etc.`
- Understand type handling in JSON
- Realize that fake APIs don't persist data and real one does

---
##  Day 17/60

### Covered Today:
__How to:__
- Send and format parameters using params, json, and data

- Handle response objects:
  - .json() for parsed JSON
  - .text for raw string
  - .content for byte-level data
  - .headers to inspect response metadata
  - .status_code to check response status
  - .url to view the final requested URL
---
##  Day 18/60
### Covered Today:

__How to:__
- Handle binary response content using:
  - `.raw.read()` for low-level byte reading
  - content for the entire binary payload
  - `.iter_content`(chunk_size) to stream and write large responses efficiently
- Use `stream=True` to lazily download content without loading it all into memory
- Save binary data (like images) to a file using with open("file", "wb")
- Understand the use of .raise_for_status() to trigger errors for HTTP codes like 404, 500

__Explore different ways to send POST requests:__
- As a list of tuples `([("key", "val")])`
- As a dict with multiple values for a key `({"key": ["val1", "val2"]})`

---
##  Day 19/60
### Covered Today:

__How to:__
- POST a multipart-encoded file using:
  - files = `{"file": open("myfile.txt", "rb")}`
  - Combine file with other form fields using data=...
  - Upload to a server like `https://httpbin.org/post`

__Access response headers using:__
- response.headers to view metadata like Content-Type, Server
- `response.headers.get("Some-Header")` for safe access

__Work with cookies:__
  - Read cookies from response via `response.cookies.get("cookie_name")`
  - Send cookies in requests using `cookies={"name": "value"}`
  - Use `requests.Session()` to persist cookies across multiple requests

---
##  Day 20/60

### Covered Today:

__How to:__

- Use requests.Session() to:

  - Persist cookies, headers, and authentication across multiple requests
  - Improve performance via connection reuse (connection pooling)
  - Simulate logged-in behavior like browser tabs

- Send authentication:
  - Basic Auth using `auth=("username", "password")`
  - Bearer Token via headers=`{"Authorization": "Bearer <token>"}`

- Send custom headers:
  - Use headers to pass metadata like User-Agent or API keys
  - Syntax: headers=`{"X-Custom": "value", "User-Agent": "custom-bot/1.0"}`

  ---
##  Day 21/60
### Covered Today:

__How to:__

- Handle cookies in requests:

  - Read cookies from responses using `response.cookies.get("key")`

  - Send cookies in a request using `cookies={"key": "value"}`

  - Persist cookies across requests using `requests.Session()`

- Understand redirects:

  - requests follows redirects automatically by default

  - View redirect chain using `.history`

  - Get the final destination URL via `.url`

  - Disable auto-redirects with `allow_redirects=False`
--- 
##  Day 22/60
### Covered Today:

__How to:__

- Set timeouts in requests:
  - Use timeout=value to avoid hanging requests (applies to both connect and read)
  - Use `timeout=(connect_timeout, read_timeout)` to separate connection and response wait limits
  - Timeouts can be floats (e.g., timeout=(2.5, 5.0))

- If the request exceeds the limit:

  - ConnectTimeout for delayed connection
  - ReadTimeout for delayed data
- Handle exceptions gracefully:
  - Use try/except to catch requests.exceptions.* like:
    - Timeout
    - ConnectionError
    - HTTPError
    - RequestException
---
## Day 23/60

### Covered Today:

*Goal of exception handling is not to correct the error occuring part, but to gracefully terminate the program in the case of exception.*

__Types of errors:__
- Syntax Error 
- Logical Error
- Runtime Error

__Different Type of RunTime Errors:__
- NameError
- AtrributeError
- Zero Division Error
- Index Error
- Type Error

__Structure of Exception handling:__
- try:
- except:
- else:
- finally
---
## Day 24/60

### Covered Today:

- Exception Handling
- Displaying the type of error occurred
---

## Day 25/60

### Covered Today:

__Raising Custom Explanation:__
- Following is the format of making custom exception.<br>
`class NameofException(PredefinedException):`<br>
`  def __init__(self,msg):`<br>
`   self.msg=msg` 
- We can raise exception using 'raise' keyword.

---

## Day 26/60

### Covered Today:

__Revised Rules to write *try-except-else-finally* blocks__
1. Whenever we are writing try block,compulsory we should wirte exept block or finaly blocks.<br>
i.e, try without except or finally is always invalid

2. Whenver we are writing except block, compulsory try block should be there.<br>
i.e, except without try is always invalid

3. Whenever we are writing finally block, compulsory try block should be there.<br>
i.e, finally without try is always invalid

4. Whenever we are writing else block, compulsory except block should be there.<br>
i.e, else without except is always invalid.

5. We can write multiple except blocks for same try, but we cannot write multiple else blocks and finally blocks

6. In try-except-else-finally order is important

7. We can write try-except-else-finally inside, try except, else and finally.Hence nesting of try-except-else-finally is always possible.

__Made of python program following all of the above rule__

---

## Day 27/60

### Covered Today:

__File Handling:__
It refers to the process by which data is stored and retrived from files using a program.

- __Opening & Closing a file:__
  - Opening Format: `f=open("file_name","opening mode")`
  - Closing Format: `f.close`

- __Reading file:__
  - When you open a file without metioning mode, then default mode is "read" mode.  
  - If file exist, it opens file in read mode, otherwise generate error

- __Writing to the file:__
  - When opening file in write mode, opens file if file exists, otherwise create and open a new file.
  - Write mode overwrites the previous contetns of the file

- __Append to the file:__
  - `append()` adds new content to the file. It does not overwrite old contents

---
## Day 28/60

### Covered Today:

- __writelines() method:__<br>
writeline() method is use to write lists to the file.Contents of lists are stored as the string.

- __Reading from file:__<br>
  - `.read()` reads all the contents of the file.

- __readline():__<br>
  - Reads first/single line
  - If two readline() are used. It reads firsts and second line, no need to write consecutively.

- __tell(),read(n):__
  - tell() gives current position of the file object
  - read(n) reads 'n' characters of the starting from current file position.

---
## Day 29/60

### Covered Today:

- __Loop in file:__
  - Reads one line at a time

- __Check if file exists or not:__
  - We need to import os module

- __Removing a file:__
  - Need to use os module: `os.remove(file_name)`

---

## Day 30/60

### Covered Today:

Revised everything learned about file handling and written a code including those concepts.
---
## Day 31/60

### Covered Today:

- **Session Object Basics:**
  - Maintains parameters like headers, auth, and cookies across multiple requests
  - Reuses TCP connections for better performance (connection pooling)

- **Persisting Cookies:**
  - Cookies set during a session are remembered and sent automatically
  - Example: `s.get('https://httpbin.org/cookies/set/name/value')`

- **Setting Default Parameters:**
  - Use `s.headers.update()` to set default headers
  - Use `s.auth = ('user', 'pass')` to persist authentication across requests

- **Overriding Session Parameters:**
  - Request-specific parameters override session-level values
  - Method-level values (like headers or cookies) are not saved between requests

- **Manually Managing Cookies:**
  - Use `RequestsCookieJar()` to create and assign cookies manually
  - Example: `s.cookies = jar` after setting values in the jar

- **Using Session as Context Manager:**
  - Ensures session is automatically closed with `with requests.Session() as s: ...`

---
## Day 32/60

### Covered Today:
- **Request & Response Objects:**
  - `requests.get()` creates a Request and returns a Response

- **Inspecting Responses:**
  - `r.headers`-- server’s response headers
  - `r.text` / `r.json()`--response content

- **Inspecting What You Sent:**
  - `r.request.headers`--headers your script sent

- **Use Case:**
  - Helpful for debugging, API testing, and understanding server-client interactions

---
## Day 33/60

### Covered Today:

- **Prepared Requests:**
  - Built using `Request` + `Session.prepare_request()`
  - Gives full control over headers, body, and timing

- **When to use `merge_environment_settings()`:**
  - Only needed for:
    - Self-signed SSL certs
    - Proxies from environment
    - Streaming, timeouts, client certs

  - Not needed for:
    - Normal HTTPS websites with public certs
    - When no proxies or special settings are used
---

## Day 34/60
### Covered Today:

__SSL Certificate Verification:__

- requests verifies HTTPS certs by default
- Fails if:
  - Cert is self-signed
  - Hostname doesn’t match
- Fix options:
  - Use `verify='/path/to/ca.pem'`
  - Set `REQUESTS_CA_BUNDLE` env var
  - Use `verify=False` (testing only — insecure)
---

## Day 35/60

### Covered Today:
**Client & CA Certificates**

- **Client Certificates:**
  - Use `cert=(cert_path, key_path)` or a single bundle file
  - Must be **unencrypted**
  - Can be set in a `Session`
  - Wrong path = `SSLError`

- **CA Certificates:**
  - Used to verify the server’s identity
  - `requests` relies on `certifi`
  - Keep `certifi` updated for security:
    ```bash
    pip install --upgrade certifi
    ```
---
## Day 36/60
### Covered Today:

__Body Content Workflow in requests__

- **By default**, full response body is downloaded immediately.
- Use `stream=True` to defer downloading until needed.
  ```python
  r = requests.get(url, stream=True)
