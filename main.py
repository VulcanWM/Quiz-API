import flask
import os
from flask import request, jsonify, render_template
import random
import json
import uuid
f = open('questions.json')
questions = json.load(f)
app = flask.Flask(__name__)
app.config["DEBUG"] = True
topics = ["art-literature", "general-knowledge", "geography", "history", "music", "science-nature", "sport", "tv-films", "all"]

diffs = ["1", "2", "3", "4", "5"]

@app.route('/', methods=['GET'])
def home():
    return "Quiz API"

@app.route("/addquestion")
def addquestion():
  return render_template("addquestion.html")

@app.route("/addquestion", methods=["POST", "GET"])
def addquestionfunc():
  if request.method == "POST":
    theques = {"id": str(uuid.uuid4()), "Topic": request.form['topic'], "Question": request.form['question'], "Answer": request.form['answer'], "Difficulty": request.form['difficulty']}
    thef = open('wait.json')
    wait = json.load(thef)
    wait.append(theques)
    thef.close()
    with open('wait.json', 'w') as outfile:
      json.dump(wait, outfile)
    outfile.close()
    return "Question waiting to be verified!"

@app.route("/api/all")
def all():
  return jsonify(questions)

@app.route('/api/allquestions/<topic>', methods=['GET'])
def api_all(topic):
  if topic not in topics:
    return "This is not a topic name!"
  if topic.lower() == "all":
    return jsonify(questions)
  results = []
  for question in questions:
      if question['Topic'].lower() == topic:
          results.append(question)
  return jsonify(results)


@app.route('/api/random/<topic>', methods=['GET'])
def api_random(topic):
  if topic not in topics:
    return "This is not a topic name!"
  if topic.lower() == "all":
    question = random.choice(questions)
    return jsonify(question)
  results = []
  for question in questions:
      if question['Topic'].lower() == topic:
          results.append(question)
  result = random.choice(results)
  return jsonify(result)

@app.route('/api/randomnum/<topic>/<num>', methods=['GET'])
def api_randomnum(topic, num:int):
  if topic not in topics:
    return "This is not a topic name!"
  if topic.lower() == "all":
    question = random.choice(questions)
    return jsonify(question)
  results = []
  for question in questions:
      if question['Topic'].lower() == topic:
          results.append(question)
  if int(num) > len(results):
    return f"There are only {len(results)} questions in the {topic} topic!"
  end = []
  for i in range(int(num)):
    result = random.choice(results)
    end.append(result)
    index = results.index(result)
    del results[index]
  return jsonify(end)

@app.route('/api/allquestionsdif/<diff>', methods=['GET'])
def apidif_all(diff):
  if diff not in diffs:
    return "This is not a difficulty level name!"
  results = []
  for question in questions:
      if question['Difficulty'].split("/")[0] == diff:
          results.append(question)
  return jsonify(results)


@app.route('/api/randomdif/<diff>', methods=['GET'])
def apidif_random(diff):
  if diff not in diffs:
    return "This is not a difficulty level name!"
  results = []
  for question in questions:
      if question['Difficulty'].split("/")[0] == diff:
          results.append(question)
  result = random.choice(results)
  return jsonify(result)

@app.route('/api/randomnumdif/<diff>/<num>', methods=['GET'])
def apidif_randomnum(diff, num):
  if diff not in diffs:
    return "This is not a difficulty level name!"
  results = []
  for question in questions:
      if question['Difficulty'].split("/")[0] == diff:
          results.append(question)
  if int(num) > len(results):
    return f"There are only {len(results)} questions in the {num} difficulty!"
  end = []
  for i in range(int(num)):
    result = random.choice(results)
    end.append(result)
    index = results.index(result)
    del results[index]
  return jsonify(end)

@app.route("/verifywait")
def verifywait():
  return render_template("verifywait.html")

@app.route("/verifywait", methods=["POST", "GET"])
def verifywaitfunc():
  if request.method == "POST":
    if request.form['password'] == os.getenv("password"):
      waitfile = open("wait.json")
      wait = json.load(waitfile)
      wait2 = []
      for verify in wait:
        if verify['id'] == request.form['id']:
          for i in wait:
            if i['id'] != request.form['id']:
              wait2.append(i)
          with open('wait.json', 'w') as outfile:
            json.dump(wait2, outfile)
          outfile.close()
          if request.form['a/d'] == "a":
            question = verify
            del verify['id']
            questions.append(question)
            with open('questions.json', 'w') as outfile:
              json.dump(questions, outfile)
            outfile.close()
            return "Accepted question and added it to the questions!"
          else:
            return "Denied question"
    else:
      return "Wrong password!"


app.run(host='0.0.0.0', port=8080)