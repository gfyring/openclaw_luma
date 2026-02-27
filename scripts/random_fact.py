#!/usr/bin/env python

import random
import argparse
import sys

# Define facts by category
facts = {
    'roman': [
        "The Roman Empire lasted over 1000 years, from 27 BC to 476 AD.",
        "Julius Caesar was stabbed 23 times by a group of senators on the Ides of March.",
        "The Colosseum in Rome could hold up to 80,000 spectators for gladiatorial contests.",
        "Romans invented concrete, which allowed for revolutionary architecture like the Pantheon.",
        "Emperor Nero allegedly fiddled while Rome burned in 64 AD."
    ],
    'general': [
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896, lasting 38 minutes.",
        "Octopuses have three hearts: two pump blood through the gills, and one through the body.",
        "A flock of crows is known as a murder.",
        "Honey never spoils; archaeologists have found pots of edible honey in ancient Egyptian tombs.",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion."
    ]
}

def main():
    parser = argparse.ArgumentParser(description="Generate a random fact from a specified category.")
    parser.add_argument('--category', default='roman', choices=facts.keys(), help='Fact category (roman or general)')
    args = parser.parse_args()

    category_facts = facts.get(args.category)
    if not category_facts:
        print(f"Error: Invalid category '{args.category}'", file=sys.stderr)
        sys.exit(1)

    print(random.choice(category_facts))

if __name__ == "__main__":
    main()
