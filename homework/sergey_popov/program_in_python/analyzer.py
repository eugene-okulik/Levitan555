import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path', help="enter file path")
parser.add_argument("--text", help="enter text")
args = parser.parse_args()
files_list = os.listdir(args.path)


def read_dir():
    for file in files_list:
        files = os.path.join(args.path, file)
        with open(files, 'r') as file_logs:
            file_read = file_logs.readlines()
            for line in file_read:
                if args.text in line:
                    print(f'{args.text} in file name: {file} in line number: {line.index(args.text)} find!')
                    words = line.split()
                    if args.text in words:
                        idx = words.index(args.text)
                        words_before = words[max(0, idx - 5):idx]
                        words_after = words[idx + 1:idx + 6]
                        print(' '.join(words_before + [words[idx]] + words_after))

    return file_read


read_dir()
