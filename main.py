from flask import Flask, render_template, request
import random
#import numpy as np
#import pandas as pd

app = Flask(__name__)

original_questions = {
 #Format is 'question':[options]
 'Taj Mahal':['Agra','New Delhi','Mumbai','Chennai'],
 'Great Wall of China':['China','Beijing','Shanghai','Tianjin'],
 'Petra':['Ma'an Governorate','Amman','Zarqa','Jerash'],
 'Machu Picchu':['Cuzco Region','Lima','Piura','Tacna'],
 'Egypt Pyramids':['Giza','Suez','Luxor','Tanta'],
 'Colosseum':['Rome','Milan','Bari','Bologna'],
 'Christ the Redeemer':['Rio de Janeiro','Natal','Olinda','Betim']
}

def filter_product(a, b):
  n = a.size()
  c  = np.array([[]])
  for i in range(n):
    c.append([a[i][0]+b[i][0]])
  return c

def booler(a):
  if a>0:
    return 1
  else:
    return 0

@app.route('/')
def quiz():
	return render_template('main.html', q = questions, o = questions)


@app.route('/quiz', methods=['POST'])
def quiz_answers():
 correct = 0
 for i in questions.keys():
  answered = request.form[i]
  #print(answered)
  if original_questions[i][0] == answered:
   correct = correct+1
 return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

@app.route('/quizi', methods=['POST'])
def output():
	return '<h1> HI </h1>'


if __name__ == '__main__':
 app.run(debug=True)
'''
weights = np.array([[ 1,  0,  2,  0,  0],
       [ 2,  0,  0,  0,  0],
       [ 0,  1,  0,  0,  1],
       [ 0,  2,  0,  2,  0],
       [-1,  0,  2,  0,  0],
       [ 0,  2,  0,  0,  3],
       [ 0,  1,  0,  1,  2],
       [ 0,  0,  0, -2,  0],
       [ 0,  0,  1,  0,  0],
       [-1,  0,  0,  0,  0],
       [ 0,  0,  3,  0,  0],
       [ 1,  0,  0,  0,  0],
       [ 0,  0,  0, -5,  0],
       [-2,  0,  0,  0,  0],
       [ 0,  3,  0,  0,  0],
       [ 0, -2,  0,  0,  0],
       [-1,  0,  0,  0,  0],
       [ 1,  0,  0,  0,  0],
       [ 0,  3,  0,  0,  2],
       [ 0,  0,  3,  0,  0],
       [ 0,  4,  0,  0,  4],
       [ 0,  0,  1,  0,  0],
       [ 1, -1,  0,  0, -2],
       [ 0, -2,  0, -3,  0],
       [ 0,  2,  0,  0,  3],
       [ 0, -3,  0,  0, -3],
       [ 4,  0,  0,  0,  0],
       [ 0, -1,  4,  1,  0]])

# response = 28 row x 1 col

personality = np.dot(weights.T,response) # (5x28)x(28x1) = (5x1)

profession_weights  = np.array([[ 3,  8,  1,  4,  9],
	[ 5,  9,  3,  1, 10],
	[ 6, 10,  2,  1, 10],
	[ 5, 10,  1,  1, 10],
	[ 2,  7,  5,  1,  7],
	[ 3,  8,  3,  4,  8],
	[ 5,  9,  5,  5,  8],
	[ 1,  5,  3,  3,  4],
	[ 4,  7,  9, 10,  8],
	[10,  3,  1,  1,  7],
	[ 5,  6,  2,  4,  6],
	[ 8,  3,  1,  1,  9],
	[ 5,  6,  9,  8,  7],
	[ 1,  7,  5,  3,  7],
	[ 2,  8,  8,  3,  7],
	[ 1,  4,  7,  7,  6],
	[ 3,  9,  4,  2,  8],
	[ 2,  7,  9,  2,  7],
	[ 3, 10,  2,  1,  7],
	[ 1,  4,  5,  2,  6],
	[ 1,  7,  6,  1,  7],
	[ 1,  7,  1,  1,  8],
	[ 2,  9,  2,  2,  8],
	[ 1,  7,  1,  2,  6]])      #24x5

answer = np.dot(profession_weights, personality)  # (24x5)x(5x1) 

min_iq = np.array[130, 130, 130, 130, 120, 120, 120, 110, 110, 110, 110, 110, 100,
       100, 100, 100,  90,  90,  90,  90,  80,  80,  80,  80]            # min iq array
min_iq -= iq
min_iq = booler(min_iq)

answer = filter_product(answer, min_iq.T)
total_sum = np.sum(answer)
answer = (answer/total_sum)*100
'''
# Now display the answer beautifully in the web page


