from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app=Flask(__name__)
# instantiate object
#loading the different saved model for different disease
parkinsons_predict=pickle.load(open('parkinsons.pkl', 'rb'))

@app.route('/') # instancing one page (homepage)
def home():
    return render_template("home.html")
# ^^ open home.html, then see that it extends layout.
# render home page.


@app.route('/parkinsons/') # instancing child page
def parkinsons():
    return render_template("parkinsons.html")

@app.route('/predictparkinson/',methods=['POST']) 
def predictparkinsons():      #function to predict parkinsons disease
    int_features=[x for x in request.form.values()]
    processed_feature_parkinsons=[np.array(int_features,dtype=float)]
    prediction=parkinsons_predict.predict(processed_feature_parkinsons)
    if prediction[0]==1:
        display_text="This person has Parkinson's"
    else:
        display_text="This person doesn't have Parkinson's"
    return render_template('parkinsons.html',output_text="Result: {}".format(display_text))

if __name__=="__main__":
    app.run(debug=True)