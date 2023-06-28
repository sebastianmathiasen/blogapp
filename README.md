
# Blog App

Blog App is a desktop application built with Python that allows users to manage blog entries. It's an ideal tool for learning and showcasing fundamental concepts of object-oriented programming, databases, and the creation of user interfaces in Python.

## Project Description 

The Blog App project has been developed for presentation in a university setting as practice and demonstration of Python programming skills, use of databases with SQLite, and user interface design with Tkinter.
This project is a practical example of how data can be created, read, updated, and deleted from a database (also known as CRUD operations). It also provides a graphical user interface (GUI) to interact with the data.
Additionally, the Blog App serves to illustrate the Model-View-Controller (MVC) architecture. In this design pattern, the "View" is the user interface, the "Model" is the database, and the "Controller" is the application logic that coordinates the View and the Model.


## Features

    1. Create new blog entries: Fill in the "Blog Title", "Blog Content", and "Email" fields. Then press the "Submit" button to save the entry. Make sure to enter a valid email address.
    2. Consult existing entries: Select a row in the entries table and press the "Consult" button. The details of the selected entry will be displayed in the input fields.
    3. Modify existing entries: First, select and consult the entry you want to modify. Then make the necessary changes in the input fields and press the "Modify" button.
    4. Delete existing entries: Select the entry in the table that you want to delete and press the "Delete" button.


## Usage

To use the application, run the Python script in your terminal:

```bash
  python blog_app.py
```

A window will open with controls to create, consult, modify, and delete blog entries. The top table displays all existing blog entries in the database.
## System Requirements

    • Python 3
    • SQLite3
    • Tkinter
You can install Tkinter using pip:

```bash
  pip install tk
```
SQLite comes pre-installed with Python.

## File Structure

This project consists of a single Python file:

    • blog_app.py: This is the main script which contains the model (database management), the view (user interface), and the controller (application logic).


## Final Considerations 

Although this application is simple, it illustrates several important concepts of programming and software development, making it an excellent project to present in an educational environment. By understanding and building an application like this, students can gain practical understanding of how software applications work and how they can be built using Python.

