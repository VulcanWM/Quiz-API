This is the code for how to use this API in **Python**

This code will print all the questions:
```py
import requests
response = requests.get("https://quizapi.vulcanwm.com/api/all")
print(response.json())
```

This code will print all the questions in a certain topic:
```py
import requests
response = requests.get("https://quizapi.vulcanwm.com/api/allquestions/<topic_name>")
print(response.json())
```

This code will print a random question in a certain topic:
```py
import requests
response = requests.get("https://quizapi.vulcanwm.com/api/random/<topic_name>")
print(response.json())
```

This code will print a certain amount of questions in a certain topic:
```py
import requests
response = requests.get("https://quizapi.vulcanwm.com/api/randomnum/<topic_name>/<num>")
print(response.json())
```

This code will print all the questions in a certain difficulty:
```py
import requests
response = requests.get("https://quizapi.vulcanwm.com/api/allquestionsdif/<difficulty>")
print(response.json())
```

This code will print a random question in a certain difficulty:
```py
import requests
response = requests.get("https://quizapi.vulcanwm.com/api/randomdif/<difficulty>")
print(response.json())
```

This code will print a certain amount of questions in a certain difficulty:
```py
import requests
response = requests.get("https://quizapi.vulcanwm.com/api/randomnumdif/<difficulty>/<num>")
print(response.json())
```

If you get an error in any of those, do the code below which will print the error if you are doing something wrong (response exists)
```py
print(reponse.content)
```