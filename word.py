"""
input: plain text word
output: sorted addresses list
function: Convert plain text to the list of vanity-addresses
"""
from subprocess import Popen, PIPE
import argparse
import base58

UNIT_SIZE = 2

def sorted_keys(text):
        list = [text[i:i+UNIT_SIZE] for i in range(0, len(text), UNIT_SIZE)]

        pairs = []
        for i in list:
                p = Popen(['vanitygen', '1'+i], stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output, err = p.communicate(b"input data that is passed to subprocess' stdin")
                rc = p.returncode
                some_list = output.splitlines()

                address = [s for s in some_list if "Address" in s][0][9:]
                privkey = [s for s in some_list if "Privkey" in s][0][9:]

                pairs.append({'address': address, 'privkey': privkey})

        return pairs

def b64tob58(text, n):
    '''return the list of base58-strings with n-chars lenght'''
    line = str(base58.b58encode(text))
    #todo: also should return count of chars in the last string
    return [line[i:i+n] for i in range(0, len(line), n)]



def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--text', help='word to convert')
        parser.add_argument('--number', help='number of bites that to reserve in address')
        args = parser.parse_args()

        text = vars(args)['text']
        n = int(vars(args)['number'])


        print b64tob58(text, n)


if __name__ == "__main__":
    main()
