# Car Hire System

## Table of contents
* [Introduction](#introduction)
* [Project Tracking](#project-tracking)
* [Diagrams](#diagrams)
* [Risk Assessment](#risk-assessment)
* [Design](#design)
* [Deployment](#deployment)
* [Testing](#testing)
* [Improvements for future](#improvements-for-future)

## Introduction

The overall objective of this project was to create a CRUD application with utilisation of supporting tools,methodologies and technologies that encapsulate all core modules that are covered during training. These core modules include: 

* Project Management 
* Python Fundamentals 
* Python Testing 
* Git 
* Basic Linux 
* Python Web Development 
* Continuous Integration 
* Cloud Fundamentals 
* Databases


As I had full control over the topic of this project, I decided to create a car hire system that would allow a user to select a car to rent from a list of available vehicles.

## Project Tracking

A [Trello][trello-link] board was used to organise this project of all of its respective requirements and tasks.

![Trello sc][trello-sc-link]

## Diagrams

This was the initial design of the entity-relationship model which highlights the components and the relationships between the tables.

![ERD][erd-link]

However after careful consideration and a look at the requirements, it was clear that a customers table was not necessary and doing so could cause the risk of gold-plating which is mentioned later in the risk assessment.

![ERD2][erd2-link]

This updated ERD only shows the relationship between 2 tables rather than 3 as is mentioned in the brief.  


## Risk Assessment

![Risk Assessment][ra-link]

## Design

show screenshots of project, explain how each feature in design addresses the functional requirements

## Deployment

show diagram of tools working together

### Tools and Technologies

* Python3 - Logic
* Flask - Web development framework
* Jinja2 - Web template for Python
* WTforms - Forms rendering framework for web development
* Jenkins - CI server
* GUnicorn - Production server
* MySQL - Database
* Pytest - Unit testing
* Git - Version control system
* Trello - Project tracking
* Google cloud platform - Live environment

## Testing

Pytest, specifically Unit testing, has been used to test the code produced in this project. Selenium was planned to be used for Integration testing however it was not fully implemented and therefore not included at this time.

### Analysis

Through Unit testing, a coverage of 90% was acheived. To push this to 100%, further tests could have been made that tested if redirects had successfuly occured in each function.

## Improvements for future

Initially, it was planned to have a login system consisting of a customer and an admin. The admin would have most control over the application. They would have access to add a car and make the rental for the customer; while the user would only be able to sign up and view the cars available.

To acheive this: 

* Another table would have to included which would have a one-many relationship with the rentals table. 
* Register and login pages would have to be made.
* Some if-statements with the jinja2 logic within the .html forms to check which user is active and then give the options to which pages they can access.

[trello-link]: https://trello.com/b/VTXiegA8/car-hire-system-qac
[trello-sc-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/Trello.png
[erd-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/ERD%20Diagram.png
[erd2-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/ERD%20Diagram%20v2.png
[ra-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/risk%20assessment%20pic.png
[pb-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/product%20backlog.png
[add-car]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/screenshots/Add%20car.png
[rent-car]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/screenshots/Rent%20car.png
[rental-history]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/screenshots/Rental%20history.png
[update-car]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/screenshots/Update%20car%20info.png
[update-rental]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/screenshots/Update%20rental%20info.png
[home]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/screenshots/home.png
