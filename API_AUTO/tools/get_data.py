# 反射
from API_AUTO.tools import project_path
import pandas as pd

class GetData:
    tel_1 = pd.read_excel(project_path.test_data_path, sheet_name='init').iloc[0, 0]



# print(getattr(GetData, 'NpRegTel'))