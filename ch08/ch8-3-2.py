# 定義Vehicle父類別
class Vehicle:
    # 建構子
    def __init__(self, name):
        self.name = name
    # 方法
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name

# 定義Car子類別
class Car(Vehicle):
    # 建構子
    def __init__(self, name, model):
        # 呼叫父類別的建構子
        super().__init__(name)
        self.model = model
    # 方法
    def displayCar(self):
        print("名稱 = " + self.getName())
        print("車型 = " + self.model)
        
# 使用類別建立物件
c1 = Car("Ford", "GT350")
c1.displayCar()  # 呼叫方法
print("車輛廠牌 = " + c1.getName())
