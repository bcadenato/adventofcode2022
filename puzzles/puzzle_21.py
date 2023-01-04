import operator

COLON = ':'

MONKEY_NAME = 'monkey_name'
MONKEY_TYPE = 'monkey_type'
TYPE_NUMBER = 'monkey_number'
TYPE_OP = 'monkey_operation'
NUMBER = 'number'
OPERATOR = 'operator'
PARAM_1 = 'param_1'
PARAM_2 = 'param_2'

def read_monkey(line):
    
    monkey = {}
    
    line = line.replace(COLON, '')
    tokens = line.split()
    
    monkey[MONKEY_NAME] = tokens.pop(0)
    
    if len(tokens) == 1:
        monkey[MONKEY_TYPE] = TYPE_NUMBER
        monkey[NUMBER] = int(tokens.pop(0))
        
        return monkey
    
    if len(tokens) == 3:
        monkey[MONKEY_TYPE] = TYPE_OP
        monkey[PARAM_1] = tokens.pop(0)
        monkey[OPERATOR] = tokens.pop(0)
        monkey[PARAM_2] = tokens.pop(0)
        
        return monkey


def read_monkey_file(file):
    
    with open(file) as f:
        lines = f.read().splitlines()
    
    monkey_dict = {}
    
    for line in lines:
        monkey = read_monkey(line)
        monkey_dict[monkey[MONKEY_NAME]] = monkey
    
    return monkey_dict

class MonkeyOperator:
    OP_ADD = '+'
    OP_SUB = '-'
    OP_MUL = '*'
    OP_DIV = '/'


def process_monkey_dict(monkey_dict, monkey_name):
    
    monkey_specs = monkey_dict[monkey_name]
    
    if monkey_specs[MONKEY_TYPE] == TYPE_NUMBER:
        monkey = MonkeyNumber(monkey_specs[MONKEY_NAME], 
                              monkey_specs[NUMBER])
        
        return monkey
    
    if monkey_specs[MONKEY_TYPE] == TYPE_OP:
        
        monkey_child_1 = process_monkey_dict(monkey_dict, monkey_specs[PARAM_1])
        monkey_child_2 = process_monkey_dict(monkey_dict, monkey_specs[PARAM_2])
        
        match monkey_specs[OPERATOR]:
            case MonkeyOperator.OP_ADD:
                monkey_op = operator.add
            case MonkeyOperator.OP_SUB:
                monkey_op = operator.sub
            case MonkeyOperator.OP_MUL:
                monkey_op = operator.mul
            case MonkeyOperator.OP_DIV:
                monkey_op = operator.floordiv
        
        monkey = MonkeyOperation(monkey_specs[MONKEY_NAME],
                                 monkey_op,
                                 monkey_child_1,
                                 monkey_child_2)
        
        return monkey


MONKEY_ROOT = 'root'
MONKEY_HUMN = 'humn'

def process_monkey_dict_2(monkey_dict, monkey_name):
    
    monkey_specs = monkey_dict[monkey_name]
    
    if monkey_name == MONKEY_ROOT:
        
        monkey_child_1 = process_monkey_dict_2(monkey_dict, monkey_specs[PARAM_1])
        monkey_child_2 = process_monkey_dict_2(monkey_dict, monkey_specs[PARAM_2])
        
        monkey_op = operator.eq
        
        monkey = MonkeyOperation(monkey_specs[MONKEY_NAME],
                                 monkey_op,
                                 monkey_child_1,
                                 monkey_child_2)
        
        return monkey
    
    if monkey_name == MONKEY_HUMN:
        
        monkey = MonkeySolver(monkey_specs[MONKEY_NAME])
        
        return monkey
    
    if monkey_specs[MONKEY_TYPE] == TYPE_NUMBER:
        monkey = MonkeyNumber(monkey_specs[MONKEY_NAME], 
                              monkey_specs[NUMBER])
        
        return monkey
    
    if monkey_specs[MONKEY_TYPE] == TYPE_OP:
        
        monkey_child_1 = process_monkey_dict_2(monkey_dict, monkey_specs[PARAM_1])
        monkey_child_2 = process_monkey_dict_2(monkey_dict, monkey_specs[PARAM_2])
        
        match monkey_specs[OPERATOR]:
            case MonkeyOperator.OP_ADD:
                monkey_op = operator.add
            case MonkeyOperator.OP_SUB:
                monkey_op = operator.sub
            case MonkeyOperator.OP_MUL:
                monkey_op = operator.mul
            case MonkeyOperator.OP_DIV:
                monkey_op = operator.floordiv
        
        monkey = MonkeyOperation(monkey_specs[MONKEY_NAME],
                                 monkey_op,
                                 monkey_child_1,
                                 monkey_child_2)
        
        return monkey


class Monkey:
    
    def __init__(self, monkey_name):
        self.monkey_name = monkey_name


class MonkeyNumber(Monkey):
    
    def __init__(self, monkey_name, number):
        super().__init__(monkey_name)
        
        self.number = number
    
    def value(self):
        return self.number
    
    def is_solver(self):
        return False
    
    def solve(target):
        return self.value()


class MonkeyOperation(Monkey):
    
    def __init__(self, monkey_name, operator, param_1, param_2):
        super().__init__(monkey_name)
        
        self.operator = operator
        self.param_1 = param_1
        self.param_2 = param_2
    
    def value(self):
        return self.operator(self.param_1.value(), self.param_2.value())
    
    def is_solver(self):
        return self.param_1.is_solver() or self.param_2.is_solver()
    
    def solve(self, target=None):
        
        param_1_solver = self.param_1.is_solver()
        param_2_solver = self.param_2.is_solver()
        
        if not (param_1_solver or param_2_solver):
            return self.value()
        
        match self.operator:
            case operator.add:
                if param_1_solver:
                    new_target = target - self.param_2.value()
                    
                    return self.param_1.solve(new_target)
                
                if param_2_solver:
                    new_target = target - self.param_1.value()
                    
                    return self.param_2.solve(new_target)
            
            case operator.sub:
                if param_1_solver:
                    new_target = target + self.param_2.value()
                    
                    return self.param_1.solve(new_target)
                
                if param_2_solver:
                    new_target = self.param_1.value() - target
                    
                    return self.param_2.solve(new_target)
            
            case operator.mul:
                if param_1_solver:
                    new_target = target // self.param_2.value()
                    
                    return self.param_1.solve(new_target)
            
                if param_2_solver:
                    new_target = target // self.param_1.value()
                    
                    return self.param_2.solve(new_target)
            
            case operator.floordiv:
                if param_1_solver:
                    new_target = target * self.param_2.value()
                    
                    return self.param_1.solve(new_target)
                
                if param_2_solver:
                    new_target = self.param_1.value() // target
                    
                    return self.paraam_2.solve(new_target)
            
            case operator.eq:
                if param_1_solver:
                    return self.param_1.solve(self.param_2.value())
                
                if param_2_solver:
                    return self.param_2.solve(self.param_1.value())


class MonkeySolver(Monkey):
    
    def is_solver(self):
        return True
    
    def solve(self, target):
        return target





















