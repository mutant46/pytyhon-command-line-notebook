from typing import List
from note import Note
import json
# global varibales


def global_read_data():
    with open('./noteFiles/notes.txt') as notes:
        data = json.load(notes)
        return data


notes = global_read_data() if global_read_data() else []


class Notebook:
    def __init__(self):
        ''' Represent the notebook that contains all the
            notes '''
        self.notes = notes

    def new_note(self, memo, completionDate=''):
        ''' Create a new note with Note object and add
            it in the file '''
        note = Note(memo, completionDate)
        self.notes = self.Create_file(note)

    def find_note(self, note_id):
        ''' Locate the note with the given id '''
        for note in self.notes:
            if note['id'] == int(note_id):
                return note
        return False

    def modify_note(self, note_id, memo, completionDate=''):
        ''' Find the note with given id and change it's
            data to the given data and update the file '''
        modified_note = self.find_note(note_id)
        if modified_note:
            modified_note['memo'] = memo
            modified_note['completion-date'] = completionDate
            for note in self.notes:
                if note['id'] == int(note_id):
                    note = modified_note
                    with open('./noteFiles/notes.txt', 'w') as notes:
                        json.dump(self.notes, notes, indent=4)
                    return True
        else:
            return False

    def search(self, note_id):
        ''' Search the notes that matches the id '''
        if self.find_note(note_id):
            return True
        else:
            return False

    def Create_file(self, note):
        ''' Creating a file and storing the new note data
             all in it '''
        with open('./noteFiles/notes.txt', 'w') as notebook:
            global notes
            noteContent = {
                'id': note.id,
                'memo': note.memo,
                'date': note.date,
                'completion-date': note.completionDate
            }
            notes.append(noteContent)
            json.dump(notes, notebook, indent=4)

        return self.read_data_from_file()

    def read_data_from_file(self):
        ''' Reading all the notes form the file
            and return empty list if data does not
            exits  '''
        with open('./noteFiles/notes.txt') as notes:
            if notes:
                data = json.load(notes)
                return data
        return []

    def remove_data_from_file(self):
        ''' delete all the notes from the notebook and
            files '''
        self.modify_data_in_file([])

    def remove_note_from_notebook(self, note_id):
        ''' Removing note of given id and refresing the 
            notebook notes attibutes '''
        for note in self.notes:
            if note['id'] == int(note_id):
                print(note['id'])
                new_notes = [
                    notes for notes in self.notes if notes['id'] != int(note_id)]
                self.modify_data_in_file(new_notes)
                return True
        return False

    def modify_data_in_file(self, new_notes_array):
        ''' Implements the data to the file and reset the
            notes with the new data  '''
        with open('./noteFiles/notes.txt', 'w') as notes:
            json.dump(new_notes_array, notes, indent=4)
        self.notes = self.read_data_from_file()
