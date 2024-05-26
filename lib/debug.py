#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Example usage to test the classes
    author1 = Author("Alice")
    author2 = Author("Bob")

    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    author1.add_article(magazine1, "The Future of AI")
    author1.add_article(magazine2, "Wellness Trends 2024")
    author2.add_article(magazine1, "Blockchain Innovations")

    # Set a breakpoint to start debugging
    ipdb.set_trace()
