"""
This module is to test the tokeniser functionality
"""
import os
import base64
import pytest
import tokeniser


@pytest.fixture(name='input_value')
def parameter():
    """
    Initialise the parameters to use by other function
    :return: list of parameter to the other functions
    """
    appname_val = 'test_tokeniser.py'
    first_name = ('Andrew', 'John', 'Clifford', 'Jinna', 'Andy', 'Joe'
                  , 'Joesph', 'Thomas', 'Praveen', 'Edward')
    input_file = os.path.join(os.path.abspath('.'), 'create_csv.csv')
    output_folder = os.path.join(os.path.abspath('.'),'tokenised_output')
    number_of_lines = 100
    return [appname_val, first_name, input_file, output_folder,number_of_lines ]


def test_spark_init(input_value):
    """
    Test the spark initialisation
    :param input_value: as a list of inputs from fixtures
    :return:
    """
    spark = tokeniser.spark_init(input_value[0])
    assert isinstance(spark,object),'spark initialisation failed'


def test_tokeniser(input_value):
    """
    Test the tokeniser & detokeniser functionality with base64
    :param input_value: as a list of inputs from fixtures
    """
    string_input = input_value[1][1]
    tokenised_value = base64.b64encode(string_input.encode('ascii'))
    untokenised_value = base64.b64decode(tokenised_value).decode('ascii')
    assert untokenised_value == string_input,'Tokenisation is failed'


def test_load_file(input_value):
    """
    Test the load file function
    :param input_value: as a list of inputs from fixtures
    """
    app_name = input_value[0]
    file_name = input_value[2]
    spark = tokeniser.spark_init(app_name)
    data = tokeniser.load_file(file_name,spark)
    assert data.count() ==  100,"Load didn't work properly"


def test_write_file(input_value):
    """
    Test the write file
    :param input_value: as a list of inputs from fixtures
    """
    folder_name = input_value[3]
    app_name = input_value[0]
    file_name = input_value[2]
    number_of_lines = input_value[4]
    spark = tokeniser.spark_init(app_name)
    data = tokeniser.load_file(file_name, spark)
    tokeniser.write_file(data,folder_name)
    data_after_writing = spark.read.parquet(folder_name)
    data_count = data_after_writing.count()
    assert data_count == number_of_lines, 'write failed'
