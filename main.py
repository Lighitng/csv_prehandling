from DFWrapper import DFWrapper
import pandas as pd
df = pd.read_csv('./data.csv')
dfc = DFWrapper(df).regularColumn('组合').transposeType([('千粒重(g)', 'float')]).getFrame()
print(dfc.loc[:, '千粒重(g)'])
