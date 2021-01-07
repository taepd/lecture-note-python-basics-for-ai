import argparse

parser = argparse.ArgumentParser(description="Sum two integers.")

parser.add_argument(
    "-a", "--a_value", dest="a", help="A integers", type=int, required=True
)
parser.add_argument(
    "-b", "--b_value", dest="b", help="B integers", type=int, required=True
)

args = parser.parse_args()
print(args)
print(args.a)
print(args.b)
print(args.a + args.b)
