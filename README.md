# Car Hire System

## Table of contents
* [Introduction](#introduction)
* [Project Tracking](#project-tracking)
* [Diagrams](#diagrams)
* [Risk Assessment](#risk-assessment)
* [Design](#design)
* [Tools and Technologies](#tools-and-technologies)
* [Acceptance Criteria](#acceptance-criteria)
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

## Tools and Technologies

technologies used

## Acceptance Criteria

Set of statements that usually have a pass/fail result for requirements

## Testing

Pytest, specifically Unit testing, has been used to test the code produced in this project. Selenium was planned to be used for Integration testing however it was not fully implemented and therefore not included at this time.

### Analysis

Through Unit testing, a coverage of 90% was acheived. To push this to 100%, further tests could have been made that tested if redirects had successfuly occured in each function.

## Improvements for future

a sort of final conclusion, say what went well but could have been improved or what can still be added.


[trello-link]: https://trello.com/b/VTXiegA8/car-hire-system-qac
[trello-sc-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/Trello.png
[erd-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/ERD%20Diagram.png
[erd2-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/ERD%20Diagram%20v2.png
[ra-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/risk%20assessment%20pic.png
[pb-link]: https://github.com/HamzaYacub/QAC-Fundamental-Project/blob/master/Documentation/product%20backlog.png
