import turtle

import pandas
from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.title("Discover Madagascar 🇲🇬")
screen.bgpic("mdg_22-regions.gif")

score = 0
user_guess_list = []
regions = pandas.read_csv("region_data.csv")

print(regions)

screen.exitonclick()