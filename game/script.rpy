
#Charather declaration
define winstonText = Character("Winston Steel")
define captain = Character("Captain") #thats us

default winstonPoints = 0 #points for winston

$ prevPoint = True #True for positive and False for negative


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

#hint button
screen hint_button(hint_text):
    textbutton "Hint" action Show("hint_screen", hint_text=hint_text) xpos 0.9 ypos 0.1
#hint screen
screen hint_screen(hint_text):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            text hint_text
            textbutton "Close" action Hide("hint_screen")



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


label chooseNPC:
    menu:
        "The Elder – Winston Steel":
            jump winstonInterview
        "The Younger Man - Dante Hawke":
            pause
        "The Young Woman – Nova Reed":
            pause

return



#define the hint message for the winston interview
#define accordingly for the other characters
define hint_message_winston = """Possible strengths:
-His deep knowledge of the settlement's history and seasoned approach to leadership are unmatched.
-His familiarity with the people and their needs provides continuity and stability, even in these turbulent times.

Possible Weaknesses:
-His grief has festered into anger, which could cloud his judgment and lead to harsh, undesirable decisions.
-There’s a growing malevolence in his demeanor, raising concerns about his capacity for mercy and fairness.
"""



label winstonInterview:
    #winston here is not an Character but an image
    show winston at left 

    #no charater given so it is narrated
    "First, the elder enters. His eyes, once filled with wisdom, now you get a sense of inner bitterness and deep-seated grief in him."
    " The recent loss of his wife and daughter has twisted his sorrow into a smoldering resentment. He takes a seat, his hands trembling slightly—not from age, but from barely suppressed rage."
    
    #hint button, send the hint message according to the character
    show screen hint_button(hint_text = hint_message_winston)
    
    #dialogue
    captain "Winston, it's good to see you. I know things have been tough lately. How are you holding up?"

    winstonText "Captain, I've seen better days, but I'm managing. The settlement needs stability, and I'm here to help, despite everything. How are you settling into your new role?"

    captain "It's been a whirlwind, to be honest. There's so much to take in, but I'm committed to leading Haven's Rest forward. Let's start with your insights—what do you think our top priority should be right now?"
    jump WinstonStage1
return


label WinstonStage1:
    menu:
        "Winston, amidst the chaos of Neo-Terra, what would you say is your greatest asset that has enabled you to survive and thrive as an elder? ":
            $ winstonPoints = winstonPoints + 2
            $ prevPoint = True
            "+2 Good question, open question"

            winstonText "Survival! That's the only thing that matters! We must gather enough resources and hold on to them. We must ration them if we don't have enough. We must guarantee that we have food to feed our people. I was good at it, pal."
            jump WinstonStage4
        
        "Winston. Your experience is invaluable to us all. I am sure that you will agree that among other important traits for a leader adaptability seems to be crucial. In your tenure as an elder, what challenges have you faced where this trait proved indispensable? ":
            $ winstonPoints =  winstonPoints + 1
            $ prevPoint = True
            "+1 Suggestive question, less value"
            
            winstonText "The rise and fall of factions, the scarcity of resources, the constant threat of marauders - it all was a great part of our everyday nightmare, kid. But through flexibility and resourcefulness, I've weathered them all."
            jump WinstonStage2
        
        "Winston, what made you take a decision to join me as an advisor for our settlement even though you earlier voluntarily stepped down from the role of a leader yourself?":
            $ winstonPoints -= 2
            $ prevPoint = False
            "-2 hostile approach - poor practice"

            winstonText "Listen kid, I think you are not feeling ground under your feet. I was not looking forward for this. I dont want any of this. But at the same time I don’t think that you have what it takes. People asked me, but I am still not sure that I am willing…..and you are not helping either."

            jump WinstonStage2

return


label WinstonStage4:
    menu:
        "I appreciate your honesty. I will definitely think about what you said. My another question will be about handling pressure here at Haven`s Rest. Resilience in the face of adversity - a quality much needed in our world. How do you personally cope with the constant pressure and hardships of leadership without succumbing to despair? " if prevPoint == False:
            $ winstonPoints = winstonPoints + 2
            $ prevPoint = True
            "+2"
            winstonText "It's about finding solace in the small victories, Captain. Whether it's salvaging a vital resource or witnessing the resilience of our people, I draw strength from these moments to keep pressing forward, no matter how dire the circumstances."

        "Resilience in the face of adversity - a quality much needed in our world. How do you personally cope with the constant pressure and hardships of leadership without succumbing to despair? " if prevPoint == True:
            $ winstonPoints = winstonPoints + 2
            $ prevPoint = True
            "+2 "

            winstonText "It's about finding solace in the small victories, Captain. Whether it's salvaging a vital resource or witnessing the resilience of our people, I draw strength from these moments to keep pressing forward, no matter how dire the circumstances."

    menu:
        "Your dedication to the future of Neo-Terra is evident, Winston. Before we conclude, is there anything else you'd like to share about your strengths or aspirations for this land? " if prevPoint == True:
            $ winstonPoints = winstonPoints + 2
            $ prevPoint = True
            "+2 "
            winstonText "Only this, Captain - that no matter how bleak the outlook may seem, as long as there are leaders willing to stand tall and fight for what's right, there's always hope for a brighter tomorrow in Neo-Terra."

        "I appreciate your honesty. I will definitely think about what you said. Your dedication to the future of Neo-Terra is evident, Winston. Before we conclude, is there anything else you'd like to share about your strengths or aspirations for this land?  " if prevPoint == False:
            $ winstonPoints = winstonPoints + 2
            $ prevPoint = True
            "+2 "
            winstonText "Only this, Captain - that no matter how bleak the outlook may seem, as long as there are leaders willing to stand tall and fight for what's right, there's always hope for a brighter tomorrow in Neo-Terra."

    captain "Yeah Yeah, I hear you, old man. Let us agree to disagree. But overall - how bad are things around here. Do you think I can handle this with your help?"
    
    winstonText "….?????" 

    "Winstons once again takes a deep breath in, but this time only exhales with a heavy sound. After a few seconds of silence he speaks"

    captain "Listen, Cap, you don’t seem like a bad or evil person, but it takes more to lead people. Confidence in your own strengths and capabilities is invaluable. I appreciate that you are able to question your skills, but you must be strong. So my answer is - I hope yes, but this ain’t gonna be pretty…..kid."

return
    

#Main start point of the game
label start:
    # jump introduction
    jump chooseNPC

    "End of demo. Thanks for playing!"
return