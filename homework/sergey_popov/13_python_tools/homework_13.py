import datetime
import os

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))

ev_file_path = os.path.join(file_path, 'eugene_okulik', 'hw_13', 'data.txt')
new_file_path = os.path.join(file_path, 'sergey_popov', '13_python_tools', 'data2.txt')


def read_file():
    with open(ev_file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    data = data_line.split(' ', 1)[1].split(' - ')[0]
    data_time = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f')
    if data_line.startswith('1'):
        print(data_time + datetime.timedelta(days=7))
    elif data_line.startswith('2'):
        print(data_time.isoweekday())
    elif data_line.startswith('3'):
        print(datetime.datetime.now() - data_time)
