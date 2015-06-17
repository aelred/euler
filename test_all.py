import hashlib
import subprocess
import os

with open('answers.txt') as f:
    MD5_ANSWERS = [answer.strip() for answer in f.readlines()]

FILE_DIR = os.path.dirname(os.path.realpath(__file__))

LANGUAGES = [
    ('python3', 'py'),
    ('runhaskell', 'hs'),
]


def test_all():
    # try each problem
    for number, md5 in enumerate(MD5_ANSWERS):
        # try each known language in turn
        for interpreter, extension in LANGUAGES:
            fname = 'q' + str(number + 1) + '.' + extension
            path = os.path.join(FILE_DIR, fname)
            if os.path.isfile(path):
                print(number+1)
                answer = subprocess.check_output([interpreter, path]).rstrip()
                assert hashlib.md5(answer).hexdigest() == MD5_ANSWERS[number]
                break


if __name__ == '__main__':
    test_all()
