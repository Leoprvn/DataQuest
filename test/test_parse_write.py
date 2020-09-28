import sys
import pytest
import random
import string
import os
import parse_write


@pytest.fixture
def input_value():
    """
    Initalise the input parameters for other test function
    :return: list of the parametes flat_file_input,delimited_output_file,number_of_records,tot_num_char
    """
    flat_file_input = os.path.join(os.path.abspath('.'),'input.txt')
    delimited_output_file = os.path.join(os.path.abspath('.'),'output.dat')
    number_of_records = 100
    offset = [int(i) for i in str('5,12,3,2,13,7,10,13,20,13').split(',')]
    tot_num_char = sum(offset)
    lines = ['PZyqA,mHYVG9wWHw21,cDi,ah,iCxnOW7puwGFF,YFCWSF4,u2D6XpHSCj,pLlL5SQ0yKmze,Alx6adR2YdbguyUmYSQB,\
    Vl6e3ecMNOgfI','Q2XCo,sfsJRE8QxwPj,XSl,ay,LFRyQpFVQu1KM,xrcVmM0,AqSI4wQohk,HvbDSV1tdE72N,z1w4q48OPPGbIYz7hkMJ,\
    fW2vVhj8zbDhV']
    return [flat_file_input,delimited_output_file,number_of_records,tot_num_char,offset,lines]


def test_parse_file(input_value):
    """
    :param input_value:
    :return:
    """
    file_name = input_value[0]
    offset = input_value[4]
    number_of_records = input_value[2]
    parser = parse_write.parse_file(file_name, offset)
    del parser[0] #removes header
    assert len(parser) > 0 , 'There is no content in the file'
    assert len(parser) == number_of_records, 'number of records from the file has not processed, proccessed partially'
    for i in range(number_of_records):
        for i in range(len(offset)):
            assert len(parser[i].split(",")[i]) == offset[i],'split has failed'


def test_write_file(input_value):
    """
    :param input_value:
    :return:
    """
    file_name = input_value[1]
    number_of_records = input_value[3]
    offset = input_value[4]
    lines = input_value[5]
    parse_write.write_file(file_name, lines)
    assert os.path.exists(file_name)
    cnt = 0
    for count in open(file_name):
        cnt += 1
    assert cnt == len(lines)

