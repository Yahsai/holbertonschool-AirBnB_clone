# Holbertonschool-AirBnB_clone

## AirBnB Clone - The Console

This project aims to create an Airbnb clone with a console interface. The console allows users to interact with the application, create and manage instances of BaseModel, and store/retrieve data using JSON serialization.

---

## Table of Contents

1. Requirements
2. Installation
3. Usage
4. Console Commands
5. Unit Tests
6. File Storage
7. User Class
8. Console 1.0
9. Authors
10. Contributing

---

## Requirements

    - Python 3.8.5
    - Ubuntu 20.04 LTS
    - pycodestyle 2.7.*
    - unittest module

---

## Installation 

1. Clon the repository:
git clone https://github.com/your-username/airbnb-clone-console.git

2. Navigate to the project folder:
 cd airbnb-clone-console

3. Make sure to have pycodestyle folder:
pip install pycodestyle

4. Run the console: 
./console.py

---

## Usage 

The console has been updated to include new commands for creating, showing, destroying, updating, and listing instances of various classes.

### Console Commands

    - create <class name>: Creates a new instance of the specified class (e.g., create BaseModel).
        If the class name is missing, print ** class name missing **.
        If the class name doesn’t exist, print ** class doesn't exist **.
    - show <class name> <id>: Prints the string representation of an instance based on the class name and id (e.g., show - BaseModel 1234-1234-1234).
        If the class name is missing, print ** class name missing **.
        If the class name doesn’t exist, print ** class doesn't exist **.
        If the id is missing, print ** instance id missing **.
        If the instance doesn’t exist for the id, print ** no instance found **.
    - destroy <class name> <id>: Deletes an instance based on the class name and id.
        If the class name is missing, print ** class name missing **.
        If the class name doesn’t exist, print ** class doesn't exist **.
        If the id is missing, print ** instance id missing **.
        If the instance doesn’t exist for the id, print ** no instance found **.
    - all [<class name>]: Prints string representations of all instances based on the class name (optional).
        If the class name doesn’t exist, print ** class doesn't exist **.
    - update <class name> <id> <attribute name> "<attribute value>": Updates an instance based on the class name, id, attribute name, and attribute value.
        If the class name is missing, print ** class name missing **.
        If the class name doesn’t exist, print ** class doesn't exist **.
        If the id is missing, print ** instance id missing **.
        If the instance doesn’t exist for the id, print ** no instance found **.
        If the attribute name is missing, print ** attribute name missing **.
        If the attribute value is missing, print ** value missing **.
        Only one attribute can be updated at a time.
        Only “simple” arguments can be updated: string, integer, and float.

---

## Non-interactive Mode

The console supports non-interactive mode for scripted operations.

### Example:

$ echo "create BaseModel" | ./console.py
(hbnb) 28bfb967-520c-4c2b-8f65-06ad098cfbea

---

## Unit Tests

- To run unit tests, use the following command:

python3 -m unittest discover tests

- You can also test file by file:

python3 -m unittest tests/test_models/test_base_model.py

---

## File Storage

The project includes a FileStorage class for serializing instances to a JSON file and deserializing JSON files to instances. FileStorage has been updated to manage serialization and deserialization for all new classes.

---


## User Class

A new class User has been added, inheriting from BaseModel. It has public class attributes: email, password, first_name, and last_name.

---

## More Classes

The following classes have been added, all inheriting from BaseModel:

    - State (models/state.py):
        Public class attributes: name (string).

    - City (models/city.py):
        Public class attributes: state_id (string), name (string).

    - Amenity (models/amenity.py):
        Public class attributes: name (string).

    - Place (models/place.py):
        Public class attributes: city_id (string), user_id (string), name (string), description (string), number_rooms (integer), number_bathrooms (integer), max_guest (integer), price_by_night (integer), latitude (float), longitude (float), amenity_ids (list of string).

    - Review (models/review.py):
        Public class attributes: place_id (string), user_id (string), text (string).

---


## Console 1.0

FileStorage has been updated to manage serialization and deserialization of all new classes: Place, State, City, Amenity, and Review. The console has been modified to allow actions (create, show, destroy, update, and all) with all classes created.

---

## Authors

    - Yahsai Santana
    - Lyan Osorio

---


## Contributing

Contributions are welcome! Please follow the project's coding style and guidelines. If you find any issues or have suggestions, feel free to open an issue.