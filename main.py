class Calculator:
    def __init__(self, init_value, init_atributes_number):
        self.__dict__['storage'] = {}
        self.atributes_number = init_atributes_number
        self.value = init_value
        self.counter = 0

    def __del__(self):
        print('ghjk')

    def __repr__(self):
        return self.storage

    def __str__(self):
        return str(self.storage)

    def __add__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        new_calculator = Calculator(self.value + value, self.atributes_number)
        for key in self.storage:
            new_calculator.__setattr__(key, self.storage[key])
        return new_calculator

    def __sub__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        new_calculator = Calculator(self.value - value, self.atributes_number)
        for key in self.storage:
            new_calculator.__setattr__(key, self.storage[key])
        return new_calculator

    def __mul__(self, other):
        value = other.value if isinstance(other, Calculator, ) else other
        new_calculator = Calculator(self.value * value, self.atributes_number)
        for key in self.storage:
            new_calculator.__setattr__(key, self.storage[key])
        return new_calculator

    def __truediv__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        new_calculator = Calculator(self.value / value, self.atributes_number)
        for key in self.storage:
            new_calculator.__setattr__(key, self.storage[key])
        return new_calculator

    def __pow__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        new_calculator = Calculator(self.value ** value, self.atributes_number)
        for key in self.storage:
            new_calculator.__setattr__(key, self.storage[key])
        return new_calculator

    def __setattr__(self, key, value):
        if key in self.storage:
            self.storage[key] = value
        elif key == 'atributes_number':
            self.storage[key] = value
        elif len(self.storage) < self.atributes_number + 3:
            self.storage[key] = value
        else:
            raise AttributeError

    def __getattr__(self, item):
        return self.storage[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter<len(self.storage):
            self.counter = self.counter + 1
            return self.value
        else:
            self.counter = 0
            raise StopIteration


if __name__ == '__main__':
    calculator = Calculator(100, 3)
    calculator.some_atribute1 = 'znachenie'
    calculator.some_atribute2 = 'znachenie'
    calculator.some_atribute3 = 'znachenie'
    print(calculator + 7)
    for i in calculator:
        print(i)
    print(calculator.counter)
    print(calculator)
