import pandas as pd
import matplotlib.pyplot as plt
import random


# Trivia questions and answers
questions = [
    {"question": "Where was located the first UW campus?", "answer": "Downtown Seattle"},
    {"question": "Who is the official mascot of the University of Washington?", "answer": "Dubs"},
    {"question": "When was the University of Washington founded?", "answer": "1861"},
    {"question": "Where is located the MSTI program (city)?", "answer": "Bellevue"},
    {"question": "What is the name of the second official UW mascot?", "answer": "Harry"}
]

# Set up variables to store the results
correct_answers = 0
results = []


# Ask the user's name and welcome them to the game
user_name = input("What is your name? ")
print("\nWelcome to the University Trivia, " + user_name + "!")
print("Answer the following questions. Let's see how well you know the University of Washington!")


# Ask random questions and analyze if the answer is correct or incorrect
# The 'enumerate' function is used to keep a record of the position (i) of each question as the loop iterates.
for i, q in enumerate(random.sample(questions, len(questions))):
    answer = input(f"{q['question']}: ")
    if answer.lower() == q['answer'].lower():
        correct_answers += 1
        result = "Correct"
    else:
        result = "Incorrect"
    results.append({"Question": q["question"], "Answer": q["answer"], "Result": result})


# Print the results
print(f"\n You, {user_name}, answered {correct_answers} questions correctly.")


# Store the results in a dataframe
results_data = pd.DataFrame(results)
print("\n Results:")
print(results_data)


# Plot the results using matplotlib
results_data.groupby("Result").count().plot(kind='bar', y='Question', legend=False)
plt.ylabel("Questions")
plt.xlabel("Result")
plt.title("Trivia Results for " + user_name)
plt.show()
