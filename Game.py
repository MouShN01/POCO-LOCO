def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question + " (y/n)? ").lower()
    return response 

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("Вы запустили модуль games, а не импортировали его (import games).")
    input("\n\nНажмите Enter, что бы выйти.")