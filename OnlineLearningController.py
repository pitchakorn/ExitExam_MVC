from flask import Flask, render_template
from OnlineLearningModel import OnlineLearningModel
app = Flask(__name__)
OnlineLearningModel = OnlineLearningModel()

@app.route("/")
def showDataOnlineLearning():
    table1 = OnlineLearningModel.fetchDataSubjectAndLecturer()
    table2 = OnlineLearningModel.fetchCountSubjects()
    table3 = OnlineLearningModel.fetchSortSatisfactionScore()
    return render_template('index.html', dataTable1 = table1, dataTable2 = table2 , dataTable3 = table3)

if __name__ == '__main__':
    app = app.run(debug=True)
