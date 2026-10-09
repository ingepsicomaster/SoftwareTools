# Step 1: Raw / Messy Code (Before Principles)

# Messy code – not modular, not reusable, hard to maintain

import pandas as pd
from typing import List, Any
import random

# FUNCTIONS CREATED <==
# I HAVE ACTIVATED AUTOPEP8


def generate_numbers(count: int, lower: int = 1, upper: int = 100) -> List[int]:
    numbers = [random.randint(lower, upper) for _ in range(count)]
    print("Generated numbers:", numbers)
    return numbers

# Calculate average


def calculate_average(numbers: List[int]) -> float:
    total = 0
    for n in numbers:
        total += n
    average = total / len(numbers)
    print("Average:", average)
    return average

# Find max


def find_max(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    print("Max:", max_num)
    return max_num


"""
✅ Now Fixed:

Functions created                           SOLVED
Reusable logic                              SOLVED
Can be extended                             SOLVED
Scalable                                    SOLVED
Error handling added                        SOLVED
"""

# Step 2: Refactored Code (With Principles)


def generate_numbers(count: int, lower: int = 1, upper: int = 100) -> List[int]:
    """Generate a list of random integers."""
    return [random.randint(lower, upper) for _ in range(count)]


def calculate_average(numbers: List[int]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return sum(numbers) / len(numbers)


def find_max(numbers: List[int]) -> int:
    """Return the maximum number from a list."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return max(numbers)


if __name__ == "__main__":
    # Example workflow (can be reused in other projects)
    nums = generate_numbers(10)
    print("Generated numbers:", nums)
    print("Average:", calculate_average(nums))
    print("Max:", find_max(nums))

"""
✅ Improvements:

Modularity              SOLVED
Reusability             SOLVED
Easy to maintain        SOLVED
Scalabilit              SOLVED
"""

# Classroom Activity

# Step 1: Raw / Messy Pandas Code


# Load CSV
df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Print average sepal length
avg = df['sepal_length'].mean()
print("Average sepal length:", avg)

# Print max petal width
mx = df['petal_width'].max()
print("Max petal width:", mx)

# Filter rows where species is setosa
print(df[df['species'] == 'setosa'].head())

"""
🔴 Problems:

All logic in one block → not modular.               SOLVED
Hard to reuse functions for other datasets.         SOLVED
No error handling → breaks if column names change.  SOLVED
Not scalable (imagine working on multiple CSVs).    SOLVED
No documentation → not good for collaboration.      SOLVED
"""

# Step 2: Refactored Pandas Code (With Principles)


def load_data(url: str) -> pd.DataFrame:
    """Load CSV data from URL with error handling."""
    try:
        return pd.read_csv(url)
    except Exception as e:
        raise ValueError(f"Failed to load data from {url}: {e}")


def calculate_column_average(df: pd.DataFrame, column: str) -> float:
    """Calculate average of a specific column with validation."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset")
    if df[column].isnull().all():
        raise ValueError(f"Column '{column}' contains only null values")
    return df[column].mean()


def find_column_max(df: pd.DataFrame, column: str) -> Any:
    """Find maximum value in a specific column with validation."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset")
    if df[column].isnull().all():
        raise ValueError(f"Column '{column}' contains only null values")
    return df[column].max()


def filter_by_category(df: pd.DataFrame, column: str, value: Any) -> pd.DataFrame:
    """Filter rows by a specific category value with validation."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset")
    filtered_result = df[df[column] == value]
    if filtered_result.empty:
        raise ValueError(f"Value '{value}' not found in column '{column}'")
    return filtered_result


if __name__ == "__main__":
    # Example workflow with iris dataset
    iris_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

    iris_data = load_data(iris_url)

    avg_sepal_length = calculate_column_average(iris_data, 'sepal_length')
    print(f"Average sepal length: {avg_sepal_length}")

    max_petal_width = find_column_max(iris_data, 'petal_width')
    print(f"Max petal width: {max_petal_width}")

    setosa_data = filter_by_category(iris_data, 'species', 'setosa')
    print(f"\nSetosa flowers (first 5):\n{setosa_data.head()}")

"""
✅ Improvements:

Modularity
Reusability
error handling
Scalability
"""
