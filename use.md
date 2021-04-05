# **QUIZ API**
This is an API made in Python in which you can get random quiz questions really easily. 

The topics in this quiz API are art-literature, general-knowledge, geography, history, music, science-nature, sport, tie-break, tv-films, all

Remember when inserting the topic name or number, don't include the <>, eg. when you want the topic tie-break, do tie-break not <tie-break>.

The ways to use this API in Python is below.

This code will print all the questions in a certain topic:
```py
import requests
response = requests.get("https://api.vulcanwm.repl.co/api/allquestions/<topic_name>")
print(response.json())
```

This code will print a random question in a certain topic:
```py
import requests
response = requests.get("https://api.vulcanwm.repl.co/api/random/<topic_name>")
print(response.json())
```

This code will print a certain amount of questions in a certain topic:
```py
import requests
response = requests.get("https://api.vulcanwm.repl.co/api/randomnum/<topic_name>/<num>")
print(response.json())
```