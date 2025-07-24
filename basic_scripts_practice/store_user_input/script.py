OUTPUT_FILE = 'basic_scripts_practice/store_user_input/notes.txt'

def user_input():
    user_input = input("What do you want to write? ")
    
    exit_input = ['Exit', 'exit', 'EXIT']

    if user_input in exit_input:
        exit()
    else:
        return user_input

while True:
    try:
        notes = user_input()
        with open(OUTPUT_FILE, 'a') as file:
            file.write(f"{notes}\n")
    except:
        exit()
    