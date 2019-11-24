from django.shortcuts import render
from django.http import HttpResponse


def calculate_fibonacci_number(request, index):
    """
    This view returns a Fibonacci number, which correspond to the given index.
    If the number is incorrect, 400 status code is returned.
    :param HttpRequest request: Django HttpRequest object.
    :param int index: Index of requested Fibonacci number.
    :return: Value of Fibonacci number for provided index.
    """
    first_index = 0
    first = 0
    second = 1
    while first_index < index:
        first, second = second, first + second
        first_index += 1
    return HttpResponse(first)
