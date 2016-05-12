import sys
import threading

import input_control
from print_board import PrintBoardThread


k = None


def main():
    field_width = 80
    field_height = 30
    if len(sys.argv) > 1:
        field_width = int(sys.argv[1])
        if len(sys.argv) > 2:
            field_height = int(sys.argv[2])
    print('field_width  %d' % field_width)
    print('field_height %d' % field_height)
    
    thread = PrintBoardThread(field_width, field_height, 'Input direction or press "q" to quit', 5)
    thread.daemon = True
    thread.start()

    while thread:
        k = input_control.get_key()
        if k == '[A':
            print('up')
        elif k == '[B':
            print('down')
        elif k == '[C':
            print('right')
        elif k == '[D':
            print('left')
        elif k == 'q':
            print('Quitting..')
            break
        else:
            pass  # print('Command not found')


if __name__ == '__main__':
    main()
