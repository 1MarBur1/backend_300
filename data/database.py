import sqlite3


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        print("The database is connected successfully")

    def add_user(self, ID, name):
        with self.connection:
            try:
                self.cursor.execute("INSERT INTO 'Users' VALUES (?, ?)", (ID, name))
            except:
                ...

    def get_user(self, ID):
        return self.cursor.execute("SELECT * FROM 'Users' WHERE id = ?", (ID,)).fetchmany()[0]

    def add_point(self, name, description, location, type, photo, reward):
        with self.connection:
            try:
                self.cursor.execute(
                    "INSERT INTO 'Points' (name, description, location, type, photo, reward) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, description, location, type, photo, reward))
            except:
                ...

    def delete_point(self, ID):
        with self.connection:
            try:
                self.cursor.execute("DELETE FROM 'Points' WHERE id=?", (ID,))
            except:
                print("Error deleting user with ID:", ID)

    def get_point(self, ID):
        return self.cursor.execute("SELECT * FROM 'Points' WHERE id = ?", (ID,)).fetchmany()[0]

    def get_points(self):
        return self.cursor.execute("SELECT * FROM 'Points'").fetchmany(1000) #.execute() #fetchmany()

    def update_point_status(self, ID, status):
        with self.connection:
            try:
                self.cursor.execute("UPDATE 'Points' SET status = ? WHERE id = ?", (status, ID))
            except:
                ...

    # def client_exist(self, ID):
    #     with self.connection:
    #         result = self.cursor.execute("SELECT * FROM 'client' WHERE user_id = ?", (ID,)).fetchmany(1)
    #         if not bool(len(result)):
    #             return False
    #         return result[0]
    #
    # def get_all_client(self):
    #     return self.cursor.execute("SELECT user_id FROM 'client'").fetchall()
    #
    # def get_all_client_without_ban(self):
    #     return self.cursor.execute("SELECT user_id FROM 'client' WHERE role = 'client'").fetchall()
    #
    # def get_verification_data(self, ID):
    #     with self.connection:
    #         return self.cursor.execute("SELECT * FROM 'all_users' WHERE user_id = ?", (ID,)).fetchmany()[0]
    #
    # def delete_verification_data(self, ID):
    #     with self.connection:
    #         return self.cursor.execute("DELETE FROM 'all_users' WHERE user_id = ?", (ID,))
    #
    # def ban_client(self, ID):
    #     with self.connection:
    #         self.connection.execute("UPDATE 'client' SET role = 'ban' WHERE user_id = ?", (ID,))
    #
    # def unban_client(self, ID):
    #     with self.connection:
    #         self.connection.execute("UPDATE 'client' SET role = 'client' WHERE user_id = ?", (ID,))
    #
    # def add_data_of_send_message(self, text, photo_id=None):
    #     with self.connection:
    #         self.connection.execute("INSERT INTO 'data' VALUES (?, ?)", (text, photo_id,))
    #
    # def update_data_of_send_message(self, text, photo_id):
    #     with self.connection:
    #         self.connection.execute("UPDATE 'data' SET text= ?, photo_id = ?", (text, photo_id,))
    #
    # def get_data_of_send_message(self):
    #     with self.connection:
    #         return self.connection.execute("SELECT * FROM 'data'").fetchmany()[0]
    #
    # def delete_data_of_send_message(self):
    #     with self.connection:
    #         self.connection.execute("DELETE FROM 'data'")
