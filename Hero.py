import random

class Soldier:
    def init(self, number, team):
        self.team = team
        self.number = number
 
    def go_to_hero(self, hero):
        return hero.number, self.number
 
class Hero:
    def init(self, number, team_number, team): 
        self.team_number = team_number
        self.number = number
        self.lvl = 0
        self.team = team
 
    def up_lvl(self):
        self.lvl += 1
 
    def add_soldier(self, soldier):
        return self.team.append(soldier)
 
    def look_count_team(self):
        return len(self.team)
 
hero_team_first = Hero(1, 3, [])
hero_team_second = Hero(2, 2, [])
count = 0
while count < 10:
    team_for_soldier = random.randrange(1, 3)
    number_for_soldier = random.random()
    if team_for_soldier == 1:
        hero_team_first.add_soldier(Soldier(number_for_soldier, team_for_soldier))
    else:
        hero_team_second.add_soldier(Soldier(number_for_soldier, team_for_soldier))
        count += 1   
 
    if hero_team_first.look_count_team() > hero_team_second.look_count_team():
        hero_team_first.up_lvl()
    else:
        hero_team_second.up_lvl()
 
print(hero_team_first.team[0].go_to_hero(hero_team_first))