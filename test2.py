def calculator(expression):
    """
    Evaluates a mathematical expression string recursively.

    Args:
      expression: The mathematical expression string to evaluate.

    Returns:
      The result of the evaluated expression.

    Raises:
      ValueError: If the expression is invalid (misplaced operators or parentheses).
    """

    def evaluate(expr):
        """
        Recursively evaluates a sub-expression.
        """
        if not expr:
            return 0
        if expr.isdigit():
            return int(expr)
        if expr[0] == '(':
            closing_paren = find_closing_paren(expr)
            if closing_paren == len(expr) - 1:
                return evaluate(expr[1:closing_paren])
            else:
                return evaluate_operation(evaluate(expr[1:closing_paren]), expr[closing_paren + 1], evaluate(expr[closing_paren + 2:]))
        else:
            for i in range(len(expr) - 1, -1, -1):
                if expr[i] in ('+', '-'):
                    return evaluate_operation(evaluate(expr[:i]), expr[i], evaluate(expr[i + 1:]))

    def find_closing_paren(expr):
        """
        Finds the index of the closing parenthesis matching the first opening parenthesis.
        """
        count = 1
        for i in range(1, len(expr)):
            if expr[i] == '(':
                count += 1
            elif expr[i] == ')':
                count -= 1
            if count == 0:
                return i
        raise ValueError("Invalid expression: Misplaced parentheses")

    def evaluate_operation(left, operator, right):
        """
        Evaluates a single operation.
        """
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ValueError("Division by zero")
            return left / right
        else:
            raise ValueError("Invalid expression: Misplaced operator")

    return evaluate(expression)