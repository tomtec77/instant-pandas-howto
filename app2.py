from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/report2/<month>')

def report(month):
    from pandas_datareader.data import DataReader
    ibm = DataReader('ibm', 'yahoo', '2010-01-01', '2010-12-31')
    df = ibm[ibm.index.month == int(month)]
    return render_template('report2.html', df=df.to_html(classes='table'))

if __name__ == '__main__':
    app.run()