
# Library Management System

## About the Project

I built this Library Management System using Python to practise Object-Oriented Programming.

The application helps manage books and student records. It allows users to add books, register students, issue books and return them through a simple menu-driven interface.

I used classes and inheritance to organise the code and custom exceptions to handle situations such as issuing an unavailable book or entering an invalid book ID.

The application also uses JSON file handling to save library data, so records remain available when the program is restarted.

## Features

- Add new books to the library.
- Register students as library members.
- Display all available and issued books.
- Issue books to registered students.
- Return previously issued books.
- Handle errors using custom exceptions.
- Save and load records using a JSON file.

## Concepts Practised

- Classes and Objects
- Constructors (`__init__`)
- Inheritance
- Method Overriding
- `super()` function
- Encapsulation
- Custom Exceptions
- Try and Except
- JSON File Handling

## Technologies Used

- Python
- JSON
- Object-Oriented Programming

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Activate the virtual environment.
4. Run the following command:

```bash
python library.py
```

5. Follow the menu displayed in the terminal.

## Project Structure

```text
week2_library_management/
│
├── library.py
├── library_data.json
├── README.md
└── .gitignore
```

## What I Learned

While building this project, I got practical experience with Python OOP concepts. I understood how inheritance helps reuse code, how custom exceptions handle errors, and how JSON files can be used to store application data.

## Project Status

Completed as part of my Week 2 Python practice tasks.
