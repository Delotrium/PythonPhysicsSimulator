#shape = [x, y, x2, y2]
environment = 'filter'

#Initialise lists to off screen
shapelist = [-100, -100, -100, -100]
shapelist2 = [-100, -100, -100, -100]
shapelist3 = [-100, -100, -100, -100]
shapelist4 = [-100, -100, -100, -100]
shapelist5 = [-100, -100, -100, -100]
shapelist6 = [-100, -100, -100, -100]
shapelist7 = [-100, -100, -100, -100]
shapelist8 = [-100, -100, -100, -100]

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

ShapeList = [ shapelist, shapelist2, shapelist3, shapelist4, shapelist5, shapelist6, shapelist7, shapelist8]
Shape_Amount = len(ShapeList)



