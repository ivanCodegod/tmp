from task2 import description, action

listt = []

print("Напиши 'help' чтоб увидеть список доступных команд")
while True:
    inp = input()
    if inp == 'q':
        print("Программа остановленна")
        break
    elif inp == 'help':
        description()
    elif inp == 'action':
        action(inp)
    else:
        description()
