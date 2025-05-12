#Step 1 : Ask the questions from the user with relevant subject
#Step 2 : Store the answers in a dictionary
#Step 3 : Calculate the score based on the answers given by the user
#Step 4 : Display the score to the user
import random

def Ask_Questions():

  questions_list =[
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Mark Twain", "B) William Shakespeare", "C) Charles Dickens", "D) Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
        "answer": "A"
    },
    {
        "question": "What is the speed of light?",
        "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 600,000 km/s"],
        "answer": "A"
    }
  ]

  name =input("Enter your name: ")
  print(f"Hey {name} , Welcome to the Quiz App !!!")
  no_of_questions = int(input("How many questions do you want to answer? "))
  while no_of_questions > len(questions_list):
    print("Sorry, this is out of range. Please try again.")
    no_of_questions = int(input("How many questions do you want to answer? "))

  print("Great! Let's start the quiz.")  
  print("Please answer the following questions...")

  
  questions = random.sample(questions_list, no_of_questions)
  correct_answers={}

  for i in range(no_of_questions):
    print(f"Q{i+1}) : {questions[i]["question"]}")
    print(f"Options : {questions[i]["options"]}")
    answer = input("Enter your answer (A,B,C,D) :").upper()

    if answer ==questions[i]["answer"]:
      print("You are correct!")
      correct_answers[questions[i]["question"]] = questions[i]["answer"]
    else:
      print(f"You are wrong! The correct answer is {questions[i]["answer"]}")

  print("Your correct answers are : ")
  print(correct_answers)
  calculate_score(correct_answers,no_of_questions)

def calculate_score(correct_answers,no_of_questions):
  
  score =len(correct_answers)*10

  print(f"Your score is {score} out of {no_of_questions*10}")
  print("Thank you for playing the quiz!")


Ask_Questions()

