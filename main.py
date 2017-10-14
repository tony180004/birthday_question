import numpy as np
import pandas as pd
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

birthday_q_a = 'birth2.csv'
questions = pd.read_csv(birthday_q_a, usecols=[0, 1, 2]).values
i = [0]
which = random.sample(range(questions.shape[0]), questions.shape[0])

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/getQuestions')
def get_questions():
	if i[0] == questions.shape[0]:
		i[0] = 0
		return jsonify(ans='全部題目結束')
	ques = questions[which[i[0]]][1]
	ans = questions[which[i[0]]][2]
	i[0] += 1
	return jsonify(ques=ques, ans = ans)


if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8080, debug=True)
