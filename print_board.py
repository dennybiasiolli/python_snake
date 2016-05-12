import os
import time
from threading import Thread
from queue import Queue

queue_directions = Queue()


class PrintBoardThread(Thread):

    def __init__(self, width, height, stringa_comandi, refresh_rate_ms):
        Thread.__init__(self)
        self.refresh_rate_ms = refresh_rate_ms
        self.stringa_comandi = stringa_comandi
        self.board = Board(width, height)
        self.board.add_point(Point((width // 4) - 4, height // 2))
        self.board.add_point(Point((width // 4) - 3, height // 2))
        self.board.add_point(Point((width // 4) - 2, height // 2))
        self.board.add_point(Point((width // 4) - 1, height // 2))
        self.head_position = Point(width // 4, height // 2)
        self.board.add_point(self.head_position)
        self.seconds = 0
        self.current_direction = 'right'

    def run(self):
        while True:
            os.system('clear')
            if not queue_directions.empty():
                direction = queue_directions.get()
                if(direction in ['right', 'left', 'up', 'down']):
                    self.current_direction = direction
            self.board.move_points(self.current_direction)
            print(self.board)
            print('\rFrames elapsed %d' % self.seconds)
            print('\r%s\r' % self.stringa_comandi)
            if self.board.is_dead:
                print('\rYOU DIED!\r')
                break
            self.seconds += 1
            time.sleep(self.refresh_rate_ms / 1000)
        return


class Board(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__board = []
        self.__board.append(list('\u2588' + '\u2588' * (self.width - 2) + '\u2588'))
        for i in range(self.height - 2):
            self.__board.append(list('\u2588' + ' ' * (self.width - 2) + '\u2588'))
        self.__board.append(list('\u2588' + '\u2588' * (self.width - 2) + '\u2588'))
        self.points = []
        self.last_direction = None
        self.is_dead = False

    def __repr__(self):
        ret_val = '\r'
        for line in self.__board:
            ret_val += ''.join(line) + '\r\n'
        return ret_val

    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
            self.__board[point.y][point.x] = '*'

    def remove_last_point(self):
        last_point = self.points.pop(0)
        if isinstance(last_point, Point):
            self.__board[last_point.y][last_point.x] = ' '

    def point_is_over_borders(self, point):
        return (
            point.x == 0
            or
            point.x == self.width - 1
            or
            point.y == 0
            or
            point.y == self.height - 1
        )

    def move_points(self, direction):
        new_point = Point(self.points[-1].x, self.points[-1].y)
        if not (
            (self.last_direction == 'right' and direction == 'left')
            or
            (self.last_direction == 'left' and direction == 'right')
            or
            (self.last_direction == 'up' and direction == 'down')
            or
            (self.last_direction == 'down' and direction == 'up')
        ):
            self.last_direction = direction
        new_point.move(self.last_direction)
        if self.point_is_over_borders(new_point):
            self.is_dead = True
        self.add_point(new_point)
        self.remove_last_point()


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str({'x': self.x, 'y': self.y})

    def move(self, direction):
        if direction == 'right':
            self.x += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'up':
            self.y -= 1
