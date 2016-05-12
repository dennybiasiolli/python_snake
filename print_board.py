import os
import time
from threading import Thread


class PrintBoardThread(Thread):

    def __init__(self, width, height, stringa_comandi, count):
        Thread.__init__(self)
        self.width = width
        self.height = height
        self.count = count
        self.stringa_comandi = stringa_comandi

    def run(self):
        print('Counting down from', self.count)
        while self.count >= 0:
            os.system('clear')
            print('\r' + '#' * self.width)
            for i in range(self.height - 2):
                print('\r#' + ' ' * (self.width - 2) + '#')
            print('\r' + '#' * self.width)
            print('\rCounting down %d' % self.count)
            print('\r%s\r' % self.stringa_comandi)
            self.count -= 1
            time.sleep(1)
        return
