import pandas as pd

print("\n----- EX. NO: 4 (b) - Employee Work Hours -----")

data_b = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR'],
    'Hours Worked': [40, 45, 38, 50, 42, 48, 41]
}

df_b = pd.DataFrame(data_b)
dept_hours = df_b.groupby('Department')['Hours Worked'].sum().reset_index()

print("\nTotal Hours Worked by Department:")
print(dept_hours)

pivot_b = pd.pivot_table(df_b, values='Hours Worked', index='Department', aggfunc=['sum', 'mean']).round(2)
pivot_b.columns = ['Total Hours', 'Average Hours']

print("\nDepartment-wise Summary:")
print(pivot_b)

highest_avg_dept = pivot_b['Average Hours'].idxmax()
print(f"\nDepartment with highest average working hours: {highest_avg_dept}")
