import os
import time
from threading import Thread


class PrintBoardThread(Thread):

    def __init__(self, width, height, stringa_comandi, refresh_rate_ms):
        Thread.__init__(self)
        self.refresh_rate_ms = refresh_rate_ms
        self.stringa_comandi = stringa_comandi
        self.board = Board(width, height)
        self.head_position = Point(width // 4, height // 2)
        self.seconds = 0

    def run(self):
        while True:
            os.system('clear')
            self.board.add_point(self.head_position)
            print(self.board)
            print('\rFrames elapsed %d' % self.seconds)
            print('\r%s\r' % self.stringa_comandi)
            print(self.head_position)
            self.seconds += 1
            time.sleep(500 / 1000)
        return


class Board(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__board = []
        self.__board.append(list('#' * self.width))
        for i in range(self.height - 2):
            self.__board.append(list('#' + ' ' * (self.width - 2) + '#'))
        self.__board.append(list('#' * self.width))

    def __repr__(self):
        ret_val = '\r'
        for line in self.__board:
            ret_val += ''.join(line) + '\r\n'
        return ret_val

    def add_point(self, point):
        if isinstance(point, Point):
            self.__board[point.y][point.x] = '*'

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str({'x': self.x, 'y': self.y})
