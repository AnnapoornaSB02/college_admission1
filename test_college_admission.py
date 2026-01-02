from college_admission import apply_admission, view_application

def test_apply_admission():
    result = apply_admission("A101", "Anu", "CSE", 85)
    assert result == "Application submitted successfully"

def test_rejected_admission():
    apply_admission("A102", "Ravi", "ECE", 45)
    data = view_application("A102")
    assert data[4] == "Rejected"
