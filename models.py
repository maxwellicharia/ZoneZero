class Models:

    def __init__(self):
        pass

    # with app.app.context()
    #     mysql = MySQL()


    def create(self):
        # self.cur.execute('CREATE TABLE Notes IF NOT EXISTS(NoteID INT AUTOINCREMENT, '
        #                  'NoteSubject TEXT, NoteName TEXT, NoteContent TEXT)')
        # self.cur.close()
        pass

    def extract(self):
        pass

    def insert(self, date, name, content):
        # self.cur.execute('INSERT INTO Notes(NoteDate, NoteName, NoteContent) VALUES(?, ?, ?)', (date, name, content))
        # self.cur.close()
        pass

    def edit(self, date, name, content):

        pass

    def delete(date, name):
        pass

    def view(date, name):
        pass
