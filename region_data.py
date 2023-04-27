from turtle import Screen

# Screen setup
screen = Screen()
screen.title("Discover Madagascar 🇲🇬")
screen.bgpic("mdg_22-regions.gif")

# TODO: Get coordinates to each region


# method found on stackoverflow
def get_mouse_click_coor(x, y):
    print(x, y)


# .onscreenclick : a function with two arguments which will be called
# with the coordinates of the clicked point on the canva
screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()

# Diana, 124, 425.0
# Sava, 185, 364.0
# Sofia, 72, 283.0
# Analanjirofo, 153, 179.0
# Boeny, -85, 194.0
# Betsiboka, -6.0, 128.0
# Alaotra-Mangoro, 76, 82.0
# Atsinanana, 112, 17.0
# Melaky, -178, 97.0
# Bongolava, -90, 25.0
# Itasy, 10, 32.0
# Vakinakaratra, -41, -11.0
# Haute-Matsiatra, -175, -100.0
# Amoroni Mania, -40, -79.0
# Ihorombe, -44, -128.0
# Atsimo-Atsinanana, 43, -187.0
# Androy, -62, -198.0
# Anosy, -238, -325.0
# Atsimo-Andrefana, -92, -266.0
# Vtovavy Fitovinany, 3, -336.0
# Menabe, -137, -454.0
# Analamanga, -67, -425.0
