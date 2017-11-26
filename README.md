# Team 3.14Buddies -- Shakil Rafi, Anish Shenoy, Caleb Smith-Salzberg, Charles Weng
## SoftDev Fall Project #02 - ArRESTed Development

We put the PI in API

### Overview

Our webiste mimicks the popular game show Jeopardy! We integrated two APIs: [Jservice](http://www.jservice.io/) and [GettyImages](http://developers.gettyimages.com/en/). Two players enter their names and select 5 categories they'd like to compete in on the homepage. Next, a board of 20 questions sorted by value is shown and players can choose the question theyd like to answer. The question is displayed and the user can input their answer. Once an answer is submitted, the correct answer is shown along with a corresponding image of the answer. Te site keeps track of each user's point total throughout the game. The game ends once all questions have been answered.

### Dependencies

1. Python
2. Flask

If you don't have flask installed, just run this command in your terminal:

```$ pip install flask```

### Instructions

1. Clone this repo
  * In the terminal, run 
  ```$ git clone https://github.com/Anish2454/3.14Buddies.git```

2. Procure a Getty-Images API Key
  * Head over to the [Registration Page](https://developer.gettyimages.com/member/register) and sign up.
  * Check the email you signed up with for a confirmation link. Click the link.
  * Once you click the confirmation link, you should see your key listed under your name.
  * Copy this link into the "gettykeys.txt" file in the util folder of the project
  
3. Run the application
  * In the terminal, run
    ```$ python app.py```
  * Navigate to "localhost:5000" in your browser and have fun!




