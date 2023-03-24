import random
import string
import sys


def email_write(file):
    with open(file, 'w') as f:
        for i in range(1000000):
            username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            domain = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
            email = f'{username}@{domain}.com'
            f.write(email+"\n")


if __name__ == '__main__':
    email_write(sys.argv[1])
    print(f'writing emails in {sys.argv[1]} is completed')
    email_write(sys.argv[2])
    print(f'writing emails in {sys.argv[2]} is completed')
