import datetime

if __name__ == "__main__":
    with open('test.txt', 'a', encoding='utf-8') as file:
        file.write(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '\n')
