# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
# define screenText = Character('', kind=nvl)



init:
    #these are the inports for the image of the slides
    #text centering was a problem so we opted for this solution
    #resizing is necessary for the images to fit the screen
    image slide1:
        "Slide1.JPG"
        xysize(1280,720)
    image slide2:
        "Slide2.JPG"
        xysize(1280,720)
    image slide3:
        "Slide3.JPG"
        xysize(1280,720)
    image slide4:
        "Slide4.JPG"
        xysize(1280,720)
    image slide5:  
        "Slide5.JPG"
        xysize(1280,720)
    image slide6:
        "Slide6.JPG"
        xysize(1280,720)
    image slide7:
        "Slide7.JPG"
        xysize(1280,720)
    image slide8:
        "Slide8.JPG"
        xysize(1280,720)
    image slide9:
        "Slide9.JPG"
        xysize(1280,720)
    image slide10:
        "Slide10.JPG"
        xysize(1280,720)
    image slide11:
        "Slide11.JPG"
        xysize(1280,720)
    image slide12:
        "Slide12.JPG"
        xysize(1280,720)
    image slide13:
        "Slide13.JPG"
        xysize(1280,720)
    image slide14:
        "Slide14.JPG"
        xysize(1280,720)
    image slide15:
        "Slide15.JPG"
        xysize(1280,720)
    image slide16:
        "Slide16.JPG"
        xysize(1280,720)




# The game starts here.

label introduction:


    scene slide1
    pause 
    scene slide2
    pause
    scene slide3
    pause
    scene slide4
    pause
    scene slide5
    pause
    scene slide6
    pause
    scene slide7
    pause
    scene slide8
    pause
    scene slide9
    pause
    scene slide10
    pause
    scene slide11
    pause
    scene slide12
    pause
    scene slide13
    pause
    scene slide14
    pause
    scene slide15
    pause
    scene slide16
    pause




    return




label start:
    jump introduction

return