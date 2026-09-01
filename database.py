# Este ficheiro é responsável pela ligação entre a aplicação Python e a base
# de dados MySQL. A classe Database centraliza a configuração da ligação e a
# execução das instruções SQL solicitadas pelos Repositories. As Views e os
# Services não devem comunicar diretamente com o MySQL, devendo o acesso aos
# dados ser realizado através da camada Repository.
import os
import mysql.connector


class Database:
    def __init__(self):
        self.config = {
            "host": os.getenv("CITYDRIVE_DB_HOST", "localhost"),
            "port": int(os.getenv("CITYDRIVE_DB_PORT", "3306")),
            "user": os.getenv("CITYDRIVE_DB_USER", "root"),
            "password": os.getenv("CITYDRIVE_DB_PASSWORD", ""),
            "database": os.getenv("CITYDRIVE_DB_NAME", "citydrive"),
        }

    def connect(self):
        return mysql.connector.connect(**self.config)

    def execute(self, sql, params=None, fetch=False):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(sql, params or ())
            if fetch:
                return cursor.fetchall()
            connection.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            connection.close()
