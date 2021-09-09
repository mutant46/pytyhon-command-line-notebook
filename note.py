from datetime import date
import json


# get last_id from
# file if {notes}
# exists
def global_last_id():
    with open('./last_id.txt') as id:
        last_id = id.read()
        if last_id:
            return int(last_id)
    return False


# variable to store the previos id
last_id = global_last_id() if global_last_id() else 0


class Note:
    def __init__(self, memo, completionDate=''):
        ''' Represent the note in the notebook creates note 
            and store it in the file as an json object. '''
        global last_id
        last_id += 1
        created_date = date.today()
        self.id = last_id
        self.memo = memo
        self.date = created_date.strftime("%d %B, %Y")
        self.completionDate = completionDate if completionDate else 'Not set'
        self.write_last_id(str(last_id))

    def __str__(self):
        ''' Output it's content '''
        return "Id = {}, Msg = {} , Completion-date = {}".format(
            self.id, self.memo, self.completionDate)

    def write_last_id(self, last_id):
        with open('./last_id.txt', 'w') as id:
            id.write(last_id)

    def reset_id():
        global last_id
        last_id = 0
