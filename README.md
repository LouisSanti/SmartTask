SmartTask

## Project description
SmartTask is a simple but scalable task management application built using Python. It allows users to create, update, delete, filter, and categorize tasks. The project demonstrates clean architecture using design patterns and includes unit testing for reliability.

## Features
- Add, edit, delete tasks
- Mark tasks as completed
- Categorize tasks (School, Work, Personal)
- Filter tasks by status or category
- Save and load tasks using interchangeable storage modules
- Unit tests for all major components

## Design Patterns Used
- Factory Pattern → Creates storage type (JSON or Memory)
- Strategy Pattern → Interchangeable storage system
- Separation of Concerns → Models, Services, Storage layers

## Project Structure
- factory/
- model/
- service/
- storage/
- test/
- main.py

## How to run
1. Install Python (3.8+ recommended)
2. Run program: python main.py
3. Run tests: python -m unittest discover tests
