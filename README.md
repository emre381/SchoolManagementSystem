


# School Management System

## Overview
This Python project simulates a **School Management System** with two different user roles: **Teacher** and **Director**. The system allows users to perform various operations depending on their role, such as viewing and editing information about branches, departments, and teachers.

### Features:
- **Teacher Panel**:
  - View branch, teacher, department, and student availability.
  - Change department (restricted to teachers).
  
- **Director Panel**:
  - Full access to view and edit the branch, teacher, and department information.
  - Change the teacher assigned to a branch.
  - Change the branch name.
  - Change the department.
  
## How It Works
When you run the program, you will be prompted to choose your role: either `teacher` or `director`. Based on the role you select, you will be taken to the corresponding panel with access to different functions.

### Teacher Panel
- Teachers can view information about the current branch, teacher, department, and available students.
- Teachers can only change the department.
- The panel runs in a loop, allowing repeated changes until the user exits.

### Director Panel
- Directors have full control over the information. They can:
  - Change the department.
  - Change the teacher assigned to a branch.
  - Change the branch name.
- The panel provides multiple options for modification and remains active until the user chooses to exit.

## Installation
1. Clone or download the repository:
   ```bash
   git clone <repository-url>
   ```

2. Ensure you have Python installed (version 3.6 or later).

3. Run the Python script:
   ```bash
   python school_management.py
   ```

## Usage

1. **Run the Script**: Start the program by running the Python script.
   ```bash
   python school_management.py
   ```

2. **Select Role**: You will be prompted to enter your role as either a `teacher` or `director`.
   
3. **Follow Prompts**: Based on your role:
   - If you are a `teacher`, you can change the department.
   - If you are a `director`, you can change the branch, teacher, and department.

4. **Exit**: You can exit the panels anytime by choosing the "Exit" option in the menus.

## Example

```bash
Enter your role (teacher/director): director
Welcome to the director panel.
Branch: 11
Teacher: Emre
Department: Tech
Available Students: 55
Title: CTO
---------------------------------------------
1. Change Department
2. Change Teacher
3. Change Branch
4. Exit
Please choose an option: 1
Please enter the new department: Science
Branch: 11
Teacher: Emre
Department: Science
Available Students: 55
Title: CTO
```

## Future Improvements
- Add more functionality, such as adding or removing students.
- Implement user authentication to better manage the roles.
- Store data in a database or external file for persistence.



---

