import numpy as np
import pandas as pd

data = [
  {"student_id": 103, "student_name": "Kabir", "subject": "Physics", "marks": 78.9},
  {"student_id": 101, "student_name": "Aarav", "subject": "Mathematics", "marks": 88.5},
  {"student_id": 105, "student_name": "Rohan", "subject": "Chemistry", "marks": 82.6},
  {"student_id": 102, "student_name": "Diya", "subject": "Physics", "marks": 89.6},
  {"student_id": 104, "student_name": "Meera", "subject": "Mathematics", "marks": 95.2},
  {"student_id": 101, "student_name": "Aarav", "subject": "Chemistry", "marks": 84.7},
  {"student_id": 106, "student_name": "Ananya", "subject": "Mathematics", "marks": 91.8},
  {"student_id": 102, "student_name": "Diya", "subject": "Chemistry", "marks": 94.1},
  {"student_id": 103, "student_name": "Kabir", "subject": "Mathematics", "marks": 81.7},
  {"student_id": 105, "student_name": "Rohan", "subject": "Physics", "marks": 76.4},
  {"student_id": 104, "student_name": "Meera", "subject": "Chemistry", "marks": 90.4},
  {"student_id": 101, "student_name": "Aarav", "subject": "Physics", "marks": 91.2},
  {"student_id": 106, "student_name": "Ananya", "subject": "Physics", "marks": 87.3},
  {"student_id": 102, "student_name": "Diya", "subject": "Mathematics", "marks": 92.3},
  {"student_id": 103, "student_name": "Kabir", "subject": "Chemistry", "marks": 85.6},
  {"student_id": 105, "student_name": "Rohan", "subject": "Mathematics", "marks": 79.8},
  {"student_id": 104, "student_name": "Meera", "subject": "Physics", "marks": 93.7},
  {"student_id": 106, "student_name": "Ananya", "subject": "Chemistry", "marks": 89.5}
]

students = pd.DataFrame(data=data)

# print(type(students.iloc[3].values))
something = students.groupby(["student_id"]).agg(
    total_marks=("marks", "sum")
)

something["grade"] = np.where(something["total_marks"] > 250, "Excellent", "Good")

print(something.to_markdown())