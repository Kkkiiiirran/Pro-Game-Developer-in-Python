import random

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer
    
    def is_correct(self, choice):
        return self.answer.lower() == choice.lower()

class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))  # Shuffle questions
        self.score = 0

    def start(self, player):
        print("\nWelcome to the Quiz!\n")
        for index, question in enumerate(self.questions, 1):
            print(f"Q{index}: {question.text}")
            for i, option in enumerate(question.options, 1):
                print(f"  {i}. {option}")
            
            choice = input("Enter the correct option number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(question.options):
                selected_option = question.options[int(choice) - 1]
                if question.is_correct(selected_option):
                    print("Correct! ✅\n")
                    player.increment_score()
                else:
                    print(f"Wrong! ❌ The correct answer was: {question.answer}\n")
            else:
                print("Invalid input. Skipping question.\n")
        
        print(f"Quiz Over! {player.name}, your final score is: {player.score}/{len(self.questions)}\n")

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increment_score(self):
        self.score += 1
    
    def display_score(self):
        return self.score

if __name__ == "__main__":
    questions_list = [
        Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
        Question("Which language is primarily used for web development?", ["Python", "Java", "JavaScript", "C++"], "JavaScript"),
        Question("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"], "Albert Einstein"),
        Question("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
        Question("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Osmium", "Hydrogen"], "Oxygen")
    ]
    
    player_name = input("Enter your name: ")
    player = Player(player_name)
    quiz = Quiz(questions_list)
    quiz.start(player)
    print(player.display_score())


