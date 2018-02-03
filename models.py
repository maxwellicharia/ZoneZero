import sqlite3 as lite


class Models:

    def __init__(self):
        self.con = lite.connect('notes.db')
        self.cur = self.con.cursor()

    def create(self):
        with self.con:
            try:
                self.cur.execute("CREATE TABLE IF NOT EXISTS Notes(NoteID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                 "NoteSubject TEXT, NoteName TEXT, NoteContent TEXT)")
                self.con.commit()
            except lite.Error, e:
                print "An Error Occurred: %s" % e
                self.con.rollback()

    def insert(self, subject, name, content):
        with self.con:
            try:
                self.cur.execute("INSERT INTO Notes(NoteSubject, NoteName, NoteContent) VALUES(?, ?, ?)",
                                 (subject, name, content))
                self.con.commit()
            except lite.Error, e:
                self.con.rollback()
                print "An Error Occurred: %s" % e

    def edit(self, id):
        with self.con:
            pass

    def delete(self, id):
        with self.con:
            pass

    def view(self):
        with self.con:
            try:
                self.cur.execute("SELECT * FROM Notes")
                rows = self.cur.fetchall()
                print rows
                return rows
            except lite.Error, e:
                return "Error: " % e
