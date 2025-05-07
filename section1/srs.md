# Software Requirements Specification - Little Library Tracker
**Table of Contents**  
placeholder

## 1. Introduction
### Purpose
The purpose of this document is to provide solution requirements for a little library tracking system.
### Problem Definition
Little libraries are small, outdoor structures used in community settings (i.e., neighborhoods) to allow and expand access to books for the public. Little libraries are often purpose-built to encourage community building, access to information which might otherwise be restricted, promoting specific concepts/ideas, promoting reading, expanding access in underserved areas, and more. However, due to the emphasis on a low barrier to entry, there is limited surveillance and controls to monitor the effectiveness of little libraries, particularly if they are not registered.

Our problem considers the following use case: A little library is installed in a neighborhood shopping district by a group of store owners/renters (“the board”). They would like to track how many books are donated, borrowed, taken, or replaced. Additionally, they would like to promote the library by publishing a daily list of books to a public website. By monitoring the usage of the library, they can make other strategic decisions on what kind of books to donate, how much money to donate to maintenance, and possibly adding another community amenity.

### System Solution
The little library tracking system utilizes a database and API-client to manage the library inventory. It also regularly publishes a list of book titles to a website. Last, the system notifies the board if capacity is full or is less than 25%. A board member performs daily checks on the library to verify and update the database.

## 2. Concept
The Little Library Tracker is a web-based, object-oriented and domain-driven system that manages the library inventory, sends notifications, and publishes daily library inventory to a public website. There are three major components:
- Inventory database with API-client interaction
- Scheduled jobs
- Website

The goals of this system are:
- Manage the library inventory
- Notify board members when the library capacity is either at-limit or under-utilized
- Allow the public to see current inventory

## 3. Requirements Statements
placeholder

## 4. Specifications
Activity Diagram  
![Activity diagram for steward daily inventory routine](/section1/activity1.png)

Class Diagram  
![Class diagram for Book and Catalog classes](/section1/class1.png)

Sequence Diagram  
![Sequence diagram for steward daily inventory routine](/section1/sequence1.png)

Component Diagram  
![Component diagram for little library system overview](/section1/component.png)
