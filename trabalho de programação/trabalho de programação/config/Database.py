import psycopg2

class Database:
    def __init__(self, config: dict) -> None:
        self.connect(config)

    def connect(self, config: dict):
        self.conn = None

        try:
            print('Conectando o PostgreSQL como banco de dados')
            self.conn = psycopg2.connect(**config)

            cur = self.conn.cursor()

            print('Versão do Banco de Dados')
            cur.execute('SELECT version()')

            database_version = cur.fetchone()
            print(database_version)

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)