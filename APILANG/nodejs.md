This is the code for how to use this API in **NodeJS**

This code will print all the questions:
```js
const axios = require('axios');
axios.get('https://quizapi.vulcanwm.com/api/all')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```

This code will print all the questions in a certain topic:
```js
const axios = require('axios');
axios.get('https://quizapi.vulcanwm.com/api/allquestions/<topic_name>')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```

This code will print a random question in a certain topic:
```js
const axios = require('axios');
axios.get('https://quizapi.vulcanwm.com/api/random/<topic_name>')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```

This code will print a certain amount of questions in a certain topic:
```js
const axios = require('axios');
axios.get('https://quizapi.vulcanwm.com/api/randomnum/<topic_name>/<num>')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```

This code will print all the questions in a certain difficulty:
```js
const axios = require('axios');
axios.get('https://quizapi.vulcanwm.com/api/allquestionsdif/<difficulty>')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```

This code will print a random question in a certain difficulty:
```js
const axios = require('axios');
axios.get('https://quizapi.vulcanwm.com/api/randomdif/<difficulty>')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```

This code will print a certain amount of questions in a certain difficulty:
```js
const axios = require('axios');
axios.get('https://quizapi.vulcanwm.com/api/randomnumdif/<difficulty>/<num>')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```