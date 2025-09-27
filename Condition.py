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

# Exercise
# Kiểm tra độ tuổi lái xe
userAge = int(input("Enter your age: "))
if userAge >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-userAge} more years to learn to drive.") # Sử dụng ký tự f trước 1 chuỗi => thay đổi linh hoạt nội dung bên trong nó

