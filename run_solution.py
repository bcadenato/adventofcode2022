import sys

problem = int(sys.argv[1])

file_name = f'scripts/solution_{problem:02}.py'

print(f'Calling {file_name}')

exec(open(file_name).read())
