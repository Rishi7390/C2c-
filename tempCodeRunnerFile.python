from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# PDF file name
pdf_file = "Python_Programming_Ebook.pdf"

# Create document template
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Ebook content
content = [
    ("Chapter 1 – Introduction to Python", """
- History of Python
- Features of Python (simple, interpreted, portable, extensible, open-source, high-level)
- Applications: Web, Data Science, AI, Automation, Cybersecurity, etc.
- Installing Python (Windows/Linux/Mac)
- First Python Program:
    print("Hello, World!")
    """),
    ("Chapter 2 – Python Basics", """
- Variables, Data Types (int, float, str, bool, complex)
- Type Casting & type() function
- Operators: Arithmetic, Relational, Logical, Assignment, Bitwise
- Input/Output functions: input(), print()
- Example:
    a = int(input("Enter number: "))
    print("Square:", a**2)
    """),
    ("Chapter 3 – Control Structures", """
- Conditional Statements: if, if-else, if-elif-else
- Loops: for, while
- break, continue, pass
- Example:
    for i in range(1,6):
        if i == 3:
            continue
        print(i)
    """),
    ("Chapter 4 – Functions", """
- Defining functions using def
- Function arguments (default, keyword, variable-length *args, **kwargs)
- Return values
- Lambda functions
- Recursion
- Example:
    def factorial(n):
        return 1 if n==0 else n*factorial(n-1)
    print(factorial(5))
    """),
    ("Chapter 5 – Data Structures", """
- List (mutable, ordered)
- Tuple (immutable, ordered)
- Set (unique, unordered)
- Dictionary (key-value mapping)
- Comprehensions: List, Dict, Set
- Example:
    squares = [x*x for x in range(1,6)]
    print(squares)  # [1, 4, 9, 16, 25]
    """),
    ("Chapter 6 – Strings in Python", """
- String creation, slicing, indexing
- String methods (upper(), lower(), find(), split(), join())
- String formatting: f-strings, format()
- Example:
    name = "Rishi"
    print(f"Hello, {name.upper()}")
    """),
    ("Chapter 7 – File Handling", """
- Reading and writing text files (open, read, write, with)
- Working with CSV using csv module
- Example:
    with open("data.txt", "w") as f:
        f.write("Hello File!")
    """),
    ("Chapter 8 – Object-Oriented Programming", """
- Classes and Objects
- __init__ constructor
- Inheritance (single, multiple, multilevel)
- Encapsulation, Polymorphism
- Example:
    class Animal:
        def sound(self):
            print("Some sound")
    class Dog(Animal):
        def sound(self):
            print("Bark")
    Dog().sound()
    """),
    ("Chapter 9 – Modules & Packages", """
- Importing modules (math, os, sys)
- Creating user-defined modules
- Installing external packages with pip
- Example:
    import math
    print(math.sqrt(25))
    """),
    ("Chapter 10 – Exception Handling", """
- Errors vs Exceptions
- try, except, finally, raise
- Example:
    try:
        num = int("abc")
    except ValueError:
        print("Invalid number")
    """),
    ("Chapter 11 – Python Advanced Concepts", """
- Iterators and Generators (yield)
- Decorators (@decorator)
- Context Managers (with)
- Regular Expressions (re module)
- Example:
    def gen():
        for i in range(3):
            yield i
    for x in gen():
        print(x)
    """),
    ("Chapter 12 – Python Libraries", """
- NumPy: Arrays, matrix operations
- Pandas: DataFrames, data analysis
- Matplotlib: Data visualization
- Requests: Web API calls
- BeautifulSoup: Web scraping
    """),
    ("Chapter 13 – Python for Automation", """
- Automating files with os & shutil
- Automating emails with smtplib
- Web scraping automation
- Example:
    import os
    print(os.listdir("."))
    """),
    ("Chapter 14 – Python for Web Development", """
- Flask / Django basics
- Routing, templates, simple web apps
    """),
    ("Chapter 15 – Python for Data Science & AI", """
- NumPy + Pandas (data manipulation)
- Matplotlib + Seaborn (data visualization)
- Scikit-learn (machine learning intro)
    """),
    ("Chapter 16 – Python in Cybersecurity", """
- Password hashing (hashlib)
- Simple port scanner using socket
    """),
    ("Chapter 17 – Projects", """
1. Calculator GUI (Tkinter)
2. To-Do List App
3. Weather App using API
4. Student Database using SQLite
5. Web Scraper for News
    """),
    ("Chapter 18 – Interview Questions", """
- Difference between list and tuple
- What is GIL in Python?
- Shallow vs Deep copy
- How memory management works in Python?
- Example coding questions:
  - Reverse a string
  - Find factorial
  - Sort dictionary by values
    """),
    ("Chapter 19 – Exercises", """
- 100+ practice problems with increasing difficulty
    """),
    ("Chapter 20 – Roadmap", """
- Start with basics → Practice problems
- Learn libraries (NumPy, Pandas, Matplotlib)
- Do projects → Apply for internships → Freelancing/Jobs
    """)
]

# Add content to PDF
for title, text in content:
    story.append(Paragraph(title, styles['Heading2']))
    story.append(Paragraph(text.strip().replace("\n", "<br/>"), styles['Normal']))
    story.append(Spacer(1, 12))

# Build PDF
doc.build(story)

print(f"E-book created successfully: {pdf_file}")
