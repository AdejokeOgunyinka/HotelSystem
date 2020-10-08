# Hotel System

This is a system to be used by a manager to help customers in booking hotel rooms that are available on the system. The system has to be setup with necessary information by an administrator before the manager can actually use the system.

### Users

* Administrator
* Manager

### Functionalities

* Administrator should be able to register hotels onto the system
* Administrator should be able to add room details for an existing hotel
* Manager should be able to get complete information of a room
* Manager should be able to book a room for a customer

# Deliverables

* Build out the database module that will backup our system as a datastore
* Build out the system models to be used in representing data on the system as objects
* Build out the actual system that uses the database and models perform required activities

# General Notes

* Comments has been added into the codebase to specify the requirements for implementations
* Ensure to understand the context and deliverables of the system before starting to write any code

# Building The Database

The database is simply a class that have references to table objects, of which these objects can individually be used to query the table for data and select data out of the tables. The supported database tables are (1) Rooms (2) Hotels (3) Bookings

Data are represented at this level as dictionaries. Below are examples of records we can have in the respective tables in the database

```python

#### Hotel Record ####

{
  '_id': 1,
  'name': 'Julian Hotel',
}

#### Room Record ####

{
  '_id': 1,
  'hotel_id': 2,
  'price': 1000,
  'capacity': 5,
}

#### Booking Record ####

{
  '_id': '5,
  'room_id': 1,
  'name': 'John Doe',
  'paid': False,
}

```

**Go through the checklist below to implement the database module**

* Checkout the `__init__.py` file in the database folder to see how tables have been created as objects from the `Table` class
* Head over to the `table.py` file in the database folder to see the expected methods needed to be completed and use later for sending queries to a table
* Use the requirements(comments) to complete the implementation of the methods in the `table.py` file

**Note:**
Going forward, you will be relying so much on the interface(attributes + methods) provided by the database module, so it is important for you to understand how to use the interface very well before proceeding

# Building The Models

The models are classes with fields already defined on them as attributes, of which these fields maps directly to fields defined for table objects in the database class.

The purpose of models in this system, is to present a different representation of records from the database instead of rely on dictionaries in the system. This way, we can get values of record by attributes instead of dictionary keys

Head over to the `model.py` file in the models folder that defines a base class for all other models in the folder. Also, notice the following
* The use of `@classmethod` to make the `create` method a class method as opposed to been an instance method
* How the model base class has been imported into other model classes
* How model classes names are `singular` as opposed to tables in the Database class that are `pluralized`
* Existence of other methods different from `create` in the `room.py` & `booking.py` model files. Those methods has been used to define association between tables. Meaning that from the room model, we will be able to get the hotel record that the room belongs to. This is also true for booking model where the room method is used to get room record the booking was made for

**Go through the checklist below to implement the models modules**

* Checkout the `hotel.py` model file in the models folder and use the requirements to complete the implementation for the `create` class method
* Checkout the `room.py` model file in the models folder and use the requirements to complete the implementation for the `create` class method & `hotel` instance method
* Checkout the `booking.py` model file in the models folder and use the requirements to complete the implementation for the `create` class method & `room` instance method

# Building The System

This is the interface(attributes + methods) the administrator and the manage will rely on as the core functionalities (database & models) have been abstracted away from them

**Go through the checklist below to implement the hotel system module**

* Checkout the `hotel_system.py` file at the root of the project and use the requirements to complete the implementation for each of the methods in there

# Running Tests 

```bash

# Head over to your terminal and type in the following commands
# Failing tests means loosing points

User Prompt> cd <project-folder-root>

User Prompt> python -m unittest

```

# Refelection & Analysis

It is assumed that by the time you get here, all your tests are passing and all expected implementations are complete. So here, you are expected to go through the whole project again to reflect and try to get better understanding of the whole flow.

After the above, open up the `ANALYSIS.md` file and document what you think and understand about the following

* What are the different OOP patterns you noticed was used in the codebase?
* What are the different design patterns you noticed was used in the codebase?
* What are the bootlenecks you identified and think we can erradicate to make the system better(In terms of performance, coding styles and codebase structure)?