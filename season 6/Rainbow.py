import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):

    with open(input_file_name) as csv_file:
        read_file = csv.reader(csv_file)
        password_dict = OrderedDict()
        password_list = list()
        # we should hash all number from 1000 to 10000 and save these hash numbers with real number in a dictionary
        for num in range(1000,10000):
                num = str(num)
                x = hashlib.sha256(num.encode())
                password_dict[x.hexdigest()] = num
        for row in read_file:
                name = row[0]
                # search hash password in our hash numbers dictionary for find password number
                if row[1] in password_dict.keys():
                    password_list.append([name,password_dict[row[1]]])

    with open(output_file_name, 'w' ,newline = '') as csv_file_write:
        write_file = csv.writer(csv_file_write)
        for item in password_list:
             write_file.writerow(item)


