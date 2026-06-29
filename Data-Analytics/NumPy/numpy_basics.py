import numpy as np

var1=np.array([1,2,3,4])
print(var1)
var2=np.array([[1,2,3,4],[5,6,7,8]])
print(var2)

z=np.zeros((3,3),dtype='int')
print(z)
x=np.ones((3,3),dtype='int')
print(x)

np.random.seed(3)
a=np.random.rand(4,4)
print(a)

b=np.random.randn(4,4)
print(b)

np.random.seed(3)
x1=np.random.randint(low=50,high=100,size=(4,4))
print(x1)
x1[1,1]
x1[3,2]
x1[1:,2:]
x1[0:2,0:2]

np.identity(3,dtype='int')
np.arange(1,12)

a2=np.arange(1,10).reshape(3,3)
print(a2)
a2=a2.ravel()
print(a2)

c=np.arange(1,13).reshape(4,3)
c
c.transpose()

mat1=np.arange(12).reshape(3,4)
mat2=np.arange(12,24).reshape(3,4)
mat1
mat2
v=np.vstack((mat1,mat2))
v
h=np.hstack((mat1,mat2))
h
np.vsplit(h,3)
np.hsplit(v,2)
