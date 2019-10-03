import pandas as pd
from collections import Counter

class DFWrapper:
  # 只更改了数据值 未更改DataFrame.dtypes
  def __init__(self, df):
    if isinstance(df, pd.DataFrame):
      self.__df = df
      self.__columnHashTable = dict()
      self.__allowTypes = ['int', 'float', 'str', 'boolean']
    else:
      raise TypeError('Constructor error. Param not DataFrame.')
  def __setattr__(self,name,value):
    if name in self.__dict__:
      raise ValueError(f'{name} cannot be modified.')
    self.__dict__[name]=value
  def __str__(self):
    return self.__df.__str__()
  def _transposeValue(self, value, ttype):
    if ttype == 'int':
      return int(value)
    elif ttype == 'float':
      return float(value)
    elif ttype == 'str':
      return str(value)
    elif ttype == 'boolean':
      return 1 if value else 0
    else:
      raise TypeError('Unexpected error.')
  # @params {List} trinities
  #   [(key, to_type, holder), ]
  def transposeType(self, trinities):
    for trinity in trinities:
      holder = None
      key = None
      ttype = None
      # 省略了key是否存在的检验
      if len(trinity) == 2:
        key, ttype = trinity
      elif len(trinity) == 3:
        key, ttype, holder = trinity
      else:
        raise TypeError('Tuple must be (key, to_type) or (key, to_type, holder)')
      if ttype not in self.__allowTypes and type(ttype) != type:
        raise ValueError('Type illeagal.')
      for index, value in self.__df.loc[:, key].iteritems():
        try:
          if type(ttype) == type:
            value = ttype(value)
          else:
            value = self._transposeValue(value, ttype)
        except:
          value = holder
        self.__df.loc[index, key] = value
    return self
  def regularColumn(self, key, regRule=0):
    counter = Counter(self.__df.loc[:, key].to_list())
    if isinstance(regRule, list):
      if len(counter.keys) > len(regRule):
        raise ValueError('Extra index of range required.')
      for index, (val, times) in enumerate(counter.items()):
        counter[val] = regRule[index]
    elif isinstance(regRule, int):
      for index, (val, times) in enumerate(counter.items()):
        counter[val] = regRule
        regRule += 1
    else:
      raise ValueError('Parameter [regRule] must be list or int')
    self.__columnHashTable[key] = counter
    print(counter)
    for index, value in self.__df.loc[:, key].iteritems():
      self.__df.loc[index, key] = counter[value]
    return self
  def getFrame(self):
    return self.__df
  def getHashTable(self, key):
    return self.__columnHashTable.get(key)
