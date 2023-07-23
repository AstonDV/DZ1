import json
import datetime


def add_note():
    title = input("Enter the note title: ")
    body = input("Enter the note body: ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes = read_notes()

    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": current_time,
        "updated_at": current_time
    }
    notes.append(note)
    save_notes(notes)
    print("Note added successfully!")


def read_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []  # Если файл не найден, инициализируем пустым списком
    return notes


def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f, indent=4)


def edit_note():
    note_id = int(input("Enter the id of the note to edit: "))
    index = find_note_index(note_id)

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
    note_id = int(input("Enter the id of the note to delete: "))
    index = find_note_index(note_id)

    if index != -1:
        del notes[index]
        save_notes(notes)
        print("Note deleted successfully!")
    else:
        print("Note not found.")


def filter_notes_by_date():
    date = input("Enter the date (YYYY-MM-DD) to filter notes: ")
    filtered_notes = [note for note in notes if note["created_at"].startswith(date) or note["updated_at"].startswith(date)]

    if filtered_notes:
        print("Filtered Notes:")
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Created At: {note['created_at']}")
            print(f"Updated At: {note['updated_at']}")
            print("--------------------")
    else:
        print("No notes found for the specified date.")


def view_all_notes():
    sorted_notes = sorted(notes, key=lambda note: note["created_at"])

    if sorted_notes:
        print("All Notes:")
        for note in sorted_notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Created At: {note['created_at']}")
            print(f"Updated At: {note['updated_at']}")
            print("--------------------")
    else:
        print("No notes found.")


def find_note_index(note_id):
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            return i
    return -1


commands = {
    "add": add_note,
    "edit": edit_note,
    "delete": delete_note,
    "filter": filter_notes_by_date,
    "view": view_all_notes
}

notes = read_notes()

while True:
    command = input("Enter a command (add, edit, delete, filter, view): ")

    if command == "exit":
        break

    if command in commands:
        commands[command]()
    else:
        print("Invalid command.")
