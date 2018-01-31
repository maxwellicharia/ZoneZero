import os
import urlparse
import psycopg2

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


def create(self):

    self.con.execute('CREATE TABLE Notes IF NOT EXISTS(NoteID INT AUTOINCREMENT, '
                     'NoteDate DATE, NoteName TEXT, NoteContent TEXT)')
    self.con.close()


def extract(self):
    pass


def insert(self, date, name, content):
    self.con.execute('INSERT INTO Notes(NoteDate, NoteName, NoteContent) VALUES(?, ?, ?)', (date, name, content))
    self.con.close()


def edit(self, date, name, content):
    pass


def delete(date, name):
    pass


def view(date, name):
    pass
