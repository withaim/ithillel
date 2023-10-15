class NegativeDigitError(ValueError):
    """Exception raised when digit is negative in power and square_root calculations"""

    def __init__(self, digit):
        self.digit = digit
        self.message = f'Digit "{digit}" has to be positive for powering or square rooting'
        super().__init__(self.message)
        
        
class NotIntFloatError(ValueError):
    """Exception raised when input data neither int nor float for any action in calculations"""

    def __init__(self, args):
        self.args  = args
        self.types = {arg: type(arg) for arg in args}
        self.message = f'Values "{self.types}" has to be int or float to proceed calculation'
        super().__init__(self.message)


class Calculator:
    
    def is_int_or_float(self, x, y) :
        return isinstance(x, (int, float)) and isinstance(y, (int, float))
    
    def add(self, x, y):
        try:
            if not self.is_int_or_float(x, y) :
                raise NotIntFloatError((x, y))
            return x + y
        except NotIntFloatError as e :
            return f'Error: {e}'
        except Exception as e:
            return f'Error: {e}'

    def subtract(self, x, y):
        try:
            if not self.is_int_or_float(x, y) :
                raise NotIntFloatError((x, y))
            return x - y
        except NotIntFloatError as e :
            return f'Error: {e}'
        except Exception as e:
            return f'Error: {e}'

    def multiply(self, x, y):
        try:
            if not self.is_int_or_float(x, y) :
                raise NotIntFloatError((x, y))
            return round(x * y, 2)
        except NotIntFloatError as e :
            return f'Error: {e}'
        except Exception as e:
            return f'Error: {e}'

    def divide(self, x, y):
        try:
            if not self.is_int_or_float(x, y) :
                raise NotIntFloatError((x, y))
            return round(x / y, 5)
        except NotIntFloatError as e :
            return f'Error: {e}'
        except ZeroDivisionError as e:
            return f'Error: {e}'
        except Exception as e:
            return f'Error: {e}'

    def power(self, x, y):
        try:
            if not self.is_int_or_float(x, y) :
                raise NotIntFloatError((x, y))
            if y < 0:
                raise NegativeDigitError(y)
            return x ** y
        except NotIntFloatError as e :
            return f'Error: {e}'
        except NegativeDigitError as e:
            return f'Error: {e}'
        except Exception as e:
            return f'Error: {e}'

    def square_root(self, x):
        try:
            if not isinstance(x, (int, float)) :
                raise NotIntFloatError((x))
            if x < 0:
                raise NegativeDigitError(x)
            return round(x ** 0.5, 5)
        except NotIntFloatError as e :
            return f'Error: {e}'
        except NegativeDigitError as e:
            return f'Error: {e}'
        except Exception as e:
            return f'Error: {e}'




calc = Calculator()

print('Except add :' + calc.add('a', 3))
print('Normal add :' + str(calc.add(5, 3)))
print('Except sub :' + calc.subtract(10, [10,15])) # Не понимаю почему здесь выскакивает просто Exception но не NotIntFloatError когда прокидываю list
print('Normal sub :' + str(calc.subtract(10, 4)))
print('Except mul :' + calc.multiply(3, 'hello'))
print('Normal mul :' + str(calc.multiply(3, 0.1111)))
print('Except div :' + calc.divide(8, 0))
print('Except div :' + calc.divide(8, 'bbb'))
print('Normal div :' + str(calc.divide(10, 3)))
print('Except pow :' + calc.power(2, -3))
print('Except pow :' + calc.power(2, 'error'))
print('Normal pow :' + str(calc.power(2, 3)))
print('Except sqr :' + calc.square_root(-3))
print('Except sqr :' + calc.square_root((5,)))
print('Normal sqr :' + str(calc.square_root(8)))
