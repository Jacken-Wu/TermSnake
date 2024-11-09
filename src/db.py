import sqlite3


class DB:
    def __init__(self):
        pass

    @staticmethod
    def init_table():
        conn = sqlite3.connect("snake_data.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value INTEGER, time TEXT)")
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def insert_data(value: int, time: str):
        conn = sqlite3.connect("snake_data.db")
        c = conn.cursor()
        c.execute(f"INSERT INTO data (value, time) VALUES ({value}, '{time}')")
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def get_first3():
        conn = sqlite3.connect("snake_data.db")
        c = conn.cursor()
        c.execute("SELECT value, time FROM data ORDER BY value DESC LIMIT 3")
        data = c.fetchall()
        c.close()
        conn.close()
        return data


def __clear_data():
    conn = sqlite3.connect("snake_data.db")
    c = conn.cursor()
    c.execute("DELETE FROM data")
    conn.commit()
    c.close()
    conn.close()


if __name__ == '__main__':
    DB.init_table()
    __clear_data()
    # DB.insert_data(10, '2021-01-01 12:00:00')
    # DB.insert_data(20, '2021-01-01 12:00:01')
    data = DB.get_first3()
    print(data)
