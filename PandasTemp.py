import pandas as pd

good_data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 42],  # All non-negative
    'salary': [50000.0, 72000.5, 48000.75]  # All floats
}
good_df = pd.DataFrame(good_data)

def validate_data(good_df):
    """Validate DataFrame for business rules"""
    assert good_df['age'].min() >= 0, "Age cannot be negative"
    assert good_df['salary'].dtype == 'float64', "Salary should be a float"
    print("All validations passed!")

# Test the validation
try:
    validate_data(good_df)
except AssertionError as e:
    print(f"Validation Error: {e}")

