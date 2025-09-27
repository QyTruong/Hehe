# Trong câu điều kiện có thể sử dụng thêm các ký tự như là and, or, not, in

# Kiểm tra học lực
a = int(input("Enter a number: "))
if a > 9:
    print("Gioi")
elif a >= 7 and a <= 9:
    print("Kha")
elif a >= 5 and a < 7:
    print("tb")
else:
    print("yeu")

# Ngoài ra ta có thể lồng 1 điều kiện bên trong 1 điều kiện khác hay còn được gọi là "nested condition"
a = 0
if a > 0:
    # Đây có thể gọi là "nested condition" từ khóa này có xuất hiện trong câu 2. của Exercise: Level 1
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# Exercise
# Kiểm tra độ tuổi lái xe
userAge = int(input("Enter your age: "))
if userAge >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-userAge} more years to learn to drive.") # Sử dụng ký tự f trước 1 chuỗi => thay đổi linh hoạt nội dung bên trong nó

