import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    command = """
                    CREATE TABLE video_details (
                        id SERIAL PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        thumbnail_url TEXT NOT NULL,
                        publishtime TIMESTAMP NOT NULL
                    )
            """
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()