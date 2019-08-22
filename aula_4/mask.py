import sys
import hashlib

if len(sys.argv) != 3:
    print('Número de argumentos inválidos')]
    sys.exit(1)

operation, filename = sys.argv[1:]

csv = []

with open(filename, 'r') as f:
    for line in f.readlines():
        csv.append(
            line.strip().split(';')
        )

