#!/usr/bin/python3
"""print the alphabet in lowercase, not followed by a new line."""

for let in range(97, 123):
  if chr(let) != 'q' and chr(let) != 'e':
    print("{}" .format(chr(let)), end="")
