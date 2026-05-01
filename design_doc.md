SmartTask Design Document

## Overview
SmartTask is a task management system designed using object-oriented programming principles and software design patterns. The system is structured to ensure modularity, scalability, and testability.

## Design Patterns Used

1. Factory Pattern
Used in `StorageFactory` to create different storage types (JSON or Memory). This allows flexibility in switching storage without changing business logic.

2. Strategy Pattern
Implemented through `StorageInterface`, allowing interchangeable storage implementations.

3. Separation of Concerns
The project is divided into:
- Models (data structure)
- Services (business logic)
- Storage (data persistence)
- Factory (object creation)

## System Architecture
The system follows a layered architecture:
- Presentation Layer → main.py (user interaction)
- Service Layer → TaskService (business logic)
- Model Layer → Task class (data structure)
- Storage Layer → JSONStorage / MemoryStorage

## Unit Testing Strategy
Unit tests are written using Python’s `unittest` module.
Tests cover:
- Adding tasks
- Deleting tasks
- Completing tasks
- Filtering tasks

Data Flow
1. User interacts via CLI (`main.py`)
2. Input is passed to `TaskService`
3. Task objects are created/updated
4. Storage layer saves/loads data
5. Output is displayed back to user

Future Improvements
- Add GUI (Tkinter or Web UI)
- Add due dates and reminders
- Use SQLite instead of JSON
