# Last updated: 6/23/2026, 7:11:52 AM
1class ParkingSystem:
2
3    def __init__(self, big: int, medium: int, small: int):
4        self.slots = [0, big, medium, small]
5
6    def addCar(self, carType: int) -> bool:
7        if self.slots[carType] > 0:
8            self.slots[carType] -= 1
9            return True
10        return False
11        
12
13
14# Your ParkingSystem object will be instantiated and called as such:
15# obj = ParkingSystem(big, medium, small)
16# param_1 = obj.addCar(carType)