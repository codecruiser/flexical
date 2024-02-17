import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery


class FlexiDBManager(object):

    def __new__(cls, *args, **kwargs):
        """
        Singelton
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            return cls.instance

    def __del__(self):
        if self.db.isOpen():
            self.db.close()

    def connect(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setHostName(os.getenv("FLEXICAL_HOST") or "127.0.0.1")
        self.db.setDatabaseName(os.getenv("FLEXICAL_DBNAME") or "flexical.sqlite")
        self.db.setUserName(os.getenv("FLEXICAL_USERNAME") or "flexical")
        self.db.setPassword(os.getenv("FLEXICAL_USERNAME") or "flexical")
        if self.db.open():
            print("Connected")
        else:
            print("Cannot open database")

    def create_tables(self):
        query = QSqlQuery(self.db)
        res = query.exec("""CREATE TABLE IF NOT EXISTS flexical.categories (
            name varchar(255) NOT NULL,
            description text NULL,
            parent_id INTEGER NULL,
            FOREIGN KEY (parent_id)
                REFERENCES flexical.categories (rowid) 
        )""")
        print(res)
        query.exec("""CREATE TABLE IF NOT EXISTS flexical.series (
            name varchar(255) NOT NULL,
            description text NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id)
                REFERENCES flexical.categories (rowid) 
        )""")
        query.exec("""CREATE TABLE IF NOT EXISTS flexical.todo_type (
            name varchar(255) NOT NULL,
            description text NULL
        )""")
        query.exec("""CREATE TABLE IF NOT EXISTS flexical.todo (
            name varchar(510) NOT NULL,
            description text NULL,
            do_at datetime NULL,
            position integer NOT NULL,
            done boolean NOT NULL DEFAULT false,
            type_id integer NOT NULL,
            FOREIGN KEY (type_id)
                REFERENCES flexical.todo_type (rowid),
        )""")
        query.exec("""CREATE TABLE IF NOT EXISTS flexical.categories_todo (
            todo_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (todo_id)
                REFERENCES flexical.todo (rowid),
            FOREIGN KEY (category_id)
                REFERENCES flexical.categories (rowid)
        )""")
        query.exec("""CREATE TABLE IF NOT EXISTS flexical.series_todo (
            todo_id INTEGER NOT NULL,
            serie_id INTEGER NOT NULL,
            FOREIGN KEY (todo_id)
                REFERENCES flexical.todo (rowid),
            FOREIGN KEY (serie_id)
                REFERENCES flexical.series (rowid)
        )""")


fdbm = FlexiDBManager()
fdbm.connect()
fdbm.create_tables()
