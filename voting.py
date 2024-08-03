
# count the total votes and print the output in the form of a dictionary where the key is the candidate name and value is the total number of votes in the order of maximum votes.

class Election: #Created a class with name Election
    def __init__(self):
        self.candidates = {}

    def add_candidates(self, name):  #Function to add a candidate to election classs
        self.candidates[name] = 0

    def all_candidates(self):       #Function to print all the candidates that added
        print("Added Candidates: ")
        for candidate in self.candidates.keys():
            print(candidate)

    def vote(self, name):       #Function for casting a vote
        if name in self.candidates:
            self.candidates[name] += 1
            return True
        else:
            return False

    def print_winner(self):     #Function to print the winner of election
        max_votes = max(self.candidates.values())
        winners = [name for name, votes in self.candidates.items() if votes == max_votes]
        for winner in winners:
            print(winner)

    def print_votes(self):      #Function to show the total votes for each candidates
        sorted_candidates = sorted(self.candidates.items(), key=lambda x: x[1], reverse=True)
        for name, votes in sorted_candidates:
            print(f"{name}: {votes}")




election = Election()

election.add_candidates("Bruce")
election.add_candidates("Clark")
election.add_candidates("Diana")

election.all_candidates()

election.vote("Bruce")
election.vote("Diana")
election.vote("Bruce")
election.vote("Clark")

print("\nVotes:")
election.print_votes()

print("\nWinner:")
election.print_winner()
