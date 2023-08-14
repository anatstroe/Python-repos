def sum(a: float, b: float) -> float:
    return float(a) + float(b)

def diff(a: float, b: float) -> float:
    return float(a) - float(b)

def prod(a: float, b: float) -> float:
    return float(a) * float(b)

def div(a: float, b: float) -> float:
    return float(a) / float(b)

def pow(a: float, b: float) -> float:
    return float(a) ** float(b)

def root(a: float, b: float) -> float:
    return float(a) ** (1 / float(b))

def log(a: float, b: float) -> float:
    return float(math.log(a, b))


def ln(a: float) -> float:
    return float(math.log(a))

def factorial(a: float) -> float:
    return float(math.factorial(a))

def gcd(a: float, b: float) -> float:
    return float(math.gcd(a, b))

def lcm(a: float, b: float) -> float:
    return float(math.lcm(a, b))

# define calculator's operations
operations = {
    '+': sum,
    '-': diff,
    '*': prod,
    '/': div,
    '^': pow,
    'root': root,
    'log': log,
    'ln': ln,
    '!': factorial,
    'gcd': gcd,
    'lcm': lcm
}

def two_args_operation(operation):
    while True:
        try:
            a = float(input('Enter first number: '))
            b = float(input('Enter second number: '))
            return operations[operation](a, b)
        except:
            print('Error: invalid input')
            continue

def one_arg_operation(operation):
     while True:
        try:
            a = float(input('Enter number: '))
            return operations[operation](a)
        except:
            print('Error: invalid input')
            continue
    
# define cases for calculator's operations

def case_sum():
    return two_args_operation('+')

def case_diff():
    return two_args_operation('-')

def case_prod():
    return two_args_operation('**')

def case_div():
    return two_args_operation('/')

def case_pow():
    return two_args_operation('^')

def case_root():
    return two_args_operation('root')

def case_log():
    return two_args_operation('log')

def case_ln():
    return one_arg_operation('ln')

def case_factorial():
    return one_arg_operation('!')

def case_gcd():
    return two_args_operation('gcd')

def case_lcm():
    return two_args_operation('lcm')

switcher = {
    '1': case_sum,
    '2': case_diff,
    '3': case_prod,
    '4': case_div,
    '5': case_pow,
    '6': case_root,
    '7': case_log,
    '8': case_ln,
    '9': case_factorial,
    '10': case_gcd,
    '11': case_lcm
}

# define calculator's menu
def menu():
    print('1. Sum')
    print('2. Difference')
    print('3. Product')
    print('4. Division')
    print('5. Power')
    print('6. Root')
    print('7. Logarithm')
    print('8. Natural logarithm')
    print('9. Factorial')
    print('10. Greatest common divisor')
    print('11. Least common multiple')
    print('0. Exit')

# define calculator's main function
def main():
    while True:
        menu()
        choice = input('Enter your choice: ')
        if choice == '0':
            break
        else:
            try:
                print(switcher[choice]())
            except:
                print('Error: invalid input')

if __name__ == '__main__':
    main()