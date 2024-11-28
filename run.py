import random

class Options:
    """Defines the options"""
    def __init__(self, number, country, capital, incorrect_1, incorrect_2):
        self.number = number
        self.country = country
        self.capital = capital
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2 
    
    def the_question(self):
        """the question"""
        print(f"Question {self.number}: What is the capital of {self.country}?")
        options = [self.capital, self.incorrect_1, self.incorrect_2]
        random.shuffle(options)
        print('A: ', options[0])
        print('B: ', options[1])
        print('C: ', options[2])
        return options
    
def the_quiz():
    """Country, capital and two incorrect options stored here"""
    dictionary = [
        {
            'country': 'the United States', 'capital': 'Washington DC', 'incorrect_1': 'Los Angeles', 'incorrect_2': 'New York',
        },
        {
            'country': 'China', 'capital': 'Beijing', 'incorrect_1': 'Hong Kong', 'incorrect_2': 'Shanghai',
        },
        {
            'country': 'Germany', 'capital': 'Berlin', 'incorrect_1': 'Hamburg', 'incorrect_2': 'Munich',
        },
        {
            'country': 'Japan', 'capital': 'Tokyo', 'incorrect_1': 'Hiroshima', 'incorrect_2': 'Osaka',
        },
        {
            'country': 'India', 'capital': 'New Dheli', 'incorrect_1': 'Chennai', 'incorrect_2': 'Mumbai',
        },
        {
            'country': 'the United Kindgom', 'capital': 'London', 'incorrect_1': 'Birmingham', 'incorrect_2': 'Manchester',
        },
        {
            'country': 'France', 'capital': 'Paris', 'incorrect_1': 'Lyon', 'incorrect_2': 'Nice',
        },
        {
            'country': 'Italy', 'capital': 'Rome', 'incorrect_1': 'Milan', 'incorrect_2': 'Naples',
        },
        {
            'country': 'Canada', 'capital': 'Ottawa', 'incorrect_1': 'Montreal', 'incorrect_2': 'Toronto',
        },
        {
            'country': 'Brazil', 'capital': 'Brasilia', 'incorrect_1': 'Rio de Janerio', 'incorrect_2': 'Sao Paulo',
        }
    ]
    
    score = 0

    for index, question in enumerate(dictionary):
        question = Options(
            number=index + 1,
            country=question["country"],
            capital=question["capital"],
            incorrect_1=question["incorrect_1"],
            incorrect_2=question["incorrect_2"]
        )
        options = question.the_question()
        while True:
            available_options = input("Please select and option of A, B or C, then press Enter:\n")
            if available_options.upper() not in ['A', 'B', 'C']:
                print("That is not a valid answwer, please select A, B or C")
            else:
                break

        if available_options.upper() == "A" and options[0] == question.capital:
            print("Well done, that is the correct answer")
            score += 1
            print("Score", score)
        elif available_options.upper() == "B" and options[1] == question.capital:
            print("Well done, that is the correct answer")
            score += 1
            print("Score", score)
        elif available_options.upper() == "C" and options[2] == question.capital:
            print("Well done, that is the correct answer")
            score += 1
            print("Score", score)
        else:
            print("Sorry, you have chosen an incorrect option")

the_quiz()