import csv

answer_path = 'sample_data/answer.csv'
fieldnames = ['id', 'submisson_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def read_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        content = []
        for row in reader:
            content.append(row)
    return content


def write_data(file_path, new_row):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_row)

