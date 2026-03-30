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
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        self.length -= 1
        return self.array[self.length]


    def resize(self) -> None:
        new_array = [0] * 2 * len(self.array)
        self.capacity = len(new_array)
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity