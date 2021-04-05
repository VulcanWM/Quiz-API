import flask
from flask import request, jsonify, render_template
import random
from questions import questions
app = flask.Flask(__name__)
app.config["DEBUG"] = True

topics = ["art-literature", "general-knowledge", "geography", "history", "music", "science-nature", "sport", "tv-films", "all"]

diffs = ["1", "2", "3", "4", "5"]

@app.route('/', methods=['GET'])
def home():
    return "Quiz API"


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

app.run(host='0.0.0.0', port=8080)