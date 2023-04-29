from turtle import Screen

import pandas

# Screen setup
screen = Screen()
screen.title("Discover Madagascar 🇲🇬")
screen.bgpic("mdg_22-regions.gif")

# TODO: Get coordinates to each region


# # method found on stackoverflow
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# # .onscreenclick : a function with two arguments which will be called
# # with the coordinates of the clicked point on the canva
# screen.onscreenclick(get_mouse_click_coor)
#
# screen.mainloop()

# TODO: CREATE A .CSV FILE WITH THIS LIST
data = [
    ("Diana", 124, 425),
    ("Sava", 185, 364),
    ("Sofia", 72, 283),
    ("Analanjirofo", 153, 179),
    ("Boeny", -85, 194),
    ("Betsiboka", -6.0, 128),
    ("Alaotra Mangoro", 76, 82),
    ("Atsinanana", 112, 17),
    ("Melaky", -178, 97),
    ("Bongolava", -90, 25),
    ("Analamanga", 10, 32),
    ("Itasy", -35, -12.0),
    ("Vakinakaratra", -43, -63),
    ("Haute-Matsiatra", -65, -194),
    ("Amoron'i Mania", -44, -128),
    ("Ihorombe", -88, -270),
    ("Menabe", -167, -106),
    ("Vatovavy-Fitovinany", 34, -192),
    ("Atsimo Atsinanana", 5, -340),
    ("Atsimo Andrefana", -221, -326),
    ("Androy", -132, -477),
    ("Anosy", -80, -407)
    ]

# region_data = pandas.DataFrame(data)
# region_data.to_csv("region_data.csv")

# region_data = pandas.DataFrame(data, columns=["region", "x", "y"])
# region_data.to_csv("region_data2.csv")

# region_data = pandas.DataFrame.from_records(data).to_csv("region_data3.csv")

# region_data = pandas.DataFrame.DataFrame(data).to_csv("region_data4.csv")

region_data = pandas.DataFrame(data, columns=["region", "x", "y"])
region_data.to_csv("region_data5.csv", index=False)