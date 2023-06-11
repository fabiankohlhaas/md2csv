# Markdown list to CSV Converter

Small script to convert an unordered markdown list copyed to the clipboard into a csv file. The seperator will be a pipe (|).
The first column will be the question and the second column will be the answer.
The output file will be overwritten every time the script is run.

---

## Use Case

While studing I write dwon questions and answers to the toppics I'm studying in obsidian. I use the script to convert the list to a csv file that I can import into anki.

---

## Setup

### Run the following command to install pyperclip:

If pip is in your path: 

```bash
pip install -r requirements.txt
``` 

If pip is not in your path:

```bash
python3 -m pip install -r requirements.txt
``` 

### Make the script executable:

```bash
chmod +x ["path to script"]/md2csv.py
```

### Add the script to your path:

To add the script to your path, run the following command:

```bash
sudo ln -s ["path to script"]/md2csv.py /usr/local/bin/md2csv
```

Change the following line to the desired full path of your desired output file or delete the path and outcomment the input line to be asked for the path every time you run the script:

```python
csv_filename = "output/import-to-anki.csv" #input("Please enter the path of the CSV file to be created: ")
```

Now you can run the script from anywhere with the command:

```bash
md2csv
```
---
## Usage

The list should be ordered like this:

```markdown
- Question 1
    - Answer 1
- Question 2
    - Answer 2
```
To use the script, copy the list to the clipboard and run the script from your terminal with the command:
    
```bash
md2csv
```

If you did not change the path for the output file, The output will be in a folder called "output" witht the filename "import-to-anki.csv" in the same directory as the script. Import that file into anki.