# Steps to deploying python app to Heroku

- login to Heroku, open cmd

  ```
  heroku login
  ```

- Create app

  ```
  heroku create car-prediction-api
  ```

  above command will return git repo link

- Clone empty git repo and paste all the files here

  ```
  git clone <git link>
  cd car-prediction-api
  ```

- Push code

  ```
  heroku git:remote -a car-prediction-api
  git commit -am "initial code"
  git push heroku master
  ```
