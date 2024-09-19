import re


class BreakException(Exception):
    pass


class SmplInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = []

    def find_next_empty_line(self, lines, i):
        while i < len(lines):
            if not lines[i].strip():
                return i
            i += 1
        return -1

    def split_preserve_leading_spaces(self, text):
        leading_spaces = re.match(r'\s*', text).group(0)
        rest_of_string = text.strip()

        # Calculate the number of leading spaces
        space_count = len(leading_spaces)

        # Calculate preserved spaces based on multiples of 4
        preserved_spaces = ' ' * (space_count // 4 * 4)

        # Split the rest of the string by spaces
        result = [preserved_spaces] + rest_of_string.split(' ')
        return result

    def evaluate_expression(self, expression):
        tokens = expression.split()
        if len(tokens) == 1:
            var_name = tokens[0]
            if var_name.isdigit():
                return int(var_name)
            elif var_name.startswith('"') and var_name.endswith('"'):
                return var_name.strip('"')
            elif var_name in self.variables:
                return self.variables[var_name]
            else:
                raise ValueError(f"Variable {var_name} not found")
        else:
            left = tokens[0]
            operator = tokens[1]
            right = tokens[2]
            left_value = self.evaluate_expression(left)
            right_value = self.evaluate_expression(right)

            if operator == '+':
                if isinstance(left_value, (int, str)) and isinstance(right_value, (int, str)):
                    return left_value + right_value
                else:
                    raise ValueError("Cannot add different types")
            elif operator == '-':
                if isinstance(left_value, int) and isinstance(right_value, int):
                    return left_value - right_value
                else:
                    raise ValueError("Subtraction only supported for integers")
            elif operator == '*':
                if isinstance(left_value, int) and isinstance(right_value, int):
                    return left_value * right_value
                else:
                    raise ValueError(
                        "Multiplication only supported for integers")
            elif operator == '/':
                if isinstance(left_value, int) and isinstance(right_value, int):
                    if right_value == 0:
                        raise ValueError("Division by zero")
                    return left_value // right_value  # Integer division
                else:
                    raise ValueError("Division only supported for integers")
            else:
                raise ValueError(f"Unsupported operator {operator}")

    def evaluate_condition(self, condition):
        tokens = condition.split()

        if len(tokens) == 5 and tokens[1] == 'IS' and tokens[2] == 'EQUAL' and tokens[3] == 'TO':
            left = tokens[0]
            right = tokens[4]

            left_value = self.evaluate_expression(left)
            right_value = self.evaluate_expression(right)
            return left_value == right_value
        else:
            raise SyntaxError("Invalid condition")

    def extract_function_name_and_args(self, line):
        if '(' in line and line.endswith(')'):
            func_name = line.split('(')[0].strip()
            arg_string = line.split('(')[1].rstrip(')')
            args = [arg.strip() for arg in arg_string.split(
                ',')] if arg_string else []
            return func_name, args
        return None

    def add_function_body(self, func, statement):
        func['body'].append(statement)
        return func

    def define_function(self, statement):

        pattern = r'FUNCTION\s+(\w+)\(([^)]*)\)'
        match = re.match(pattern, statement)

        if match:
            func_name, params = match.groups()
            params = params.split(",")
            params = [param.strip() for param in params]
            func = {
                "name": func_name,
                "params": params,
                "body": []
            }

            return func

    def execute_function(self, func_name, args):
        # Find the function definition
        func = next(
            (f for f in self.functions if f['name'] == func_name), None)
        if not func:
            raise ValueError(f"Function {func_name} not found")

        # Create a local context for parameters
        local_vars = dict(zip(func['params'], args))

        # Execute the body of the function with replaced parameters
        for index, line in enumerate(func['body']):
            for param, value in local_vars.items():
                func['body'][index] = func['body'][index].replace(
                    param, value)

        # Execute Code
        try:
            for statement in func['body']:
                self.execute_statement(statement.strip())
        except BreakException:
            pass

    def execute_statement(self, statement):
        if not statement.strip():  # Skip empty lines
            return

        tokens = statement.split()
        if tokens[0] == 'LET' and tokens[2] == 'BE':
            var_name = tokens[1]
            expression = ' '.join(tokens[3:])
            self.variables[var_name] = self.evaluate_expression(expression)
        elif tokens[0] == 'OUTPUT':
            var_name = tokens[1]
            if var_name.startswith('"') and var_name.endswith('"'):
                print(var_name.strip('"'))
            elif var_name in self.variables:
                print(self.variables[var_name])
            else:
                output_expression = ' '.join(tokens[1:])
                try:
                    result = self.evaluate_expression(
                        output_expression)  # Evaluate the expression
                    print(result)
                except ValueError as e:
                    print(e)
        elif tokens[0] == 'IF':
            condition = ' '.join(tokens[1:])
            if self.evaluate_condition(condition):
                return True
            return False
        elif tokens[0] == 'BREAK':
            raise BreakException()
        else:
            raise SyntaxError("Invalid statement")

    def run_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        i = 0
        while i < len(lines):

            line = lines[i].strip()
            if line.startswith('IF'):

                condition_result = self.execute_statement(line)
                if condition_result:
                    i += 1

                    while i < len(lines) and self.split_preserve_leading_spaces(lines[i])[0] == "    ":
                        self.execute_statement(lines[i].strip())
                        i += 1

                    i = self.find_next_empty_line(lines, i) + 1

                if condition_result == False:

                    if i < len(lines) and lines[i].strip().startswith('IF'):
                        i = self.find_next_empty_line(lines, i) + 1

                    if i < len(lines) and lines[i].strip().startswith('ELSE'):
                        i += 1
                        while i < len(lines) and self.split_preserve_leading_spaces(lines[i])[0].isspace():
                            self.execute_statement(lines[i].strip())
                            i += 1
                        i = self.find_next_empty_line(lines, i) + 1

            elif line.startswith("FUNCTION"):
                func = self.define_function(line)
                i += 1
                while i < len(lines) and self.split_preserve_leading_spaces(lines[i])[0].isspace():
                    func = self.add_function_body(func, lines[i].strip())
                    i += 1
                self.functions.append(func)
                i = self.find_next_empty_line(lines, i) + 1

            else:
                if self.extract_function_name_and_args(line):
                    func_name, args = self.extract_function_name_and_args(line)
                    if line.startswith(func_name):
                        self.execute_function(func_name, args)
                        i += 1
                else:
                    self.execute_statement(line)
                    i += 1
