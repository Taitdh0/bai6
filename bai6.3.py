print ("Tran Tuan Tai")
print("235752021610014")
class Nguoi:
    def __init__(self, ten):
        self.ten = ten

    def getGender(self):
        pass

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Ví dụ sử dụng các class
nguoi_nam = Nam("An")
nguoi_nu = Nu("Hoa")

print(f"{nguoi_nam.ten} là {nguoi_nam.getGender()}")
print(f"{nguoi_nu.ten} là {nguoi_nu.getGender()}")
