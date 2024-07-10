class Stack:

    def __init__(self):
        self.__data = []

    def push(self, it):
        self.__data.append(it)
    
    def pop(self):
        self.__data.pop()
    
    def __str__(self):
        total = ""
        for entry in self.__data:
            total += entry
        return total