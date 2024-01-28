import pandas
from flask import Flask, render_template,request
from DB import DataLayer

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def mainPage():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        file = request.files['Excel']
        file.save(file.filename)
        ValidGaranties = pandas.read_excel(file, 'Sheet1')
        ValidGaranties = ValidGaranties.values.tolist()

        InvalidGaranties = pandas.read_excel(file, 'Sheet2')
        InvalidGaranties = InvalidGaranties.values.tolist()
        print(InvalidGaranties)

        with DataLayer.Database('db_file.sqlite') as db:
            db.insertExcel(ValidGaranties)

        return render_template('index.html', tsk1_img=validGaranties, tbl=InvalidGaranties)




@app.route("/readExcel",methods=['POST','GET'])
def readExcel():
    file = request.files['Excel']
    file.save(file.filename)
    df = pandas.read_excel(file,'Sheet1')
    l = df.values.tolist()

    with DataLayer.Database('db_file.sqlite') as db:
        db.insertExcel(l)

    return "done!"






if __name__ == '__main__':
    app.run(debug=True)