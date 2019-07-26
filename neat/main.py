"""
author: Bazarovay@github.com
This is the primary class
"""
import numpy as np


def main(test_argument):
    """
    This function is to test the documentation


    :param test_argument: A variable which contains a string value
    return: does not return anything
    """
    product = np.multiply([[1]],[[1]])
    print(test_argument, product)
    return None


if __name__ == "__main__":
    main("test_argument")
