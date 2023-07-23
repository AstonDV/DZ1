import json
import datetime


def add_note():
    title = input("Enter the note title: ")
    body = input("Enter the note body: ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": current_time,
        "updated_at": current_time
    }
    notes.append(note)
    save_notes(notes)
    print("Note added successfully!!!")


def read_notes():
    with open('notes.json', 'r') as f:
        notes = json.load(f)
    return notes


def save_notes():
    with open('notes.json', 'w') as f:
        json.dump(notes, f)


def edit_note():
    pass


def delete_note():
    pass


def filter_notes_by_date():
    pass


def find_note_index():
    pass





notes = read_notes()