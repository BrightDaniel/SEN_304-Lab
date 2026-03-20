import pytest
from project import calculate_average, get_grade

# =========================
#  BLACK-BOX TESTING
# =========================

#  Equivalence Partitioning (Valid Inputs)
def test_average_valid_scores():
    assert calculate_average([70, 80, 90]) == 80


#  Equivalence Partitioning (Mixed types)
def test_average_string_scores():
    assert calculate_average([70, "80", 90]) == 80


#  Boundary Value Analysis
def test_average_boundary_zero():
    assert calculate_average([0, 0, 0]) == 0


def test_average_boundary_high():
    assert calculate_average([100, 100, 100]) == 100


# =========================
# GRADE FUNCTION (BOUNDARIES)
# =========================

def test_grade_A_boundary():
    assert get_grade(70) == "A"


def test_grade_B_boundary():
    assert get_grade(60) == "B"


def test_grade_C_boundary():
    assert get_grade(50) == "C"


def test_grade_D_boundary():
    assert get_grade(45) == "D"


def test_grade_F_boundary():
    assert get_grade(44) == "F"


# =========================
# WHITE-BOX TESTING
# =========================

# Statement Coverage
def test_calculate_average_executes():
    result = calculate_average([10, 20, 30])
    assert result == 20


# Branch Coverage
def test_grade_all_branches():
    assert get_grade(75) == "A"
    assert get_grade(65) == "B"
    assert get_grade(55) == "C"
    assert get_grade(47) == "D"
    assert get_grade(30) == "F"


# Path Coverage (Different execution paths)
def test_multiple_paths():
    assert calculate_average([10, 20]) == 15
    assert calculate_average([5, 15, 25]) == 15


# =========================
# EDGE CASES & ERRORS
# =========================

def test_empty_list():
    with pytest.raises(ZeroDivisionError):
        calculate_average([])


def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_average([10, "abc", 20])