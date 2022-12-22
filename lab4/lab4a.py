"""
Thierno Diallo

Lab4a
"""
import csv 
import os

#1A 
def load_data(csv_file_name):
    """
    This function loads all of the data in a csv file as a list of dictionaries
    corresponding to each row in the file.

    Argument: str csv file name
    Return Value: a list of dictionaries
    """
    lst = []
    if os.path.exists(csv_file_name) == True:
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                lst.append(row)
        return lst
    else:
        print(f'{csv_file_name} not found. Aborting')
    


#2A 
def clear_data(csv_file_name):
    """
    This function clears all the data in a csv file except for the header row.

    Argument: str csv file name
    Return Value: None
    """
    if os.path.exists(csv_file_name) == True:
        with open(csv_file_name, 'r') as csv_file:
            first_row = csv_file.readline()
        with open(csv_file_name, 'w') as csv_file:
            csv_file.write(first_row)
        print(f'{csv_file_name} data was successfully cleared')
    else:
        print(f'{csv_file_name} not found. Aborting.')
    

#3A 
def add_rows(csv_file_name, dic_lst):
    """
    This function takes a csv file and a list of dictionaries and adds
    the list of dictionaries to at the end of the file.

    Arguments: a str csv file name and a list of dictionaries
    """
    keys = list(dic_lst[0].keys())
    with open(csv_file_name, 'a', newline = '') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = keys)
        writer.writerows(dic_lst)
 
        

#4A
def filter_rows(dic_lst, column_name, value):
    """
    This fucntion takes a list of dictionaries, a column name, and a value
    and returns a filtered list of all dictionaries in that column containing the value.

    Arguments:
        - a list of dictionaries
        - a str column name
        - a value
    Retrun Value: a filtered lst of all dictionaries in the column containing the value.
    """
    filtered_lst = []
    for dic in dic_lst:
        for key in dic:
            if key == column_name and dic[key] == value:
                filtered_lst.append(dic)
    return filtered_lst



#I chose to use the csv.Dictreader because I felt it was easier to filter the columns
#if we knew which key they were in.
#5A 
def filter_column(csv_file_name, column_name):
    """
    This function takes a csv file name and a column name and returns a list of all data
    for the given column in order of the rows in that file.

    Arguments:
        - a str csv file name 
        - a str column name
    Return Value: a list containing all the values in that column in the order they appear.
    """
    with open(csv_file_name, 'r') as csv_file:
        final_lst = []
        reader = csv.DictReader(csv_file)
        for dic in reader:
            for key in dic:
                if key == column_name:
                    final_lst.append(dic[key])
    return final_lst


#6A
def value_counts(dic):
    """
    This function takes a dictinary and returns a new dictionary holding 
    the number of times each value occurs in the orginal dictionary.

    Argument: a dictionary
    Return Value: a dictionary 
    """
    new_dic = {}
    dic_values = list(dic.values())
    for item in dic_values:
        if item not in new_dic:
            new_dic[item] = dic_values.count(item)
    return new_dic



#7A
def merge_dicts(dic_1, dic_2):
    """
    This funtion takes two dictionaries and adds all key/value 
    pairs from the second dictionary into the first

    Arguments: 2 seperate dictionaries
    Return Value: a modifie first dictionary
    """
    for key in dic_2:
        if key in dic_1:
            dic_1[key] += dic_2[key]
        else:
            dic_1[key] = dic_2[key]
