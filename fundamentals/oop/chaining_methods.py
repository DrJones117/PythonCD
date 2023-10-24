class User:
    def __init__(self, first, last, email, age, rewards=False, gold_card=0):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards_member = rewards
        self.gold_card_points = gold_card

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print("Age ", self.age)
        print("Rewards? ", self.is_rewards_member)
        print("Points ", self.gold_card_points)
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self,amount):
        self.gold_card_points -= amount
        return self



new_user = User("Judah", "Kahler", "judah.kahler1345@somemail.sniff", "19",)
new_user.enroll().spend_points(50).display_info()

second_user = User("Bill", "Bob", "Blahblah@mail", 46)
second_user.enroll().spend_points(80).display_info()


third_user = User("Nigel", "Dill", "mail.mail.mail@mial.com", 99)