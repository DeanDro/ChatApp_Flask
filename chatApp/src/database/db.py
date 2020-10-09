from mysql.connector import connector


class UsersDatabase():
    """The class to handle interaction with the list of users"""

    def __init__(self, configurations):
        self.config = configurations

    def __enter__(self):
        self.conn = connector.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
