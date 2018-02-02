import sqlite3 as lite


class Models:

    def __init__(self):
        self.con = lite.connect('notes.db')
        self.cur = self.con.cursor()

    def create(self):
        with self.con:
            self.cur.execute('CREATE TABLE Notes(NoteID INT, '
                             'NoteSubject TEXT, NoteName TEXT, NoteContent TEXT)')
            self.cur.close()
        pass

    def extract(self):
        pass

    def insert(self, subject, name, content):
        with self.con:
            self.cur.execute('INSERT INTO Notes(NoteSubject, NoteName, NoteContent) VALUES(?, ?, ?)',
                             (subject, name, content))
            self.cur.close()
        pass

    def edit(self, subject, name, content):

        pass

    def delete(subject, name):
        pass

    def view(subject, name):
        pass
