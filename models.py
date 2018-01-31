import os
import urlparse
import psycopg2


class Models:

    def __init__(self):
        pass

    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    cur = conn.cursor()

    def create(self):

        self.cur.execute('CREATE TABLE Notes IF NOT EXISTS(NoteID INT AUTOINCREMENT, '
                         'NoteSubject TEXT, NoteName TEXT, NoteContent TEXT)')
        self.cur.close()

    def extract(self):
        pass

    def insert(self, date, name, content):
        self.cur.execute('INSERT INTO Notes(NoteDate, NoteName, NoteContent) VALUES(?, ?, ?)', (date, name, content))
        self.cur.close()

    def edit(self, date, name, content):

        pass

    def delete(date, name):
        pass

    def view(date, name):
        pass
