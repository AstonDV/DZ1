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
    note_id = int(input("Enter the id of the note to edit: "))
    index = find_note_index()

    if index != -1:
        title = input("Enter the new title: ")
        body = input("Enter the new body: ")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        notes[index]["title"] = title
        notes[index]["body"] = body
        notes[index]["updated_at"] = current_time
        save_notes(notes)
        print("Note edited successfully!")
    else:
        print("Note not found.")


def delete_note():
    pass


def filter_notes_by_date():
    pass


def find_note_index():
    pass





notes = read_notes()