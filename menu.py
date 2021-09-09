from notebook import Notebook
import sys
import json


class Menu:
    def __init__(self):
        ''' Display a Menu and run'''
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_note,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.show_note,
            '6': self.clear_nootbook,
            '7': self.delete_note,
            '8': self.quit
        }

    def display(self):
        print('''
        1- Show all Notes
        2- Search Note
        3- Add Note
        4- Modify Note
        5- Show Note
        6- Delete All
        7- Delete single note
        8- Quit
        ''')

    def run(self):
        ''' Display the menu and respond to the choices '''
        while True:
            self.display()
            choice = input('Enter an option : ')
            print('\n')
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print("given is not an option \n")

    def show_note(self):
        ''' Read a note from the file as dict and print
            on the console '''
        notes = self.notebook.notes
        if notes:
            note_id = input('Enter the note Id : ')
            print('\n')
            for note in notes:
                if note['id'] == int(note_id):
                    not_found = False
                    print('   {}-  memo = {}, data = {}, completion-date = {}'
                          .format(note['id'], note['memo'], note['date'], note['completion-date']))
                    break
                else:
                    not_found = True
            if not_found:
                print('Note with this Id does not exit')
        else:
            print('NoteBook is empty, Create new notes \n')

    def show_notes(self):
        ''' Read all the notes from the file '''
        notes = self.notebook.notes
        if notes:
            for note in notes:
                note_id = note['id']
                memo = note['memo']
                date = note['date']
                cDate = note['completion-date']
                print(
                    f'   {note_id}-  memo = {memo}, date = {date}, completion-date = {cDate}')
        else:
            print('NoteBook is empty, Create new notes \n')

    def search_note(self):
        note_id = input('Enter note id to search : ')
        print('\n')
        exsits = self.notebook.search(note_id)
        if exsits:
            status = 'Note with this Id exists'
        else:
            status = 'Note with such Id does not exists'
        print(status)

    def add_note(self):
        memo = input('Enter the memo : ')
        cDate = input('Enter the Completion date : ')
        print('\n')
        self.notebook.new_note(memo, cDate)
        print('Your note has been added !!!! \n')
        self.show_notes()

    def modify_note(self):
        note_id = input('Enter the note id : ')
        memo = input('Enter the memo : ')
        cDate = input('Enter compeletion-date : ')
        print('\n')
        modified_status = self.notebook.modify_note(note_id, memo, cDate)
        if modified_status:
            status = 'Note has been modified'
        else:
            status = 'Note does not exit'
        print(status)

    def clear_nootbook(self):
        self.notebook.remove_data_from_file()
        print('Every thing is removed from the notebook')

    def delete_note(self):
        note_id = input('Enter the note id to delte : ')
        print('\n')
        status = self.notebook.remove_note_from_notebook(note_id)
        if status:
            print('The note has been deleted')
        else:
            print('Note with such id does not exit already')

    def quit(self):
        print("Thanks for using Mr. MuTanT Notebook :)\n")
        sys.exit(0)


m = Menu()
m.run()
