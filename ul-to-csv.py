import csv
import re

def markdown_to_csv(markdown_filename, csv_filename):
    with open(markdown_filename, 'r') as md_file:
        lines = md_file.readlines()

    questions_answers = []

    for i in range(0, len(lines), 2):
        question = re.sub('-\s', '', lines[i]).strip()
        answer = re.sub('-\s', '', lines[i+1]).strip()
        questions_answers.append([question, answer])

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(questions_answers)
        print("CSV file created successfully!")

if __name__ == "__main__":
    markdown_filename = "input/input.md" #input("Please enter the path of the Markdown file: ")
    csv_filename = "output/import-to-anki.csv" #input("Please enter the path of the CSV file to be created: ")
    markdown_to_csv(markdown_filename, csv_filename)