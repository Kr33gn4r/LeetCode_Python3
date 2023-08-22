import pandas as pd
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    val = employee.drop_duplicates(subset=["salary"]).salary.nlargest(2)
    val = None if val.shape[0] == 1 else val.iloc[-1]
    return pd.DataFrame([val], columns=["SecondHighestSalary"])
