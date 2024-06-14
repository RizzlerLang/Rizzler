# lexer.py

class RizzlerLexer:
    def __init__(self, input_text):
        self.input_text = input_text

    def tokenize(self):
        tokens = []
        lines = self.input_text.splitlines()
        for line in lines:
            tokens.extend(self.tokenize_line(line))
        return tokens

    def tokenize_line(self, line):
        tokens = []
        line = line.strip()
        if line.startswith("line"):
            parts = line.split("=", 1)
            var_name = parts[0].split(" ")[1].strip()
            if var_name.isdigit():
                raise ValueError("Error: Variable name cannot be a full number")
            var_value = str(eval(parts[1].strip()))  # Convert value to string before storing
            tokens.append(("VARIABLE_DECLARATION", (var_name, var_value)))
        elif line.startswith("rizzline"):
            var_name = line.split(" ")[1].strip()
            tokens.append(("RIZZLINE", var_name))
        else:
            raise ValueError(f"Unknown command: {line}")
        return tokens
