import pandas as pd

# Load dataset
df = pd.read_csv("Employees.csv")

# 🔹 1. Total Employees
total_employees = df.shape[0]

# 🔹 2. Employees who left
employees_left = df[df["Attrition"] == "Yes"].shape[0]

# 🔹 3. Attrition Rate
attrition_rate = (employees_left / total_employees) * 100

print("Total Employees:", total_employees)
print("Employees Left:", employees_left)
print("Attrition Rate: {:.2f}%".format(attrition_rate))

# 🔹 4. Department-wise Attrition
dept_attrition = df[df["Attrition"] == "Yes"]["Department"].value_counts()

print("\nDepartment-wise Attrition:")
print(dept_attrition)

# 🔹 5. Average Salary by Attrition
salary_analysis = df.groupby("Attrition")["Salary"].mean()

print("\nAverage Salary by Attrition:")
print(salary_analysis)

# 🔹 6. Experience vs Attrition
experience_analysis = df.groupby("Attrition")["Experience"].mean()

print("\nAverage Experience by Attrition:")
print(experience_analysis)