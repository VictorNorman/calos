class Stack:

    def __init__(self):
        self.__data = []

    def push(self, it) -> None:
        self.__data.append(it)
    
    def pop(self):
        return self.__data.pop()

    @property
    def top(self):
        return self.__data[len(self.__data) - 1]
    
    def __str__(self):
        total = "-----\n"
        for it in reversed(self.__data):
            total += str(it) + '\n'
        total += "-----"
        return total
    
if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(6)
    assert(str(s) == "-----\n6\n5\n-----")
    s.pop()
    assert(s.top == 5)