#shape = [x, y, x2, y2]
environment = 'cup'

#Initialise lists to off screen
shapelist = [-100, -100, -100, -100]
shapelist2 = [-100, -100, -100, -100]
shapelist3 = [-100, -100, -100, -100]
shapelist4 = [-100, -100, -100, -100]

if environment == 'demo':
    shapelist = [750, 500, 1920, 900]
    shapelist2 = [1000, 200, 1200, 50]
    shapelist3 = [100, 300, 1000, 200]
    shapelist4 = [-200, 500, 100, 300]
elif environment == 'cup':
    shapelist = [640, -17.5, 1000, -17.5]
    shapelist2 = [500, 750, 640, -17.5]
    shapelist3 = [1000, -17.5, 1140, 750]
ShapeList = [ shapelist, shapelist2, shapelist3, shapelist4]
Shape_Amount = len(ShapeList)



