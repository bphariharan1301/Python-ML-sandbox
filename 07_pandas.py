
import pandas as pd
import seaborn as sns


import matplotlib.pyplot as plt

rd = pd.read_csv(r"D:\AAdityAA\Python_Sandbox\diabetes-200520-125813.csv")


# print(rd) print all the rows

print(rd.head(2)) # Print 2 rows from the dataset

print(rd.head(-2))

rd.tail(2)
rd.tail(-2)

print(rd['Pregnancies'])

print(type(rd['Pregnancies']))

print(rd.dtypes)

print(rd.shape)

print(rd.size)

print(len(rd))

print(rd.info)

print(rd.columns)

print(rd.values)

nn = rd['Age']
print(nn)

print(rd.loc[1])

print(nn.values)

nit = rd.drop([2,3], axis=0)

sns.pairplot(rd)

plt.show()



# sns.pairplot()






