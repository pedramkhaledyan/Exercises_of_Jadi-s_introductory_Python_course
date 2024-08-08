import csv
# For the average
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    stu_avg = OrderedDict()
    with open(input_file_name) as csv_file:
        # input_file_name is the name and address of the CSV file from which we want to read data.
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            grades = []
            for i in range(1, len(row)):
                grades.append (float(row[i]))
            average = mean(grades)
            stu_avg [row[0]] = average
            
    with open (output_file_name, 'w') as out:
        # output_file_name is the name and address of the CSV file from which we want to write data.
        count = 0
        for person in stu_avg:
            count += 1
            if count == 1:
                out.write(person+ ","+ str(stu_avg[person]))
            else:
                out.write("\n"+ person+ ","+ str(stu_avg[person]))
            
        


def calculate_sorted_averages(input_file_name, output_file_name):
    stu_avg = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            grades = []
            for i in range(1, len(row)):
                grades.append (float(row[i]))
            average = mean(grades)
            stu_avg [row[0]] = average
    # use lambda for sort dictionary by value or key
    averages_ordered = OrderedDict (sorted (stu_avg.items(), key=lambda x:(x[1], x[0])))

    with open (output_file_name, 'w') as out:
        count = 0
        for person in averages_ordered:
            count += 1
            if count == 1:
                out.write(person+ ","+ str(averages_ordered[person]))
            else:
                out.write("\n"+ person+ ","+ str(averages_ordered[person]))
    
        


def calculate_three_best(input_file_name, output_file_name):
    stu_avg = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            grades = []
            for i in range(1, len(row)):
                grades.append (float(row[i]))
            average = mean(grades)
            stu_avg [row[0]] = average

    averages_ordered = OrderedDict (sorted (stu_avg.items(), key=lambda x:(-x[1], x[0])))

    with open (output_file_name, 'w') as out:
        best = []
        for i in range (3):
            best_avg = averages_ordered.popitem (last=False)
            best.append (best_avg)

        out.write (best[0][0]+","+str(best[0][1])+"\n")
        out.write (best[1][0]+","+str(best[1][1])+"\n")
        out.write (best[2][0]+","+str(best[2][1]))


def calculate_three_worst(input_file_name, output_file_name):
    stu_avg = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            grades = []
            for i in range(1, len(row)):
                grades.append (float(row[i]))
            average = mean(grades)
            stu_avg [row[0]] = average

    averages_ordered = OrderedDict (sorted (stu_avg.items(), key=lambda x:(x[1], x[0])))
    
    with open (output_file_name, 'w') as out:
        worst = []
        for i in range (3):
            worst_avg = averages_ordered.popitem (last=False)
            worst.append (worst_avg)
            
        out.write (str(worst[0][1])+"\n")
        out.write (str(worst[1][1])+"\n")
        out.write (str(worst[2][1]))


def calculate_average_of_averages(input_file_name, output_file_name):
    stu_avg = {}
    with open(input_file_name) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            grades = []
            for i in range(1, len(row)):
                grades.append (float(row[i]))
            average = mean(grades)
            stu_avg [row[0]] = average

    averages_ordered = OrderedDict (sorted (stu_avg.items(), key=lambda x:(x[1], x[0])))

    SUM = 0
    count = 0
    for average in averages_ordered:
        count += 1
        SUM += float(averages_ordered[average])

    avg_avg = SUM/count
    with open (output_file_name, 'w') as out:
        out.write(str(avg_avg))
        

calculate_averages('input_file_name', 'output_file_name')
calculate_sorted_averages('input_file_name', 'output_file_name')
calculate_three_best('input_file_name', 'output_file_name')
calculate_three_worst('input_file_name', 'output_file_name')
calculate_average_of_averages('input_file_name', 'output_file_name')

# example for input_file_name and output_file_name at bottom lines
# calculate_averages('E:/Programming/grades.csv', 'E:/Programming/task1.csv')

# calculate_sorted_averages ('E:/Programming/grades.csv','E:/Programming/task2.csv')

# calculate_three_best ('E:/Programming/grades.csv','E:/Programming/task3.csv')

# calculate_three_worst ('E:/Programming/grades.csv','E:/Programming/task4.csv')

# calculate_average_of_averages ('E:/Programming/grades.csv','E:/Programming/task5.csv')