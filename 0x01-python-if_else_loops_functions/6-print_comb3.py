#!/usr/bin/python3
for i in range(8):
	for j in range(i + 1, 10):
		if i != j:
			print('{:d}{:d}, '.format(i, j), end='')
print('{:02d}\n'.format(89))
