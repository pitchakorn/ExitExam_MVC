import pymysql

class OnlineLearningModel(object):

    def connector(self):
        connect = pymysql.connect('localhost', 'root', '', 'mvcdb')
        return connect

    def fetchDataSubjectAndLecturer(self):
        connect = self.connector()
        with connect:
            cursor = connect.cursor()
            cursor.execute("""SELECT SID, subjects.SubjectName, lecturer.Firstname , lecturer.Lastname 
                        FROM subjects INNER JOIN lecturer ON subjects.TID = lecturer.TID """)
            rows = cursor.fetchall()
        return rows


    def fetchCountSubjects(self):
        connect = self.connector()
        with connect:
            cursor = connect.cursor()
            cursor.execute("""SELECT  lecturer.Firstname , lecturer.Lastname , count(*) as count
                        FROM subjects INNER JOIN lecturer ON subjects.TID = lecturer.TID
                        group by lecturer.TID """)
            rows = cursor.fetchall()
        return rows

    def fetchSortSatisfactionScore(self):
        connect = self.connector()
        with connect:
            cursor = connect.cursor()
            cursor.execute("""SELECT  subjects.SubjectName , platforms.SatisfactionScoree
                        FROM subjects INNER JOIN platforms ON subjects.PID = platforms.PID
                        Order by platforms.SatisfactionScoree DESC""")
            rows = cursor.fetchall()
        return rows
