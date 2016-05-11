import sys

field_width = 50
field_height = 30
if len(sys.argv) > 1:
    field_width = int(sys.argv[1])
    if len(sys.argv) > 2:
        field_height = int(sys.argv[2])
print('field_width  %d' % field_width)
print('field_height %d' % field_height)
