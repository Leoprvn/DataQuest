import random
import string
import sys


def arg_validate():
    """
    Validate the anumber of argument
    :return: if validateion fails, comes out of the script
    """
    if len(sys.argv) < 3:
        print("Please pass valid arguments")
        print("Execute: python parse_write.py  <flat_file_input> <output_file> <offset>")
        print("Example: python parse_write.py 'flat_file.txt' 'delimited_file.dat' \
              5,12,3,2,13,7,10,13,20,13")
        sys.exit(1)


def parse_file(file_name, offset):
    """
    Parse the file and add the delimter for the columns based on the offset value
    Parameter: file_name,offset
    Example: parse_file("/tmp/input.txt",file_name,5, 12, 3, 2, 13, 7, 10, 13, 20, 13)
    Input: 'U72hWc08wssxR3zUznGYhZn6VdSl3x45EChc5FrqICTAaFUZsHQ1Op4rU9lHDG9E1XdeqeYwjLpuZxlvcpaRrRbIWheiZmXW1v
            GBrXguIwVQAGQgfqsEIhwgTI2ZUM4OiR0p7AKuskQLmEdRLwTTMmin0tJqVpDMcBPsODKvB61Kd5r1VpXwiZxylKLHw0Y8FQpE'
    Output:
     ['U72hW,c08wssxR3zUz,nGY,hZ,n6VdSl3x45ECh,c5FrqIC,TAaFUZsHQ1,Op4rU9lHDG9E1,XdeqeYwjLpuZxlvcpaRr,RbIWheiZmXW1v',
     'GBrXg,uIwVQAGQgfqs,EIh,wg,TI2ZUM4OiR0p7,AKuskQL,mEdRLwTTMm,in0tJqVpDMcBP,sODKvB61Kd5r1VpXwiZx,ylKLHw0Y8FQpE]
    """
    try:
        offsetu = []
        lines = []
        headerlist = []
        headerstr = ''
        offsetu.append(offset[0])
        for i in range(len(offset) - 1):
            offsetu.append(offsetu[i] + offset[i + 1])
        headerlist = ["f" + str(i + 1) + "," for i in range(len(offset) - 1)]
        headerlist.append("f" + str(len(offset)))
        for i in headerlist:
            headerstr += i
        lines.append(headerstr)
        '''
        offsetu.append(offset[0])
        for i in range(len(offset) - 1):
            offsetu.append(offsetu[i] + offset[i + 1])'''
        for line in open(file_name):
            string = line[:offsetu[0]]
            for i in range(len(offsetu) - 1):
                string += "," + (line[offsetu[i]:offsetu[i + 1]])
            lines.append(string)
            #print(lines)
        print("File {} has been parsed with the offset {}".format(file_name,offset))
        return lines
    except:
        print("Parsing the file {} has failed".format(file_name))
        sys.exit(1)


def write_file(file_name, lines):
    """
    Write into a file with the content of parsed file
    Parameters: file name , lines(as list)
    Example: write_file('/tmp/output_file.dat,lines)
    Return: Write into the a file
    """
    try:
        with open(file_name, "w") as f:
            for i in lines:
                f.write(i)
                f.write("\n")
            print("Writing into a file {} has been completed successfully".format(file_name))
    except:
        print("Writing into a file {} has failed".format(file_name))
        sys.exit(1)


def main():
    """
    Main function to call the parse and write function
    :return:
    """
    arg_validate()
    flat_file_input = str(sys.argv[1])
    delimited_output_file = str(sys.argv[2])
    offset = [int(i) for i in str(sys.argv[3]).split(',')]
    try:
        lines = parse_file(flat_file_input, offset)
        write_file(delimited_output_file, lines)
    except:
        print("main function failed")


if __name__ == "__main__":
    main()

