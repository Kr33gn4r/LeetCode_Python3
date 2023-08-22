import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=["salary"])
    if employee.shape[0] < N: return pd.DataFrame([None], columns=[f"getNthHighestSalary({N})"])
    else: return pd.DataFrame(
        [employee.salary.nlargest(N).iloc[-1]],
        columns=[f"getNthHighestSalary({N})"]
        )