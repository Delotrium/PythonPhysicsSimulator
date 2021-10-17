import random

#shape = [x, y, x2, y2]
environment = 'course1'
environmentOptions = [ 'demo', 'defualt', 'tube', 'pool', 'cup', 'filter', 'course1']
#Initialise lists to off-screen
shapelist = [-100, -100, -100, -100]
shapelist2 = [-100, -100, -100, -100]
shapelist3 = [-100, -100, -100, -100]
shapelist4 = [-100, -100, -100, -100]
shapelist5 = [-100, -100, -100, -100]
shapelist6 = [-100, -100, -100, -100]
shapelist7 = [-100, -100, -100, -100]
shapelist8 = [-100, -100, -100, -100]
shapelist9= [-100, -100, -100, -100]
shapelist10 = [-100, -100, -100, -100]
shapelist11 = [-100, -100, -100, -100]
shapelist12 = [-100, -100, -100, -100]
shapelist13 = [-100, -100, -100, -100]
shapelist14 = [-100, -100, -100, -100]
shapelist15 = [-100, -100, -100, -100]
shapelist16 = [-100, -100, -100, -100]

if environment == 'demo':
    shapelist = [750, 500, 1920, 900]
    shapelist2 = [1000, 200, 1200, 50]
    shapelist3 = [100, 300, 1000, 200]
    shapelist4 = [-200, 500, 100, 300]
elif environment == 'cup':
    shapelist = [640, -17.5, 1000, -17.5]
    shapelist2 = [500, 750, 640, -17.5]
    shapelist3 = [1000, -17.5, 1140, 750]
elif environment == 'pool':
    shapelist = [384, -10.5, 1536, -10.5]
    shapelist2 = [384, 250, 384, -10.5]
    shapelist3 = [1536, -10.5, 1536, 250]
elif environment == 'tube':
    shapelist = [900, -10.5, 1000, -10.5]
    shapelist2 = [900, -10.5, 900, 600]
    shapelist3 = [1000, -10.5, 1000, 600]
elif environment == 'filter':
    #pool area under filter
    shapelist = [384, -10.5, 1536, -10.5]
    shapelist2 = [384, 250, 384, -10.5]
    shapelist3 = [1536, -10.5, 1536, 250]
    #filter pipe 
    shapelist4 = [910, 125, 910, 500] 
    shapelist5 = [990, 125, 990, 500]
    #filter head
    shapelist6 = [910, 500, 775, 720]
    shapelist7 = [990, 500, 1125, 720]

elif environment == 'course1':
    shapelist =[0, 900, 750, 700]
    shapelist2 = [800, 700, 1550, 900]
    shapelist3 =[775, 550, 550, 450]
    shapelist4 = [775, 550, 1000, 450]
    shapelist5= [-20, 550, 750,200]
    shapelist6 = [1550, 550, 800 , 200]
    shapelist7 =[775, 150, 550, 50]
    shapelist8 = [775, 150, 1000, 50]
ShapeList = [ shapelist, shapelist2, shapelist3, shapelist4, shapelist5, shapelist6, shapelist7, shapelist8, shapelist9, shapelist10, shapelist11, shapelist12, shapelist13,
             shapelist14, shapelist16]
Shape_Amount = len(ShapeList)



