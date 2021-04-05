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
    "Answer": "stephenie meyer",
    "Difficulty": "3/5"},
  {
    "Topic": "art-literature",
    "Question": "What was Frankenstein's first name?",
    "Answer": "jolly roger",
    "Difficulty": "4/5"},
  {
    "Topic": "general-knowledge",
    "Question": "What is the only anagram of the word 'english'?",
    "Answer": "shingles",
    "Difficulty": "2/5"},
  {
    "Topic": "general-knowledge",
    "Question": "Gala, Jonagold and Pink Lady are varieties of which fruit?",
    "Answer": "apple",
    "Difficulty": "2/5"},
  {
    "Topic": "geography",
    "Question": "On which side of the road do people drive in Japan?",
    "Answer": "left",
    "Difficulty": "3/5"},
  {
    "Topic": "geography",
    "Question": "Fort Knox lies in which American state?",
    "Answer": "kentucky",
    "Difficulty": "3/5"},
  {
    "Topic": "history",
    "Question": "Who was Queen for just nine days in 1553?",
    "Answer": "lady jane grey",
    "Difficulty": "2/5"},
  {
    "Topic": "history",
    "Question": "Which American war hero during the Revolutionary War swapped sides to join the British and become a spy?",
    "Answer": "benedict arnold",
    "Difficulty": "4/5"},
  {
    "Topic": "history",
    "Question": "Who was the first U.S. Secretary of War?",
    "Answer": "henry knox",
    "Difficulty": "4/5"},
  {
    "Topic": "history",
    "Question": "Who founded the American Democratic Party?",
    "Answer": "andrew jackson and martin van buren",
    "Difficulty": "4/5"},
  {
    "Topic": "history",
    "Question": "What was the first major battle of the Revolutionary War?",
    "Answer": "Battles of Lexington and Concord",
    "Difficulty": "2/5"},
  {
    "Topic": "history",
    "Question": "What two American founding fathers went to Kings College, or currently Columbia University?",
    "Answer": "alexander hamilton and john jay",
    "Difficulty": "4/5"},
  {
    "Topic": "history",
    "Question": "Who were the five writers of the American Declaration of Independence?",
    "Answer": "thomas jefferson, john adams, benjamin franklin, robert livingston, roger sherman",
    "Difficulty": "5/5"},
  {
    "Topic": "history",
    "Question": "Who is most often regarded as the worst American president?",
    "Answer": "james buchanan",
    "Difficulty": "3/5"},
  {
    "Topic": "history",
    "Question": "What battle did the British surrender at in the Revolutionary War?",
    "Answer": "the battle of yorktown",
    "Difficulty": "2/5"},
  {
    "Topic": "history",
    "Question": "What nations took the American's side in the Revolutionary War?",
    "Answer": "france and spain",
    "Difficulty": "3/5"},
  {
    "Topic": "history",
    "Question": "Who caused the French and Indian war, or the Seven Years War?",
    "Answer": "george washington",
    "Difficulty": "4/5"},
  {
    "Topic": "history",
    "Question": "Who were the 3 members of Washington's Cabinet?",
    "Answer": "alexander hamilton, thomas jefferson, henry knox",
    "Difficulty": "4/5"},
  {
    "Topic": "history",
    "Question": "Who established the First Lady position in the U.S.?",
    "Answer": "dolley madison",
    "Difficulty": "4/5"
  }
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