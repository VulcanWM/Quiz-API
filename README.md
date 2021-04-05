# **QUIZ API**
This is an API made in Python in which you can get random quiz questions really easily. 

The topics in this quiz API are art-literature, general-knowledge, geography, history, music, science-nature, sport, tv-films and all.

The difficulties in this API are 1, 2, 3, 4 and 5

Remember when inserting the topic name or number, don't include the <>, eg. when you want the topic tv-films, do tv-films not <tv-films>.

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

This code will print all the questions in a certain difficulty:
```py
import requests
response = requests.get("https://api.vulcanwm.repl.co/api/allquestionsdif/<difficulty>")
print(response.json())
```

This code will print a random question in a certain difficulty:
```py
import requests
response = requests.get("https://api.vulcanwm.repl.co/api/randomdif/<difficulty>")
print(response.json())
```

This code will print a certain amount of questions in a certain difficulty:
```py
import requests
response = requests.get("https://api.vulcanwm.repl.co/api/randomnumdif/<difficulty>/<num>")
print(response.json())
```

If you get an error in any of those, do the code below which will print the error if you are doing something wrong (response exists)
```py
print(reponse.content)
```