class ErrorNotNumber(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    try:
        num = input(
            'Enter a number for the list or press "w" to stop typing:')
        if num == 'w':
            break
        if not num.isdigit():
            raise ErrorNotNumber(num)
        my_list.append(int(num))
    except ErrorNotNumber as err:
        print(err, ' - Is not a number! Continue typing or press "w"')
print(f' list of the entered numbers: {my_list}')