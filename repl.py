from llm_interaction import generate_text
from file_io import read_file, write_file

def start_repl():
    last_generated = ""
    while True:
        user_input = input(">> ").strip()
        
        if user_input.startswith("generate"):
            prompt = user_input[len("generate"):].strip()
            last_generated = generate_text(prompt)
            print(last_generated)
        
        elif user_input.startswith("read"):
            try:
                _, filename = user_input.split(" ", 1)
                content = read_file(filename)
                print(content)
            except ValueError:
                print("Usage: read <filename>")
        
        elif user_input.startswith("write"):
            try:
                _, filename = user_input.split(" ", 1)
                write_file(filename, last_generated)
                print(f"Content written to {filename}")
            except ValueError:
                print("Usage: write <filename>")
        
        elif user_input == "quit":
            break
        
        else:
            print("Invalid command. Type 'generate', 'read <filename>', 'write <filename>', or 'quit'.")

if __name__ == "__main__":
    start_repl()
