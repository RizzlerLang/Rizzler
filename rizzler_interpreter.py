# rizzler_interpreter.py

class RizzlerInterpreter:
    def __init__(self):
        self.variables = {}

    def run(self, tokens):
        for token_type, token_value in tokens:
            if token_type == "VARIABLE_DECLARATION":
                self.execute_variable_declaration(*token_value)
            elif token_type == "RIZZLINE":
                self.execute_rizzline(token_value)
            else:
                raise ValueError(f"Unknown command: {token_type}")

    def execute_variable_declaration(self, var_name, var_value):
        self.variables[var_name] = var_value

    def execute_rizzline(self, var_name):
        # Convert var_name to string if it's not already
        if not isinstance(var_name, str):
            var_name = str(var_name)
        
        # Check if var_name ends with a single or double quote and ignore it
        if var_name.endswith('"') or var_name.endswith("'"):
            var_name = var_name[:-1]
        
        print(var_name)
