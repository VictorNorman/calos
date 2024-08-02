from Symbol import Symbol
from CalCParser import CalCParser

# typedefs
SymbolTable = dict[str, Symbol]

def process_parameters(params: list[Symbol]):
    raise NotImplementedError()

class SymbolError(Exception):
    pass

class CalCOperations:
    @staticmethod
    def process_binary_operation(operation: CalCParser.Binary_opContext):
        if op := operation.add_op():
            return CalCOperations.process_add_op(op)
    
    @staticmethod
    def process_add_op(operation: CalCParser.Add_opContext):
        # if just mult_operation, process it respectively
        if not operation.ADD_OP():
            return CalCOperations.process_mult_op(operation.mult_op())
        
        # else, add_operation ADD_OPERATOR mult_operation form
        add_op = operation.add_op()
        mult_op = operation.mult_op()
        match operation.ADD_OP().getText():
            case "+":
                return CalCOperations.process_add_op(add_op) + CalCOperations.process_mult_op(mult_op)

            case "-":
                return CalCOperations.process_add_op(add_op) - CalCOperations.process_mult_op(mult_op)
        
    @staticmethod
    def process_mult_op(operation: CalCParser.Mult_opContext):
        # if just an operand, process it respectively
        if op := operation.operand():
            return CalCOperations.process_operand(op)
        
        # else, mult_operation MULT_OPERATOR binary_operation form
        mult_op = operation.mult_op()
        binary_op = operation.binary_op()
        match operation.MULT_OP().getText():
            case "*":
                return CalCOperations.process_mult_op(mult_op) * CalCOperations.process_binary_operation(binary_op)

            case "/":
                return CalCOperations.process_mult_op(mult_op) / CalCOperations.process_binary_operation(binary_op)
        
    @staticmethod
    def process_operand(operand: CalCParser.OperandContext):
        if lit := operand.lit():
            return eval(lit.getText())