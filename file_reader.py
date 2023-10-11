import re

lines = list()


def process_file(file_name):
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            global lines
            lines = file.readlines()
    except FileNotFoundError:
        print("File Not Found")


process_file('My Clippings.txt')

title_notes_dict = {}
title = lines[0]
notes = lines[3]
lst = list()
title_notes_dict[title] = notes
separator_found = False

for i in range(len(lines)):
    if lines[i] == "==========\n":
        separator_found = True
    elif separator_found:
        title = lines[i]
        if i + 3 < len(lines):
            notes = lines[i + 3]
            if title not in title_notes_dict:
                lst = []
            lst.append(notes)
            title_notes_dict[title] = lst
        separator_found = False


def title_notes():
    print("Title-Notes Dictionary:", title_notes_dict)
    print()
    for title, notes in title_notes_dict.items():
        print(f"Title: {title}")
        if type(notes) == list:
            for i in notes:
                print("-", i)
        else:
            print(f"Notes: {notes}")
            print()


title_notes()


def create_or_append_notes_file(title, notes):
    punc = '\n'
    title = re.sub(r'[^\x20-\x7E]', '', title)
    file_name = f"{title}.txt"  # Append ".txt" extension to the title for the file name
    with open(file_name, 'a', encoding = 'utf-8') as file:
        if type(notes) == list:
            for note in notes:
                file.write(f"- {note}\n\n")
        else:
            file.write(f"- {notes}\n\n")
    print(f"Notes added to file: {file_name}")


# Example usage with title_notes_dict
for title, notes in title_notes_dict.items():
    create_or_append_notes_file(title, notes)


