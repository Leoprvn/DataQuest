from pyspark.sql import SparkSession
from pyspark.sql.functions import base64,unbase64
import sys


def arg_validate():
    """
    Validated the argument
    :return: if the validation fails, comes out of the script
    """
    if len(sys.argv) < 2:
        print("Please pass valid arguments")
        print("Execution: tokeniser.py  <csv_file_input> <output_folder_name>")
        print("Example: tokeniser.py '/opt/io_folder/input.csv' '/opt/io_folder/tokenised'")
        sys.exit(1)


def spark_init(appname_val):
    """
    This function intializes a new spark session
    :param: appname_val: name of the application
    :return: returns the spark session
    """
    try:
        spark = SparkSession.builder.appName('appname_val').getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")
        return spark
    except:
        print("Initialisation of spark session failed")


def tokenize(column):
    """
    Thie function is to tokenize base64
    :param column: pass column to be tokensize
    :return: tokenized column
    """
    try:
        return base64(column)
    except:
        print("Tokenisation function failed")


def detokenize(column):
    """
    This function to detokenise using unbase64
    :param column: pass column to detokenize
    :return:
    """
    try:
        return(unbase64(column).cast("string"))
    except:
        print("Detokenisation function failed")


def load_file(file_name,spark):
    """
    This function to Load the csv to convert into DataFrame
    :param file_name: File to read
    :return: dataframe
    """
    try:
        input_csv=spark.read.csv(file_name,header=True)
        return input_csv
    except:
        print("Reading a file failed")


def write_file(dataframe,folder_name):
    """
    This function is to write csv file from dataframe
    :param dataframe: pass dataframe
    :param file_name: provide the absolute path
    :return: return nothing
    """
    try:
        dataframe.write.format('parquet').mode('overwrite').save(folder_name)
    except:
        print('writing a dataframe into file is failed')


def main():
    """
     Main function to call to load file, tokenise data and write file
    :return:
    """
    arg_validate()
    appname_val = sys.argv[0]
    file_name = sys.argv[1]
    folder_name = sys.argv[2]
    try:
        spark = spark_init(appname_val)
        print('Initialisation of spark session passed')
        input_df = load_file(file_name,spark)
        print('Read a csv file is passed')
        transform_data = (input_df.select(tokenize(input_df.first_name).alias('first_name'),\
                                          tokenize(input_df.last_name).alias('last_name'),\
                                          tokenize(input_df.address).alias('address'),\
                                          input_df.date_of_birth))
        print('Transformation is  passed')
        write_file(transform_data,folder_name)
        print('Writing a dataframe into a file is passed')
        """
        #To detokenise the tokenised value to check - uncomment this block to test the tokenisation and 
        #detokenisation
        df = spark.read.parquet(folder_name)
        df.show(10)
        print('reading the untokenised value from patquet')
        df.select(detokenize(df.first_name).alias('first_name'),detokenize(df.last_name).alias('last_name'),\
        detokenize(df.address).alias('address'),df.date_of_birth.alias('date_of_birth')).show()
        print("Testing successfull")
        """
    except Exception:
        print('Main function is failed')


if __name__ == "__main__":
    main()

