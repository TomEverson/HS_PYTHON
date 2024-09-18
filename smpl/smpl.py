class SmplInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def find_next_empty_line(self, lines, i):
        while i < len(lines):
            if not lines[i].strip():  # Check if the line is empty or contains only whitespace
                return i
            i += 1
        return -1  # Return -1 if no empty line is found

    def evaluate_expression(self, expression):
        tokens = expression.split()
        if len(tokens) == 1:  # Single variable or value
            var_name = tokens[0]
            if var_name.isdigit():  # Handle numeric values
                return int(var_name)
            # Handle string literals
            elif var_name.startswith('"') and var_name.endswith('"'):
                return var_name.strip('"')
            elif var_name in self.variables:  # Handle variables
                return self.variables[var_name]
            else:
                raise ValueError(f"Variable {var_name} not found")
        else:  # Basic arithmetic expression
            left = tokens[0]
            operator = tokens[1]
            right = tokens[2]
            left_value = self.evaluate_expression(left)
            right_value = self.evaluate_expression(right)
            if operator == '+':
                if isinstance(left_value, int) and isinstance(right_value, int):
                    return left_value + right_value
                elif isinstance(left_value, str) and isinstance(right_value, str):
                    return left_value + right_value
                else:
                    raise ValueError("Cannot add different types")
            else:
                raise ValueError(f"Unsupported operator {operator}")

    def define_function(self, name, params, body):
        self.functions[name] = {'params': params, 'body': body}

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
            # Handle string literals
            if var_name.startswith('"') and var_name.endswith('"'):
                print(var_name.strip('"'))
            elif var_name in self.variables:
                print(self.variables[var_name])
            else:
                print(f"Variable {var_name} not found")
        elif tokens[0] == 'IF':
            condition = ' '.join(tokens[1:])
            if self.evaluate_condition(condition):
                return True
            return False

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

                    while i < len(lines) and not lines[i].strip().startswith('IF'):
                        self.execute_statement(lines[i].strip())
                        if self.find_next_empty_line(lines, i):
                            i = self.find_next_empty_line(lines, i + 1)
                            break

                if condition_result == False:

                    if i < len(lines) and lines[i].strip().startswith('IF'):
                        i += 2

                    if i < len(lines) and lines[i].strip().startswith('ELSE'):
                        i += 1
                        while i < len(lines) and not lines[i].strip().startswith('IF'):
                            self.execute_statement(lines[i].strip())
                            i += 1

            else:

                self.execute_statement(line)
                print(self.functions)
                i += 1
