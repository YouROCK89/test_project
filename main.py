board = list(range(1, 10))

wins_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")


def take_input(player_token):
    while True:
        value = input("Ход: " + player_token)
        if not (value in "123456789"):
            print("Ошибка! Повторите.")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("Данная клетка занята. Попробуйте другую")
            continue
        board[value - 1] = player_token
        break


def check_win():
    for j in wins_comb:
        if (board[j[0] - 1]) == (board[j[1] - 1]) == (board[j[2] - 1]):
            return board[j[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 3:
            winer = check_win()
            if winer:
                draw_board()
                print(winer, "победил!")
                break
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья!")
            break


main()
