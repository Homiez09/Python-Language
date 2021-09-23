import numpy as np

# array 1D
a = [1,2,3,4,5]
arrA = np.array(a)
# array 2D *ใช้บ่อยสุด
b = [[1,2,3],
     [4,5,6],
     [7,8,9]]
arrB = np.array(b)
# array 3D
c = [[[1,2,3],[4,5,6],[7,8,9]],
     [[10,11,12],[13,14,15],[16,17,18]]]  #[dept][row][column]
arrC = np.array(c)

#สร้าง Zero Matrix 
zm = np.zeros([3,3], dtype="int")
#สร้าง Ones Matrix
om = np.ones([3,3], dtype="int")
#Matrix ค่าคงที่
km = np.full([3,3],8)

#empty array
ea = np.empty([3,5])

#Identity Matrix เส้นทะแยงมุมเป็นเลข 1
im = np.identity(3, dtype="int")
em = np.eye(5,dtype="int")
emk = np.eye(5, k=-1, dtype="int") #ย้ายตำแหน่งเลข 1 ที่เป็นเส้นทะแยงมุม ขึ้น(k=1+) ลง(k=-1-)

#linsspace np.linspace(start,stop,number)
ls = np.linspace(1,5,4)

#Arange np.arange(start,stop.step,dtype)
anp = np.arange(1,11,2,dtype="int")

#random
rdnp = np.random.random((3,3))

#NumPy Attribute
Aa = arrA.shape
Ab = arrA.ndim 
Ac = arrA.dtype
Ad = arrA.size
Ae = arrA.itemsize

#Slice Array 1D 
sa1 = np.arange(1,11) #[ 1  2  3  4  5  6  7  8  9 10]
'''print(sa[:])        #[ 1  2  3  4  5  6  7  8  9 10]
print(sa1[2:])       #[ 3  4  5  6  7  8  9 10]
print(sa1[:5])       #[1 2 3 4 5]
print(sa1[2:5])      #[3 4 5]
print(sa1[2:5:2])    #[3 5] ระบุ step [3, 3(+2)]'''

#Slice Array 2D 
sa2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(sa2[:,:])
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]'''
#print(sa2[1:,1:])
'''
[[5 6]
 [8 9]]'''
#print(sa2[2:,2:])
'''
[[9]]'''
#print(sa2[:,2:])
'''
[[3]
 [6]
 [9]]'''

#Index Opertator
xx = np.arange(1,10)
index0 = np.array([1,5])
xxindex = xx[index0]

yy = np.array([[1,-2,3],[4,-5,-9]])
yyindexy = yy[yy<2]

#ตัวดำเนินการทางคณิตศาสตร์  คูณเข้าแต่ละช่อง
tda = np.arange(1,5)
#print(tda*5)

#Reshape Resize
rh = [0,1,2,3,4,5,6,7,8,9]
arrh = np.array(rh)
#print(arrh.reshape(2,5)) 

#Flatten ทำให้ array หลายมิติเป็น 1D
arrft = np.array([[1,2],[3,4],[5,6]])
ft = arrft.flatten()
#print(ft)      #[1 2 3 4 5 6]

#Transpose เปลี่ยนจากแนวตั้งเป็นแนวนอน เปลี่ยนจากแนวนอนเป็นแนวตั้ง
ts = np.array([[1,2,3],[4,5,6]])
yests = ts.transpose()
#print(yests)

#ฟังก์ชันทางสถิติ
newarr = np.array([10,5,4,6,99,100,50,30])
print(newarr.sum())
print(newarr.prod())
print(newarr.mean())
print(newarr.max())
print(newarr.min())
print(newarr.argmax())
print(newarr.argmin())
newarr2 = np.array([[10,20,30],[40,50,90],[80,100,5]])
axis1test = np.min(newarr2,axis=1)  #หาค่าต่ำสุดในแนวนอน
print(axis1test)
axis0test = np.min(newarr2,axis=0)  #หาค่าต่ำสุดในแนวตั้ง
print(axis0test)


