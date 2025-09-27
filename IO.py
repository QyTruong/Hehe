# đầu vào hàm input luôn là kiểu string
# Khi sử dụng input, cần phải có 1 biến để hứng dữ liệu mà input truyền vào
a1 = input()
a2 = input("Enter a number: ") # Có thể viết thêm nội dung trong input giúp user dễ hiểu

# Có thể ép kiểu cho input hay 1 biến nào đó
a3 = int(input()) # ép thành int
a4 = float(input()) # ép thành float

# Ta có thể ép kiểu theo nhiều cách khác
b1 = input()
b2 = int(b1) # Lúc này b2 sẽ mang giá trị của b1 nhưng giá trị đó mang kiểu int
print(float(b1)) # Ta cũng có thể ép kiểu trong lúc print

# Sử dụng type kiểm tra kiểu dữ liệu
print(type(a1))
