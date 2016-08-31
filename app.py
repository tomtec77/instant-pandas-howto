from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/report')
def report():
    df = pd.DataFrame(np.random.randn(10,10))
    return render_template('report.html', df=df.to_html())

if __name__ == '__main__':
    app.run()