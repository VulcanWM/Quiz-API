import flask
from flask import request, jsonify, render_template
import random
app = flask.Flask(__name__)
app.config["DEBUG"] = True

topics = ["art-literature", "general-knowledge", "geography", "history", "music", "science-nature", "sport", "tie-break", "tv-films", "all"]

questions = [
  {
    "Topic": "art-literature",
    "Question": "Who wrote Twilight series of novels?",
    "Answer": "Stephenie Meyer",
    "Difficulty": "3/5"},
  {
    "Topic": "art-literature",
    "Question": "What was Frankenstein's first name?",
    "Answer": "Jolly Roger",
    "Difficulty": "4/5"},
  {
    "Topic": "general-knowledge",
    "Question": "What is the only anagram of the word 'english'?",
    "Answer": "Shingles",
    "Difficulty": "2/5"},
  {
    "Topic": "general-knowledge",
    "Question": "Gala, Jonagold and Pink Lady are varieties of which fruit?",
    "Answer": "Apple",
    "Difficulty": "2/5"},
  {
    "Topic": "Geography",
    "Question": "On which side of the road do people drive in Japan?",
    "Answer": "Left",
    "Difficulty": "3/5"},
  {
    "Topic": "Geography",
    "Question": "Fort Knox lies in which American state?",
    "Answer": "Kentucky",
    "Difficulty": "3/5"}
]

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

app.run(host='0.0.0.0', port=8080)