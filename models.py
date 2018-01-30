import os
import urlparse
import psycopg2


urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])
con = psycopg2.connect(database=url.path[1:], user=url.username,
                       password=url.password, host=url.hostname, port=url.port)

