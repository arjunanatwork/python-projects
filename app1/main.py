

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                row = f"{index+1}-{item.strip('\n')}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1
            new_todo = input("Enter new todo:")
            todos[number] =  new_todo
        case 'complete':
            number = int(input("Number of the todo to complete:"))
            todos.pop(number-1)
        case 'exit':
            break

print("Goodbye!")
