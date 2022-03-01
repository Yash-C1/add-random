from django.shortcuts import render
from flask import Flask, jsonify,render_template
import random
app=Flask(__name__)

@app.route('/')
def main_page():
    x_add = random.randint(0,9)
    y_add = random.randint(0,9)

    output_text_add = "Question : What is {} + {}".format(x_add,y_add)


    #Storing the answer to the question to compare it with user's answer
    ans = x_add + y_add
    d={}
    d['Question'] = output_text_add
    d['Answer'] = ans
    return d

if __name__=='__main__':
    app.run(debug=True)