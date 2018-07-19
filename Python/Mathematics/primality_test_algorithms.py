# coding=utf-8

"""
Given a number n, check if it is prime or not.

There are many ways to check if number is prime or not. We will discuss 3 methods here, namely:
1. Naive method - O(√n)
2. Fermat's Method - O(k log(n))

"""


def is_prime_naive(number):
    """
    Check if number is prime

    :param number: Integer - Number to be tested
    :return: Boolean
    """

    if number <= 1:
        return False
    if number <= 3:
        return True

    i = 5
    while i * i <= n:
        if n %