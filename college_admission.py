import sys

def check_admission_status(marks):
    """Check if student is approved for admission based on marks."""
    if marks >= 60:
        return "Approved"
    else:
        return "Rejected"

if __name__ == "__main__":
    if len(sys.argv) == 5:
        student_name = sys.argv[1]
        student_id = sys.argv[2]
        department = sys.argv[3]
        marks = int(sys.argv[4])
        print("Using user-provided input:")
    else:
        # Default values
        student_name = "Annapoorna Budarkatti"
        student_id = "C101"
        department = "Computer Science"
        marks = 75
        print("No input given - using default values:")

    status = check_admission_status(marks)

    print("\n========== College Admission Details ==========")
    print("Student Name:", student_name)
    print("Student ID:", student_id)
    print("Department:", department)
    print("Marks Obtained:", marks)
    print("Admission Status:", status)
