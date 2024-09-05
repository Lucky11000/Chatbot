import datetime

class TravelChatbot:
    def __init__(self):
        self.destination = None
        self.travel_dates = None
        self.budget = None
        self.preferences = None
        self.health_problems= None

    def ask_destination(self):
        while True:
            self.destination = input("Where would you like to travel to? (city, country, or region) ")
            if self.destination:
                print(f"Great choice! {self.destination} is a wonderful destination.")
                break
            else:
                print("Please enter a valid destination.")

    def ask_travel_dates(self):
        while True:
            try:
                start_date = input("When would you like to start your trip? (YYYY-MM-DD) ")
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
                end_date = input("When would you like to end your trip? (YYYY-MM-DD) ")
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")


                if start_date < end_date:
                    self.travel_dates = (start_date, end_date)
                    print(f"Your trip will be from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}.")
                    print(f"the trip is of {end_date-start_date}")
                    break
                else:
                    print("Invalid dates. Please ensure the start date is before the end date.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def ask_budget(self):
        while True:
            try:
                self.budget = float(input("What is your budget for the trip? "))
                if self.budget > 0:
                    print(f"Your budget is {self.budget:.2f} Rupees.")
                    break
                else:
                    print("Invalid budget. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ask_preferences(self):
        preferences = []
        while True:
            print("What type of activities would you like to do on your trip? (select one or more)")
            print("1. Outdoor adventures (hiking, camping, etc.)")
            print("2. Cultural experiences (museums, historical sites, etc.)")
            print("3. Food ")
            print("4. Relaxation and wellness (beaches, spas, etc.)")
            print("5. Urban exploration (cities, shopping, etc.)")
            choice = input("> ")
            if choice in ["1", "2", "3", "4", "5"]:
                preferences.append(choice)
                print("Would you like to add another preference? (yes/no)")
                add_another = input("> ")
                if add_another.lower() != "yes":
                    break
            else:
                print("Invalid choice. Please select a valid option.")
        self.preferences = preferences

    def provide_recommendations(self):
        print("Based on your preferences, here are some recommendations for your trip:")
        if "1" in self.preferences:
            print(f"For outdoor adventures, consider visiting {self.destination}'s Kayaking , Munnar Zipline.")
        if "2" in self.preferences:
            print(f"For cultural experiences, visit {self.destination}'s museums, historical sites, or attend a local festival.")
        if "3" in self.preferences:
            print(f"For food and wine tastings, try {self.destination}'s local cuisine at specific cafes.")
        if "4" in self.preferences:
            print(f"For relaxation and wellness, visit {self.destination}'s beaches, spas, or take a yoga class.")
        if "5" in self.preferences:
            print(f"For urban exploration, explore {self.destination}'s cities, shopping districts, or take a guided tour.")

    def start_conversation(self):
        print("Welcome to our travel chatbot!")
        self.ask_destination()
        self.ask_travel_dates()
        self.ask_budget()
        self.ask_preferences()
        self.provide_recommendations()
        print("It was great chatting with you! Have a wonderful trip!")
        print("we will get back to you with a planned trip just for you")

if __name__ == "__main__":
    chatbot = TravelChatbot()
    chatbot.start_conversation()