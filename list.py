fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[2])
#เปลี่ยนคำในlist
fruits[1]="blackcurrant"
print(fruits)
fruits[1:3]=["banana","kiwi","melon"]
print(fruits)
fruits[1:3]=["blackcurrant"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"banana")
print(fruits)
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("pineapple")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits:ลบตัวแปรlistทิ้งไปจากระบบ
#เรียงคำในlist
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#รวมlist
vege=["carrot","tomato","cucumber"]
all = fruits+vege
print(all)
#นายรชต หงษ์กระโทก ม.6/11 เลขที่ 6