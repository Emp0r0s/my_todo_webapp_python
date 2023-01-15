FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read text file and returns from todo item"""
    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos

def write_todos(todoarg, filepath=FILEPATH):
    """Writes the todo item to the text file"""
    with open(filepath, "w") as file:
        file.writelines(todoarg)

