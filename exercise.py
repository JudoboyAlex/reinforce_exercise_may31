ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

people = {}
def winner(ballots):
    for ballot in ballots:
       
        for medal, name in ballot.items():
            points = 0
            if medal == 'gold':
                points = 3
            elif medal == 'silver':
                points = 2
            elif medal == 'bronze':
                points = 1

            if name in people:
                people[name] += points
            else:
                people[name] = points
            print(people)

    max_score = 0
    winner = ''
    for person, score in people.items():
        if score > max_score:
            max_score = score
            winner = person
    return winner

winner = winner(ballots)
print(winner)
