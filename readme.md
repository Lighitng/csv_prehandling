# csv数据预处理
## 1. api
### 构造函数：```constructor: DFWrapper(DataFrame)```
```python
import pandas as pd
import DFWrapper
df = pd.read_csv('path_to_csv_file')
dfw = DFWrapper(df)
```
### 格式转换：```DFWrapper.transposeType([('column', 'to_type', 'holder'), ])```[允许链式调用]
```python
# holder 默认为 None
dfw.transposeType([('年龄', 'int')])
# 支持传入基础数据类型
dfw.transposeType([('月薪', float, '转换失败占位符'), ('年龄', 'int')])
```
### 格式化某列：```DFWrapper.regularColumn('columnName', regRule)```[允许链式调用]
其中regRule代表格式化规则，默认从0开始用每个数字替换列中相同的一类值

regRule允许传入一个int值（从这个数字开始依次替换，如regRule=10，则用10，11，12……替换）或一个列表（用该列表的值替换），替换顺序不能保证。
```python
dfw.regularColumn('国家')
dfw.regularColumn('市', regRule=['0435', '0431', '010', '020'])
```
### 获取DataFrame原型对象：```DFWrapper.getFrame()```

### 获取映射表（格式化映射表）```DFWrapper.getHashTable(key)```
```python
dfw.regularColumn('省份')
dfw.getHashTable('省份')
```
```python
{
  '梅河口市': 0,
  '长春市': 1,
  'xx市': 2,
  'xxx市': 3
}
```
```python
dfw.regularColumn('省份', regRule=['0435', '0431', '010', '020'])
dfw.getHashTable('省份')
```
```python
{
  '梅河口市': '0435',
  '长春市': '0431',
  'xx市': '010',
  'xxx市': '020'
}
```

