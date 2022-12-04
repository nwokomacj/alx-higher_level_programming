#!/usr/bin/python3
#two different numbers separated by ,
for i in range(0, 10):
	for k in range(i + 1, 10):
            if (i != k and k != i):
                if i == 8 and k == 9:
                    print("{}{}" .format(i, k))
                else:
                    print("{}{}" .format(i, k), end=", ")
