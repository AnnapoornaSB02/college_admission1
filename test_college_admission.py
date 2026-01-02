from college_admission import check_admission_status

def test_approved():
    marks = 75
    assert check_admission_status(marks) == "Approved"

def test_approved_boundary():
    marks = 60
    assert check_admission_status(marks) == "Approved"

def test_rejected():
    marks = 50
    assert check_admission_status(marks) == "Rejected"

def test_rejected_zero():
    marks = 0
    assert check_admission_status(marks) == "Rejected"

def test_rejected_negative():
    marks = -10
    assert check_admission_status(marks) == "Rejected"
