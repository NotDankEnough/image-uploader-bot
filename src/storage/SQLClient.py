# Copyright (c) 2022 NotDankEnough (ilotterytea)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import sqlite3
from datetime import date

from src.storage.User import UserData

class SQLInstance:
    def __init__(self, file_name: str) -> None:
        self._connection = sqlite3.connect(file_name)
        self._db = self._connection.cursor()

        self._db.execute("""
                CREATE TABLE if not exists Users (Id INTEGER PRIMARY KEY AUTOINCREMENT, AliasId INTEGER NOT NULL, Platform INTEGER NOT NULL, CustomHost VARCHAR(500), Timestamp DATE);        
        """)
        self._connection.commit()

    def getUser(self, id: int, platform: int) -> UserData | None:
        self._db.execute("""
        SELECT * FROM Users WHERE (AliasId={id} and Platform={platform});
        """.format(id=id, platform=platform))
        
        fetched = self._db.fetchone()
        
        if fetched != None:
            return UserData(fetched[0], fetched[1], fetched[2], fetched[3])
        
        return None

    def createUser(self, id: int, platform: int, host: str) -> None:
        self._db.execute("""
        INSERT INTO Users (AliasId, Platform, CustomHost, Timestamp) VALUES ({id}, {platform}, '{host}', {date});
        """.format(id=id, host=host, platform=platform, date=date.today()))
        self._connection.commit()

    def updateUserHost(self, id: int, platform: int, host: str) -> None:
        self._db.execute("""
        UPDATE Users SET CustomHost = '{host}' WHERE (AliasId = {id} AND Platform = {platform})
        """.format(host=host, id=id, platform=platform))
        self._connection.commit()

    def saveAndClose(self) -> None:
        self._connection.close()


db = SQLInstance("database.db")
