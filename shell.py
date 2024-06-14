# shell.py

import sys
from lexer import RizzlerLexer
from rizzler_interpreter import RizzlerInterpreter

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if file_path.startswith("run "):
            file_path = file_path[4:].strip()
            execute_file(file_path)
        else:
            print("Invalid command. Use 'run example.rzl' to execute a Rizzler script.")
    else:
        print("Welcome to the Rizzler shell!")
        print('Type "exit" to quit.')

        interpreter = RizzlerInterpreter()
        while True:
            input_line = input("Rizzler> ").strip()
            if input_line.lower() == "exit":
                break
            elif input_line.startswith("rzl "):
                file_path = input_line[4:].strip()
                execute_file(file_path)
            else:
                try:
                    lexer = RizzlerLexer(input_line)
                    tokens = lexer.tokenize()

                    interpreter.run(tokens)
                except Exception as e:
                    print(f"Error: {e}")

def execute_file(file_path):
    try:
        with open(file_path, 'r') as file:
            input_text = file.read()
        lexer = RizzlerLexer(input_text)
        tokens = lexer.tokenize()

        interpreter = RizzlerInterpreter()
        interpreter.run(tokens)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()