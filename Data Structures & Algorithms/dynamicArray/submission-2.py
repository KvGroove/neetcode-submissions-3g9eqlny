class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        while self.length >= self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        popped = self.array[self.length-1]
        self.array[self.length-1] = 0
        self.length -= 1
        return popped

    def resize(self) -> None:
        new_array = [0] * self.capacity * 2
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity *= 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity