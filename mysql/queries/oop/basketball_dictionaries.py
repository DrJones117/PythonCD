class Player:

    new_team = []

    def __init__(self, player):
        self.name = "name"
        self.age = "age"
        self.position = "position"
        self.team = "team"

        Player.new_team.append(self)



kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
    

kevin = Player(kevin)
print(kevin)

jason = Player(jason)
print(jason)

kyrie = Player(kyrie)
print(kyrie)

print(Player.new_team)
