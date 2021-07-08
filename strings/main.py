# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player0 = "Ruud Gullit"
player1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player0 + " " + str(goal_0) + ", " + player1 + " " + str(goal_1)

report = f"{player0} scored in the {goal_0}nd minute"'\n'f"{player1} scored in the {goal_1}th minute"

print(scorers)
print(report)

"""=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-="""


player = "Hans van Breukelen"

first_name = player[:player.find(" ")]
last_name = player[player.rfind(" ") + 1:]


name_short = player[:1] + "." + " " + player[player.find(" ") + 1:]
last_name_len = len(player[player.find(" ") + 1:])


chant1 = (first_name + "! ") * len(first_name)
chant = chant1[:-1]
good_chant = chant[0] != " "

print(first_name)
print(last_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
