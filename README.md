# CIDM6330 Final Project - Little Library Tracker
This repository (repo) contains project requirements, descriptions, and code documentation for the SP25 CIDM 6330 final project.

## Project Requirements
Copied from Dr. Babb's Final Project description:

>#### Evolution 0: Domain Specification and UML Modeling
>
>You are required to update or choose an alternative to the problem domain from this assignment to specify a problem with which you can demonstrate a propotype solution based on the remaning Evolutions
>
>You must specifiy a UML Design including the following UML diagrams (at a minimum):
>
> - Activity Diagram
> - Class Diagram
> - Component Diagram (for your architecture)
> - Sequence Diagram
> - State Machine Diagram
> - Use Case Diagram
>#### Evolution 1: An updated Requirements  Specification
> - This should more clearly articulate your problem specification and organize the solution
> - You know more now about Python/Django so you can update your per-feature diagrams alluded to above
>#### Evolution 2: An updated API
> - You may use the Django REST Framwork or Django Ninja
> - Update your ERD as we used it to validate our entities which will be expressed using Pydantic for Django Ninja and/or DRF and the Django O/RM
> - Update CRUD transactions as necessary
>#### Evolution 3: Skipping
> - This Evolution became irrelevant once we went to a monolith like Djanog with its O/RM - all repository variations are dropped as the O/RM works differently
>#### Evolution 4: Migrate to Django
> - Ensure the proper models, views, and urls are in place
> - Migrate from FastAPI to Django Rest Framework (DRF) or Django Ninja
>#### Evolution 5: Full Django + Tests
> - For DDD create a ubiquitous language glossary: https://thedomaindrivendesign.io/developing-the-ubiquitous-language/)
> - For BDD create A Gherkin Notation expression for each test: https://cucumber.io/docs/gherkin/)
> - For TDD create tests that correspond with your Gherkin Statements.
With these you will create Django unittests that demonstrates three Use Cases of your system.

### Interpreted Requirements
#### Evolution 0 & 1: Domain Specification and UML Modeling
Develop a requirements specification document to solve a problem using domain-driven design principals.
- [ ] Develop a requirements specification document in markdown with the following elements:
    - [ ] Activity Diagram
    - [ ] Class Diagram
    - [ ] Component Diagram
    - [ ] Sequence Diagram
    - [ ] State Machine Diagram
    - [ ] Use Case Diagram

#### Evolution 2: Basic API
- [ ] Create a class-based ERD in markdown
- [ ] Create a basic API using FastAPI with the following elements:
    - [ ] Pydantic models
    - [ ] CRUD functions

#### Evolution 3 & 4: Django API
- [ ] Migrate the Basic API to Django Rest Framework or Django Ninja

#### Evolution 5: Implement Tests
- [ ] Create Gerkin Notation expression tests
- [ ] Create Django unittests that demonstrate three use cases from the Gerkin statements

## Repo Structure
To fulfil the project requirements, this repo is split into three sections.

#### Section 1: Requirements Documentation
Section 1 (`` /section1 ``) contains the requirements document from Evoluation 0/1, ERD from Evolution 2, and Gerkin notation tests from Evolution 5.

#### Section 2: Basic API
To ensure clarity and separation between the Basic API and the graduated API in Django, section 2 (`` /section2 ``) contains all code for Evolution 2. The ERD in ``/section1`` is used to validate the pydantic models.

#### Section 3: Django API
Section 3 (`` /section3 ``) contains all code related to Evolutions 3-5. The Gerkin notation tests in ``/section1`` is used to implement the Django unittests.