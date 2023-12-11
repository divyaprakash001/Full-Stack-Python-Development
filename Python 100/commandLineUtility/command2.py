import argparse

parser = argparse.ArgumentParser()

# add command line arguments 
parser.add_argument('file url', help='description of arg1')
parser.add_argument('output', help='name of file after download of arg1')

# parse the arguments
args = parser.parse_args()

# use the arguments in your code
print(args.arg1)
print(args.arg2)