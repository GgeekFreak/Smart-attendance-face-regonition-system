from PyQt4 import QtSql
class DbManger:
    def __init__(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("smart_attendance_system")
        self.db.setUserName("root")
        self.db.setPassword("thedesertm")
        self.db_connection_statues = self.db.open()
        self.query = QtSql.QSqlQuery(self.db)
        self.__last_error = ""
        self.__init_seting__()

    def __init_seting__(self):
        self.query.exec_('''CREATE TABLE IF NOT EXISTS students_information(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL, student_id text NOT NULL )''')
        self.query.exec_('''CREATE TABLE IF NOT EXISTS students_attendance(
                        id integer AUTO_INCREMENT PRIMARY KEY,
                        student_id text,
                        attandance_data DATE NOT NULL,
                        FOREIGN KEY (student_id) REFERENCES students_information (student_id) 
                        )
                        ''')
        if not self.query.isActive():
            print (self.query.lastError().text())

    def inser_new_student(self , name , id):
        qur_str = '''INSERT INTO students_information (name , student_id) VALUES ('{}' , '{}')'''.format(name , id)
        if self.query.exec_(qur_str):
            QtSql.QSqlDatabase.database().commit()

    def is_exist(self , student_id):
        qur_str = '''select name from students_information where student_id = '{}' '''.format(student_id)
        self.query.exec_ (qur_str)
        qur_result = []
        if not self.query.isActive():
            print(str(self.query.lastError().text()))
        else:
            while self.query.next():
                qur_result.append(str(self.query.value(0).toString()))
        return qur_result
    def submit_attendance(self , id , date):
        qur_str = '''INSERT INTO students_attendance (attandance_data , student_id) VALUES ('{}' , '{}')'''.format(date, id)
        if self.query.exec_(qur_str):
            QtSql.QSqlDatabase.database().commit()

    def isAttended(self , id , date):
        qur_str = '''select student_id from students_attendance where student_id = '{}'  and attandance_data ='{}' '''.format(id , date)
        self.query.exec_(qur_str)
        qur_result = []
        if not self.query.isActive():
            print(str(self.query.lastError().text()))
        else:
            while self.query.next():
                qur_result.append(str(self.query.value(0).toString()))
        return qur_result





def Test():
    test = DbManger()
    test.is_exist("fooooo")
if __name__ == "__main__":
    Test()