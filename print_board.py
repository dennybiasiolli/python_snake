import os
import time
from threading import Thread


class PrintBoardThread(Thread):

    def __init__(self, width, height, stringa_comandi, refresh_rate_ms):
        Thread.__init__(self)
        self.refresh_rate_ms = refresh_rate_ms
        self.stringa_comandi = stringa_comandi
        self.count = 10
        self.board = Board(width, height)
        self.head_position = Point(width // 2, height // 2)

    def run(self):
        print('Counting down from', self.count)
        while self.count >= 0:
            os.system('clear')
            print(self.board)
            print('\rCounting down %d' % self.count)
            print('\r%s\r' % self.stringa_comandi)
            print(self.head_position)
            self.count -= 1
            time.sleep(500 / 1000)
        return


class Board(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__board = []
        self.__board.append('#' * self.width)
        for i in range(self.height - 2):
            self.__board.append('#' + ' ' * (self.width - 2) + '#')
        self.__board.append('#' * self.width)

    def __repr__(self):
        ret_val = ''
        for line in self.__board:
            ret_val += line + '\r\n'
        return ret_val

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str({'x': self.x, 'y': self.y})
