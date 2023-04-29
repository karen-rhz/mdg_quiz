import pandas
from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.title("Discover Madagascar 🇲🇬")
screen.bgpic("mdg_22-regions.gif")

score = 0
user_guess_list = []
learn_region = []
regions = pandas.read_csv("region_data5.csv")
regions_list = regions.region.to_list()

while len(user_guess_list) < 22:
    user_guess = screen.textinput(title=f"{len(user_guess_list)}/22 Guess a region",
                                  prompt="Name one region in Madagascar. "
                                         "For multiple words, Don't add \"-\" in between 2 words").title()
    if user_guess == "Exit":
        for region in regions_list:
            if region not in user_guess_list:
                learn_region.append(region)
        new_data = pandas.DataFrame(learn_region)
        new_data.to_csv("regions_to_learn.csv")
        break

    if user_guess in regions_list:
        x = int(regions[regions.region == user_guess].x)
        y = int(regions[regions.region == user_guess].y)
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(user_guess)
        user_guess_list.append(user_guess)

screen.exitonclick()