import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A2020 = pd.DataFrame(pd.read_excel('aa2020.xlsx'))
A2021 = pd.DataFrame(pd.read_excel('aabc2021.xlsx'))

# b = pd.DataFrame(pd.read_csv('b.xlsx'))
# test = pd.DataFrame(pd.read_excel('testdata.xlsx'))

timeinfo = A2020['材料']
qfz = A2020['实验屈服值']
klz = A2020['实验抗拉值']
scl = A2020['实验伸长率']

list_timeinfo = [i for i in range(len(timeinfo))]
list_qfz = [i for i in qfz]
list_klz = [i for i in klz]
list_scl = [i for i in scl]

dict_qfz = {}
dict_klz = {}
dict_scl = {}

for key, value in zip(timeinfo, list_qfz):
    if type(key) is not type(''):
        print(key)
        dict_qfz[str(key)] = value
    else:
        dict_qfz[key] = value

for key, value in zip(timeinfo, list_klz):
    dict_klz[key] = value

for key, value in zip(timeinfo, list_scl):
    dict_scl[key] = value


def rank(k1, k2):
    return k1[:2] > k2[:2]


sorted(dict_qfz.items(), key=lambda x: x[0][:2])
print(dict_qfz)
# for item in dict_qfz.items():
#     print(item[0], item[1])
# print(dict_qfz)

plt.figure()
plt.plot(dict_qfz.values())
plt.show()
