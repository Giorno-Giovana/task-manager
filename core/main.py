import datetime
import os

if __name__ == "__main__":
    # print(datetime.datetime.now())
    with open('test.txt', 'a', encoding='utf-8') as file:
        file.write(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '\n')

        # os.path.dirname(os.path.abspath(__file__)) +