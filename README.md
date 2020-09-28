# DataQuest

The Dockerised solution with Python scripts to convert flat file to delimiter file & Anonymize data as per the requirment

Docker File to create the docker image with python and pyspark setup to run the scripts with the Linux version 'alpine:latest' (Light weight Docker image of linux OS).
Execute to get into the docker: docker run -it praveenko/pyspark_data_quest:latest


Problem 1: Parse fixed width file
Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.

Solution:
The script 'create_flat_file.py' which creates the random generated alphanumberic value with fixed length file.
execute: python create_flat_file.py "../io/flat_file.txt" 100 "5,12,3,2,13,7,10,13,20,13"
The script 'parse_write.py' which parses the flat file as input and convert into the dat file with comma seperator delimiter(",") along with header.
execute: python parse_write.py "../io/flat_file.txt" "../io/delimited_file.dat" "5,12,3,2,13,7,10,13,20,13"

Problem 2: Data processing
Generate a csv file containing first_name, last_name, address, date_of_birth
Process the csv file to anonymise the data
Columns to anonymise are first_name, last_name and address

Solution:
The script 'create_csv.py' which generates csv file with the first_name,last_name,address and date_of_birth of random names from the list defined int the script with clean text/
execute: python create_csv.py "../io/csv_file.csv" 100
The script 'tokensier.py' which Anonymizes the first_name, last_name and address
execute: python tokeniser.py "../io/csv_file.csv" "../io/tokenised_data"

Testing:
For all the module, testing scenario has been addressed with pytest python package and placed in the test folder. Exceute 'pytest' from the test folder and it picks up all the scripts name starts with test name . Test module tests all the function which used in scripts.

cmd: pytest -v

Test Summary:
=========================================================================================================================== test session starts ===========================================================================================================================
platform win32 -- Python 3.7.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- c:\users\bravo\pycharmprojects\dataquest\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\bravo\PycharmProjects\DataQuest\venv\test
collected 10 items                                                                                                                                                                                                                                                         

test_create_csv.py::test_random_first_last_name_dob PASSED                                                                                                                                                                                                           [ 10%]
test_create_csv.py::test_create_csv_file PASSED                                                                                                                                                                                                                      [ 20%]
test_create_flat_file.py::test_get_random_alphanumeric_character PASSED                                                                                                                                                                                              [ 30%]
test_create_flat_file.py::test_create_flat_file PASSED                                                                                                                                                                                                               [ 40%]
test_parse_write.py::test_parse_file PASSED                                                                                                                                                                                                                          [ 50%]
test_parse_write.py::test_write_file PASSED                                                                                                                                                                                                                          [ 60%]
test_tokeniser.py::test_spark_init PASSED                                                                                                                                                                                                                            [ 70%]
test_tokeniser.py::test_tokeniser PASSED                                                                                                                                                                                                                             [ 80%]
test_tokeniser.py::test_load_file PASSED                                                                                                                                                                                                                             [ 90%]
test_tokeniser.py::test_write_file PASSED                                                                                                                                                                                                                            [100%]

============================================================================================================================ warnings summary =============================================================================================================================
test_tokeniser.py::test_spark_init
  c:\users\bravo\pycharmprojects\dataquest\venv\lib\site-packages\pyspark\sql\context.py:77: DeprecationWarning: Deprecated in 3.0.0. Use SparkSession.builder.getOrCreate() instead.
    DeprecationWarning)

-- Docs: https://docs.pytest.org/en/stable/warnings.html
====================================================================================================================== 10 passed, 1 warning in 8.70s ======================================================================================================================

