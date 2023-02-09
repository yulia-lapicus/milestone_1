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
results = []

# Loop through 3 times to collect data from 3 users
for i in range(3):
    # Ask the user's name and welcome them to the game
    user_name = input("What is your name? ")
    print("\nWelcome to the University Trivia, " + user_name + "!")
    print("Answer the following questions. Let's see how well you know the University of Washington!")

    # Set up a variable to keep track of the correct answers
    correct_answers = 0

    # Ask random questions and analyze if the answer is correct or incorrect
    for i, q in enumerate(random.sample(questions, len(questions))):
        answer = input(f"{q['question']}: ")
        if answer.lower() == q['answer'].lower():
            correct_answers += 1
            result = "Correct"
        else:
            result = "Incorrect"
        results.append({"Name": user_name, "Question": q["question"], "Answer": q["answer"], "Result": result})

    # Print the results
    print(f"\nYou, {user_name}, answered {correct_answers} questions correctly.")

# Store the results in a dataframe
results_data = pd.DataFrame(results)
# print("Results:")
# print(results_data)

# Plot the results for each user using matplotlib
for user in results_data["Name"].unique():
    user_results = results_data[results_data["Name"] == user]
    user_results.groupby("Result").count().plot(kind='bar', y='Question', legend=False)
    plt.ylabel("Questions")
    plt.xlabel("Result")
    plt.title("Trivia Results for " + user)
    plt.show()
