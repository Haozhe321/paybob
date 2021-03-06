import sqlite3
from sqlite3 import Error
import Logger

logger = Logger.Logger()

def initialise(self, databaseFile = "payBob.sqlite"):
    try:
        self.databaseFile = databaseFile
        self.conn = sqlite3.connect(databaseFile, check_same_thread = False)
    except Error as e:
        logger.warning(e)
        logger.notify_admins(e)


def create_table(conn, create_table_statement):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_statement)
    except Error as e:
        logger.warning(e)
        logger.notify_admins(e)
