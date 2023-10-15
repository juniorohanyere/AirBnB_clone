# Airbnb Clone.

## Description.

This is a console for a clone of the [Aribnb website](https://airbnb.com). It forms the basis of the structure of the website to be cloned
Operations are however carried out from a `command line interface`.

## Description of the Command Interpreter.

- **starting the interpreter:**

```bash
./console.py
```

- **usage:**

```bash
(hbnb) # the help command displays a list of supported commands
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF all count create destroy help quit show update

(hbnb) help create  # displays the docstring for create command
Creates a new instance of a class, savves it and prints the id

(hbnb) EOF  # exits the command interpreter, same as quit and ctrl-D
```
*the command `all` displays all the models created*

```bash
(hbnb) all
[BaseModel] (8ccb3be8-7a61-47e0-ba1e-63a22da2190d) {'id': '8ccb3be8-7a61-47e0-ba1e-63a22da2190d', 'created_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 953124), 'updated_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 953124)}
[BaseModel] (3d746ba5-f322-46c3-a80b-be7465bd19c5) {'id': '3d746ba5-f322-46c3-a80b-be7465bd19c5', 'created_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 953405), 'updated_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 953405)}
[BaseModel] (02e4846b-d644-47ab-8c12-ddb581215f18) {'id': '02e4846b-d644-47ab-8c12-ddb581215f18', 'created_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 953716), 'updated_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 953716), 'name': 'My First Model', 'number': 89}
[BaseModel] (f3fe3fa2-5036-4330-b6b1-a889f4e3ed7c) {'id': 'f3fe3fa2-5036-4330-b6b1-a889f4e3ed7c', 'created_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 956051), 'updated_at': datetime.datetime(2023, 10, 15, 9, 3, 56, 956084)}
[Amenity] (81cbbc1a-12ab-427f-a039-6a5fb963d562) {'id': '81cbbc1a-12ab-427f-a039-6a5fb963d562', 'created_at': datetime.datetime(2023, 10, 15, 9, 4, 42, 82562), 'updated_at': datetime.datetime(2023, 10, 15, 9, 4, 42, 82562)}
[Amenity] (fcc2b117-62b8-47f5-b1d0-24c21ecc0efd) {'id': 'fcc2b117-62b8-47f5-b1d0-24c21ecc0efd', 'created_at': datetime.datetime(2023, 10, 15, 9, 4, 42, 82715), 'updated_at': datetime.datetime(2023, 10, 15, 9, 4, 42, 82715)}
```
