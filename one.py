def operations (a: float, b: float, o:chr) -> float:
    match o:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":  
            return a * b
        case "/":
            return a / b
        
if __name__ == "__main__":
    num1: float = float(input("Enter first number: "))
    num2: float = float(input("Enter second number: "))
    op: chr = input("Enter the operation you want to perform between the two numbers (+, -, * or /): ")
    valid_input : bool = False
    while valid_input == False:
        if op in ['+', '-', '*', '/']:
            valid_input = True
        else:
            op: chr = input("Please enter one of the four symbols to do an operation between {} and {} (+, -, * or /): ".format(num1, num2))
    print("The result of the operation {} {} {} is:".format(num1, op, num2), operations(num1, num2, op))