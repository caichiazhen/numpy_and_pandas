#import numpy as np
#
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
#
# array1 = np.array(list1)
# array2 = np.array(list2)
#
# print(array1)
# print(array1.ndim, array1.shape, array1.dtype)
#
# array1 = array1.reshape([2, 2])
# array1 = array1.astype('int')
# print(array1)
#
# array3 = np.zeros(5)
# print(array3)
#
# array4 = np.ones((3, 4))
# print(array4)
#
# array5 = np.arange(1, 10, 2)
# print(array5)
#
# array6 = np.full((3, 4), 10)
# print(array6)
#
# array7 = np.ones_like(array6)
# print(array7)
#
# print(np.random.random((2, 3)))
#
# print(np.random.randint(0, 100, size=(3, 3)))
#
# np.random.seed(45962)
# print(np.random.randint(0, 100, size=(3, 3)))
#
# array1 = array1.reshape([2, 2])
# array2 = array2.reshape([2, 2])
# print(array1)
# print(array2)
#
# array8 = np.concatenate((array1, array2), axis=1)
# #axis:0=縱；1=橫
# print(array8)
#
# print(array1)
# print(array1.sum(axis = 1))
#
# array9 = [2, 4, 6, 7, 8, 9]
# array9 = np.array(array9)
# print(array9)
#
# array10 = np.delete(array9, [2,4])
# print(array10)
#
# array11 = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12]])

#print(np.delete(array11, [2, 4]))

#print(np.delete(array11, [2, 4], axis=0))

#print(np.delete(array11, [2, 4], axis=1))
# print(array11[0, 2])
# print(array1+array2)
# print(array1-array2)
# print(array1*array2)
# print(array1/array2)
# print(array1.dot(array2))
# print(array11>5)
# print(array11.T)#轉置
# array12 = array11[array11>5]
# print(array12)
#
# file = "a.npy"
# with open(file, "wb") as f:
#     np.save(f, array11)
#
# with open(file, 'rb') as f:
#     array14 = np.load(f)
#     print(array14)
#
# file1 = "text.out"
# np.savetxt(file1, array11, delimiter=',')
#
# array15 = np.loadtxt(file1, delimiter=',')


#pandas(python的excel)


import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

s2 = pd.Series([1, 2, 3, 4, 5],
               index=['a', 'b', 'c', 'd', 'e'])
print(s2)

dict1 = {'a':1, 'b':2, 'c':3}
s3 = pd.Series(dict1)
print(s3)

s4 = pd.Series(dict1, index = ['a', 'b', 'd'])
print(s4)

print(s1.values)

print(s2)
print(s2[0], s2['a'])#拿單一元素
print(s2[[1, 2, 4]])
print(s2[['b', 'c', 'e']])
print(s2)
s2['f'] = 50
print(s2)

print(s2>3)
print(s2[s2>3])

print('a' in s2)
print('g' in s2)

print(s2 + 100)

print(s1)
print(s2)
print(s1 + s2)

print(s3)
print(s4)
print(s3 + s4)

print(s4.isnull())
print(s4.notnull())

list1 = ['Eric', 'Lisa', 'Amber']
s4.index = list1
print(s4)

print(s4.sort_index())
print(s4.sort_index(ascending=False))#改為降冪排序，預設為升冪
print(s4.sort_index(na_position="first"))#nan值預設為放在最後，此為放前面

print(s4.sort_values())
print(s4.sort_values(ascending=False))
print(s4.sort_values(ascending=False,
                     na_position="first"))
#print(s4.fillna(100))#nan填100
print(s4.fillna(method='ffill'))#往前拿有效值
print(s4.fillna(method='bfill'))#往後拿有效值，但若後面沒有則維持nan，排去後再使用
print(s4.dropna())#直接刪掉