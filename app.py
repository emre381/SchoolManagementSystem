class School:
    def __init__(self, branch, teacher, department, available):
        self.branch = branch
        self.teacher = teacher
        self.department = department
        self.available = available

    def show_info(self):
        print("-" * 45)
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nAvailable Students: {}".format(self.branch, self.teacher, self.department, self.available))
        print("-" * 45)

    def teacher_name(self):
        print("Teacher name: ", self.teacher)

    def depart_change(self):
        new_depart = input("Please enter the new department: ")
        print("***Old Department***: ", self.department)
        self.department = new_depart
        print("-" * 45)
        self.show_info()


class Manager(School):
    def __init__(self, branch, teacher, department, available, title):
        super().__init__(branch, teacher, department, available)
        self.title = title

    def show_info(self):
        print("-" * 45)
        print("**Director panel**")
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nAvailable Students: {}\nTitle: {}".format(
            self.branch, self.teacher, self.department, self.available, self.title))
        print("-" * 45)

    def change_teacher(self):
        new_teacher = input("Enter the new teacher's name: ")
        print("***Old Teacher***: ", self.teacher)
        self.teacher = new_teacher
        print("-" * 45)
        self.show_info()

    def change_branch(self):
        new_branch = input("Enter the new branch: ")
        print("***Old Branch***: ", self.branch)
        self.branch = new_branch
        print("-" * 45)
        self.show_info()

def main():
    # Initial setup
    director = Manager("11", "Emre", "Tech", 55, "CTO")
    
    # Determine user role
    role = input("Enter your role (teacher/director): ").strip().lower()

    if role == "teacher":
        print("Welcome to the teacher panel.")
        director.show_info()

        while True:
            choice = input("Would you like to change the department? (yes/no): ").strip().lower()
            if choice == "yes":
                director.depart_change()
            else:
                print("Exiting teacher panel.")
                break

    elif role == "director":
        print("Welcome to the director panel.")
        director.show_info()

        while True:
            print("1. Change Department")
            print("2. Change Teacher")
            print("3. Change Branch")
            print("4. Exit")
            choice = input("Please choose an option: ")

            if choice == "1":
                director.depart_change()
            elif choice == "2":
                director.change_teacher()
            elif choice == "3":
                director.change_branch()
            elif choice == "4":
                print("Exiting director panel.")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Invalid role. Exiting.")

if __name__ == "__main__":
    main()
