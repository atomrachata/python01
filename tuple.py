tuplefruits = ("apple","banana","cherry") #Tuple
listfruits = ["apple","banana","cherry"] #List
print("original tuple",tuplefruits)
print("original list",listfruits)
#เปลี่ยนค่าในtuple
x=list(tuplefruits)#แปลงเป็นlistแล้วเก็บในตัวแปรx
x[1]="blueberry"
tupleFruits=tuple(x)
print("เปลี่ยนค่าในtuple:",tupleFruits)
#เพิ่มคำในtuple
x=list(tupleFruits)
x.append("melon")
tupleFruits=tuple(x)
print("เพิ่มค่าtuple:",tuplefruits)
#ลบtuple
x=list(tupleFruits)
x.remove("cherry")
tupleFruits+tuple(x)
print("ลบค่าtuple:",tupleFruits)
#join tuple
vege=("tomato","cacumber","onion")
fruitVege=tupleFruits+vege
print("join tuple:",fruitVege)
x=range(3, 6)
for n in x:
    print("range x:",n)
y=range(3,20,2)
for m in y:
    print("range x:",m)
#นายรชต หงษ์กระโทก ม.6/11 เลขที่ 6