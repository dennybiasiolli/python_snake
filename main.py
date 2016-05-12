import sys

import input_control
from print_board import PrintBoardThread, queue_directions


def main():
    k = None
    field_width = 80
    field_height = 30
    if len(sys.argv) > 1 and int(sys.argv[1]) > 50:
        field_width = int(sys.argv[1])
        if len(sys.argv) > 2 and int(sys.argv[2]) > 20:
            field_height = int(sys.argv[2])
    print('field_width  %d' % field_width)
    print('field_height %d' % field_height)

    thread = PrintBoardThread(
        field_width,
        field_height,
        'Input direction or press "q" to quit',
        250)
    thread.daemon = True
    thread.start()

    while thread:
        k = input_control.get_key()
        if k == '[A':
            queue_directions.put('up')
        elif k == '[B':
            queue_directions.put('down')
        elif k == '[C':
            queue_directions.put('right')
        elif k == '[D':
            queue_directions.put('left')
        elif k == 'q':
            print('Quitting..')
            break
        else:
            pass  # print('Command not found')


if __name__ == '__main__':
    main()
