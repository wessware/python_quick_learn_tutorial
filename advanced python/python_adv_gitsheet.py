
import csv
import pickle
import json

# Traditional file operations

# Reading from a file


def read_info(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()

# Writing to a file


def write_info(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


# Comma Separated Values (csv) operations


# reading rows from a csv file
def read_csv_file(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        return list(csv.reader(file))

# write rows to a csv file


def write_to_csv_file(filename, rows):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


"""
CSV parameters
'dialect' - excel
'delimiter' - "
'quotechar'
'doublequote' - True, False
'skipinitialspace' - True, False
'lineterminator' - '\r\n, \n'
'quoting' - 0, 1
'escapechar' - None
"""
# Pickle File operations


# read object

def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# write object


def write_to_pickle_file(filename, p_object):
    with open(filename, 'wb') as file:
        pickle.dump(p_object, file)


# JSON file operations


# read object from json file

def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)

# write object to json file


def write_json_obj(filename, j_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(j_object, file, ensure_ascii=False, indent=2)
