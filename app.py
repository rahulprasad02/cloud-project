from flask import Flask, render_template, request
import pickle 
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods= ['POST'])
def predict_placement():
    ssc_p = float(request.form.get('ssc_p'))
    hsc_p = float(request.form.get('hsc_p'))
    deg_p = float(request.form.get('deg_p'))
    etest_p = float(request.form.get('etest_p'))
    mba_p = float(request.form.get('mba_p'))


    result = float(model.predict(np.array([ssc_p, hsc_p, deg_p, etest_p, mba_p]).reshape(1,5)))
    result = round((result*12) / 100000, 2)


    return render_template('index.html', result = result)


if __name__ == "__main__":
    app.run(debug=True)