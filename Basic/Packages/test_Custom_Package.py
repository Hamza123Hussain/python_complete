# test_Custom_Package.py

# Import the functions to be tested
from Custom_Package import Sqaureme, CheckSqaure

# Test the Sqaureme function
def test_Sqaureme():
    # Testing the function with correct values
    assert Sqaureme(2) == 4, "Expected 4, but got something else"
    assert Sqaureme(3) == 6, "Expected 6, but got something else"

# # Test the CheckSqaure function (with the incorrect logic that will fail intentionally)
# def test_CheckSqaure():
#     # This will fail because Sqaureme(2) is incorrectly adding rather than squaring
#     assert Sqaureme(2) != 2 * 2, "There is an intentional error in the logic"
