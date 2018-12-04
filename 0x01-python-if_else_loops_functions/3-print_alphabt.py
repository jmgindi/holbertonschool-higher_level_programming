#!/usr/bin/python3
print(''.join(
        [chr(a) for a in range(ord('a'), ord('z') + 1)
         if a not in [ord('e'), ord('q')]]
    ),
end = '')
