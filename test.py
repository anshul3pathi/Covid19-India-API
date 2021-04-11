from datetime import datetime


FORMAT = '%Y-%m-%d %H:%M:%S.%f'

# with open("should_fetch.txt", 'w') as file:
#     file.write(str(datetime.now()))

try:
    with open("should_fetch.txt") as file:
        print(file.read())
except FileNotFoundError:
    with open("should_fetch.txt", 'w') as file:
        file.write(str(datetime.now()))


