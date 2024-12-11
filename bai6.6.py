print ("Tran Tuan Tai")
print("235752021610014")
class MyString:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Nhập chuỗi của bạn: ")

    def print_String(self):
        print(self.string.upper())

# Ví dụ sử dụng class MyString
my_string = MyString()
my_string.get_String()
my_string.print_String()
