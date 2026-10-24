import numpy as np # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# ----------------------------
# 1. NumPy Section
# ----------------------------
print("--- NumPy Analysis ---")
# 4 students x 3 subjects
marks = np.array([
    [75, 80, 85],
    [60, 65, 70],
    [90, 95, 88],
    [50, 55, 60]
])

print("Shape:", marks.shape)
print("Student averages (axis=1):", marks.mean(axis=1))
print("Subject averages (axis=0):", marks.mean(axis=0))

# Broadcasting: Add 5 grace marks
marks_with_grace = marks + 5
print("Marks with grace:\n", marks_with_grace)

# Weighted scores using np.dot
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks_with_grace, weights)
print("Weighted scores:", weighted_scores)


# ----------------------------
# 2. Pandas Section
# ----------------------------
print("\n--- Pandas Analysis ---")

# Raw data with duplicates and missing values
raw_emp_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
    'name': ['Arun', 'Priya', 'Rahul', 'Divya', 'Karthik', 'Meena', 'Suresh', 'Anitha', 'Duplicate', 'Duplicate'],
    'department': ['Sales', 'HR', 'IT', 'IT', 'Finance', 'Sales', 'IT', 'HR', 'IT', 'IT'],
    'salary': [30000.0, None, 60000.0, 75000.0, 90000.0, 52000.0, None, 48000.0, 65000.0, 65000.0],
    'city': ['Chennai', 'Chennai', 'Bangalore', 'Chennai', 'Mumbai', 'Bangalore', 'Chennai', 'Mumbai', 'Chennai', 'Chennai']
}
df_emp = pd.DataFrame(raw_emp_data)

# Inspection
print("\nInfo:")
df_emp.info()
print("\nDescribe:\n", df_emp.describe())

# Cleaning
df_emp = df_emp.drop_duplicates()
median_sal = df_emp['salary'].median()
df_emp['salary'] = df_emp['salary'].fillna(median_sal).astype(float)

# Selection using loc and iloc
print("\nloc (Chennai Emps):\n", df_emp.loc[df_emp['city'] == 'Chennai', ['name', 'salary']])
print("\niloc (First 3 rows):\n", df_emp.iloc[:3, :])

# Groupby & Aggregation
agg_df = df_emp.groupby('department').agg(
    Headcount=('id', 'count'),
    Avg_Salary=('salary', 'mean'),
    Max_Salary=('salary', 'max')
).reset_index()

print("\nDepartment Aggregations:")
print(agg_df)

# Merges
departments_df = pd.read_csv("data/departments.csv")

inner_merged = pd.merge(df_emp, departments_df, on='department', how='inner')
left_merged = pd.merge(df_emp, departments_df, on='department', how='left')
outer_merged = pd.merge(df_emp, departments_df, on='department', how='outer')

empty_dept = outer_merged[outer_merged['id'].isna()]['department'].values[0]
print(f"\nOuter join department with no employees listed: {empty_dept}")


# ----------------------------
# 3. Matplotlib Section
# ----------------------------
# Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(agg_df['department'], agg_df['Headcount'], color='skyblue', label='Headcount')
plt.title("Employee Headcount by Department")
plt.xlabel("Department")
plt.ylabel("Headcount")
plt.legend()
plt.tight_layout()
plt.savefig("reports/bar_chart.png")
plt.close()
# Insight: IT department holds the highest headcount among all business units.

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(df_emp['salary'], bins=5, color='salmon', edgecolor='black', label='Salary Range')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("reports/histogram.png")
plt.close()
# Insight: Most salaries are concentrated in the 40k to 70k bracket.

# Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(df_emp['id'], df_emp['salary'], color='green', label='Employees')
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("reports/scatter_chart.png")
plt.close()
# Insight: No strong correlation exists between employee ID registration order and compensation level.

# Line Chart
plt.figure(figsize=(6, 4))
df_sorted = df_emp.sort_values('id')
plt.plot(df_sorted['id'], df_sorted['salary'], marker='o', linestyle='-', color='purple', label='Salary Trend')
plt.title("Salary Progression Across IDs")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("reports/line_chart.png")
plt.close()
# Insight: Salary levels fluctuate significantly across employee onboarding IDs.
