def get_todos(filepath="todos.txt"):
    """ Read a text file amd return the list of
    to-do items
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a to-d- item in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            row = f"{index+1}-{item.strip('\n')}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo:")
            todos[number] =  new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number-1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with this number.")
            continue
    elif 'exit' in user_action:
        break
    else:
        print("Invalid command!")


print("Goodbye!")
