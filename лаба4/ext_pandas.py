import pandas as pd

def test_pandas():
    df = pd.DataFrame({"Ім'я": ["Анна", "Богдан"], "Вік": [20, 22]})
    print("pandas: Створено DataFrame:")
    print(df)