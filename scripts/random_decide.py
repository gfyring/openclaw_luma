import argparse
import random

parser = argparse.ArgumentParser(description="Random yes/no decider based on probability.")
parser.add_argument("--prob", type=float, required=True, help="Probability of 'yes' (0.0 to 1.0)")
args = parser.parse_args()

if random.random() < args.prob:
    print("yes")
else:
    print("no")