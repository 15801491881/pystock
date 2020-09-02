import numpy as np
import pandas as pd
s = np.arange(0,1000000)
df = pd.DataFrame(s)
print(df)
df.to_excel("股票代码.xlsx")