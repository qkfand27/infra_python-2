#step11_class.py

#step11_class.py

class MyCar:

    def __init__(self, name):
        self.name = name
        print("생성자가 호출됨")
        print(self)

    def drive(self):
        print(f"{self.name} 이(가) 달려요~")

if __name__ == "__main__":
    c1: MyCar = MyCar("코닉세그")
    c2: MyCar = MyCar("파가니")
    c1.drive()
    c2.drive()