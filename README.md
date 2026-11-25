# AirBnB Clone - The Console

## Description

This project is a command-line application that replicates some of the
basic functionality of the AirBnB website. It allows users to create,
view, update, and delete objects representing users, places, cities,
states, amenities, and reviews.

The project is built using Python and uses JSON file storage to
persist data between sessions.

## Command Interpreter

The command interpreter allows users to manage objects through a
command-line interface.

### How to start it

Clone the repository and enter the project directory:

    git clone <repository_url>
    cd alche-AirBnB_clone

Start the console:

    ./console.py

### Available commands

| Command | Description |
|---|---|
| `help` | Display available commands |
| `quit` | Exit the console |
| `EOF` | Exit the console |
| `create <class>` | Create a new instance |
| `show <class> <id>` | Display an instance |
| `destroy <class> <id>` | Delete an instance |
| `all [class]` | Display all instances |
| `update <class> <id> <attribute> <value>` | Update an instance |

### Examples

Create a User:

    (hbnb) create User

Display all User instances:

    (hbnb) all User

Count User instances:

    (hbnb) User.count()

## Supported Classes

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## Storage

The application uses a JSON file (`file.json`) to store objects.
Data is loaded when the console starts and saved when objects are
created, updated, or deleted.

## Technologies

- Python 3
- JSON
- Unittest
- Pycodestyle
