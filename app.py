import json
import argparse
import sys

'''
JSON-Parser P

Parsing is made up of two stages
1. Lexical analysis
- Dividing a sequence of characters into meaningful chunks, aka tokens

2. Syntactic analysis
- Analysing the list of tokens to match it to a formal grammer 
'''

'''
Step.1 
Parse a valid JSON object
Parse an invalid JSON file

1. Report to standard output a suitable message + exit code 
'''

parser = argparse.ArgumentParser(
                    prog='JSON-Parser',
                    description='Lexical and Syntactic analysis of JSON objects.',
                    epilog='Made in NYC with ♡')

parser.add_argument('filename', nargs='?', default=None)

parser.add_argument('-p', '--parse', action='store_true')

args = parser.parse_args()

def is_json(file):
    try:
        json.loads(file)
        print("Loaded Successfully")
        return True
    except:
        print("Invalid")
        return False

if args.parse and args.filename:
    with open(args.filename, 'r') as file:
        content = file.read()
        is_json(content)


