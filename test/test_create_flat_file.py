import os
import random
import string
import sys

import create_flat_file
import pytest


@pytest.fixture
def input_value():
    """
    Initalise the input parameters for other test function
    :return: list of the parametes flat_file_input,delimited_output_file,number_of_records,tot_num_char
    """
    flat_file_input = os.path.join(os.path.abspath('.'), 'input.txt')
    delimited_output_file = os.path.join(os.path.abspath('.'), 'output.dat')
    number_of_records = 100
    offset = [int(i) for i in str('5,12,3,2,13,7,10,13,20,13').split(',')]
    tot_num_char = sum(offset)
    return [flat_file_input, delimited_output_file, number_of_records, tot_num_char, offset]


# @pytest.mark.rand_char
def test_get_random_alphanumeric_character(input_value):
    """
    validates the length of characters generators
    :param input_value: number of characters needs to be generated
    :return: Error if we generate the more or less than the number of characters passed into \
    the function
    """
    length = input_value[3]
    random_str = create_flat_file.get_random_alphanumeric_character(length)
    assert len(random_str) == length


def test_create_flat_file(input_value):
    """
    Test the whether the files are created with the given number of lines
    :param input_value:
    :return:
    """
    file_name = input_value[0]
    number_of_lines = input_value[2]
    tot_num_char = input_value[3]
    create_flat_file.create_flat_file(file_name, number_of_lines, tot_num_char)
    assert os.path.exists(file_name)
    cnt = 0
    for count in open(file_name):
        cnt += 1
    assert cnt == number_of_lines
