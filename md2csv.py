#!/usr/bin/env python3
import csv
import re
import pyperclip

def markdown_to_csv(csv_filename):
    clipboard_data = pyperclip.paste().split('\n')

    questions_answers = []

    for i in range(0, len(clipboard_data), 2):
        question = re.sub('-\s', '', clipboard_data[i]).strip()
        # Check if i+1 is a valid index before trying to access it
        if i+1 < len(clipboard_data):
            answer = re.sub('-\s', '', clipboard_data[i+1]).strip()
        else:
            answer = 'No answer provided, check the source material'
        questions_answers.append([question, answer])

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(questions_answers)
        print("CSV file created successfully!")

if __name__ == "__main__":
    csv_filename = "/Users/fabian/SynologyDrive/programming/projects/md2csv/output/import-to-anki.csv" #input("Please enter the path of the CSV file to be created: ")
    markdown_to_csv(csv_filename)
