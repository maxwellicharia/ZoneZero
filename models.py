import sqlite3 as lite


class Models:

    def __init__(self):
        self.con = lite.connect('notes.db')
        self.cur = self.con.cursor()
        self.con.text_factory = bytes

    def create(self):
        with self.con:
            try:
                self.cur.execute("CREATE TABLE IF NOT EXISTS Notes(NoteID INTEGER PRIMARY KEY AUTOINCREMENT, "
                                 "NoteName TEXT, NoteSubject TEXT, NoteContent TEXT)")
                self.con.commit()
            except lite.Error, e:
                self.con.rollback()
                return e

    def insert(self, name, subject, content):
        with self.con:
            try:
                self.cur.execute("INSERT INTO Notes(NoteName, NoteSubject, NoteContent) VALUES(?, ?, ?)",
                                 (name, subject, content))
                self.con.commit()
            except lite.Error, e:
                self.con.rollback()
                return e

    def view(self):
        with self.con:
            try:
                self.cur.execute("SELECT * FROM Notes")
                rows = self.cur.fetchall()
                return rows
            except lite.Error, e:
                return e

    def update(self, num, name, subject, content):
        with self.con:
            try:
                self.cur.execute("UPDATE Notes SET NoteName = ?, NoteSubject = ?, NoteContent = ? "
                                 "WHERE NoteID = ?", (name, subject, content, num))
                self.con.commit()
            except lite.Error, e:
                self.con.rollback()
                return e

    def delete(self, num):
        with self.con:
            try:
                self.cur.execute("DELETE FROM Notes WHERE NoteID = ?", num)
                self.con.commit()
            except lite.Error, e:
                self.con.rollback()
                return e
