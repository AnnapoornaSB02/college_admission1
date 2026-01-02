app_ids = []
names = []
departments = []
marks_list = []
status_list = []

def apply_admission(app_id, name, department, marks):
    if app_id in app_ids:
        return "Application already exists"

    status = "Approved" if marks >= 60 else "Rejected"

    app_ids.append(app_id)
    names.append(name)
    departments.append(department)
    marks_list.append(marks)
    status_list.append(status)

    return "Application submitted successfully"

def view_application(app_id):
    if app_id in app_ids:
        index = app_ids.index(app_id)
        return (
            app_ids[index],
            names[index],
            departments[index],
            marks_list[index],
            status_list[index]
        )
    return None

def main():
    while True:
        print("\n1. Apply for Admission")
        print("2. View Application Status")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            app_id = input("Enter Application ID: ")
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")
            marks = float(input("Enter Marks: "))

            result = apply_admission(app_id, name, department, marks)
            print(result)

        elif choice == "2":
            app_id = input("Enter Application ID: ")
            result = view_application(app_id)

            if result:
                print("\n--- Application Details ---")
                print("Application ID :", result[0])
                print("Name           :", result[1])
                print("Department     :", result[2])
                print("Marks          :", result[3])
                print("Status         :", result[4])
            else:
                print("Application not found")

        elif choice == "3":
            print("Thank you")
            break

        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
