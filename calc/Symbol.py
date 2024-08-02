from enum import IntEnum

class SymbolType(IntEnum):
    function = 0
    int = 1
    float = 2
    bool = 3
    char = 4
    defined = 5
    
    def __str__(self):
        return self.name

class Symbol:
    
    def __init__(self, name: str, type: SymbolType, function: bool = False, params: list = []):
        self._name = name
        self._type = type
        self._function = function
        self._value = None

        if self._function:
            self._params_list: list[Symbol] = params

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
    @property
    def base_offset(self):
        if not self._function:
            return self._offset
        
        raise ValueError("Function symbols cannot have an offset")
    
    @base_offset.setter
    def base_offset(self, new_offset):
        if not self._function:
            self._offset = new_offset
        else:
            raise ValueError("Function symbols cannot have an offset")

    @property
    def type(self) -> SymbolType:
        return self._type

    @property
    def is_function(self) -> bool:
        return self._function
    
    @property
    def parameters(self) -> list:
        if self._function:
            return self._params_list
        
        raise ValueError("Non-function symbols cannot have parameters!")
    
    @parameters.setter
    def parameters(self, params: list):
        if self._function:
            self._params_list: list[Symbol] = params
        else:
            raise ValueError("Non-function symbols cannot have parameters!")
        
    @staticmethod
    def string2type(s):
        match(s):
            case("int"):
                return SymbolType.int
            case("float"):
                return SymbolType.float
            case("bool"):
                return SymbolType.bool
            case("char"):
                return SymbolType.char
            case _:
                return SymbolType.defined
            
    def __str__(self) -> str:
        return f"{self._name}: {self._type}, {(self._value, self._offset) if not self._function else self._params_list}"
    
    def __eq__(self, other) -> bool:

        if type(other) != Symbol:
            return False

        if (self._name != other._name or self._type != other._type):
            return False
        
        if self._function:
            return self._params_list == other._params_list
        
        return True
            
if __name__ == "__main__":
    s = Symbol("num", SymbolType.int)
    assert(not s.is_function)

    s2 = Symbol("func", SymbolType.function, True, [Symbol("num", SymbolType.int)])
    assert(s2.is_function)
    assert(s2.parameters[0] == Symbol("num", SymbolType.int))
