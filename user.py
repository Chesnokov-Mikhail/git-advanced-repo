import games
import logging_game

# анализ координат, введенных пользователем
def user_input(pole, arg):
    try:
        (user_in_line,user_in_column) = [int(x) for x in arg]
    except:
        logging_game.logger.exception(f'Ошибка установки координат пользователем: {arg}; pole: {pole}')
        return 'Необходимо ввести целые числа!'
    else:
        if games.check_coordinates(pole, (user_in_line, user_in_column)):
            return (user_in_line, user_in_column)
        else:
            logging_game.logger.info(f'Указанная ячейка занята: {arg}; pole: {pole}')
            return 'Указанная ячейка занята, выбирете другую: '