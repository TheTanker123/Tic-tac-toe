space = list(range(1, 10))

wins_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 9)]


def show_board():
    print("*************")
    for i in range(3):
        print("*", space[0 + i * 3], "*", space[1 + i * 3], "*", space[2 + i * 3], "*")
    print("*************")


def user_print_check(user_input):
    while True:
        g = input(f"Куда ставим {user_input}?")
        if not (g in '123456789'):
            print("Похоже, что вы ввели неправильный символ (Доступны числа от 1 до 9).")
            continue
            g = int(g)
            if str(space[g - 1]) in 'XO':
                print("Место занято, попробуйте другое!")
                continue
            space[g - 1] = user_input
            break


def winner_checker():
    for w in wins_combination:
        if space([w[0] - 1]) or space([w[1] - 1]) or space([w[2] - 1]):
            return space[w[1] - 1]
        else:
            return False


def construction():
    counter = 0
    while True:
        show_board()
        if counter % 2 == 0:
            user_print_check('X')
        else:
            user_print_check('O')
        if counter > 3:
            winner = winner_checker()
            if winner:
                show_board()
                print(f"{winner}ПОБЕДИЕЛЬ!")
                break
        counter += 1
        if counter > 8:
            show_board()
            print("НИЧЬЯ")
            break


construction()
