
#Charather declaration
define winstonText = Character("Winston Steel")
define captain = Character("Captain") #thats us

default winstonPoints = 0 #points for winston
default villageResources = 100
default villagePopulation = 100

$ prevPoint = True #True for positive and False for negative
$ interview = False
$ winstinterview = False
$ winstonGood = False
$ winstonBad = False
$ winstonNeutral = False
$ dantegood = False
$ novagood = False


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
    image slide8_1:
        "Slide8_1.JPG"
        xysize(1280,720)
    image slide9:
        "Slide9.png"
        xysize(1280,720)
    image slide10:
        "Slide10.png"
        xysize(1280,720)
    image slide11:
        "Slide11.png"
        xysize(1280,720)
    image slide12:
        "Slide12.png"
        xysize(1280,720)
    image slide13:
        "Slide13.png"
        xysize(1280,720)
    image slide14:
        "Slide14.png"
        xysize(1280,720)
    image slide15:
        "Slide15.png"
        xysize(1280,720)
    image slide16:
        "Slide16.JPG"
        xysize(1280,720)
    image winstonchoice_aftermath:
        "w_af.png"
        xysize(1280,720)
    image first_task_defences:
        "ft_def.png"
        xysize(1280,720)
    image first_task_resources:
        "ft_res.png"
        xysize(1280,720)
    image first_task_study:
        "ft_st.png"
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
    $ interview = False
    $ winstinterview = False
    $ winstonGood = False
    $ winstonBad = False
    $ winstonNeutral = False
    $ dantegood = False
    $ novagood = False

    play music "main_music.mp3"
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
    scene slide8_1
    pause
    scene slide9
    "The Command Center is the heart of Haven's Rest, housed in a repurposed industrial warehouse fortified with metal plates and concrete."
    "Here, the settlement's leaders coordinate daily activities, defense strategies, and resource allocation. Solar panels on the roof provide power, and the walls are lined with maps, communication equipment, and emergency protocols."
    scene slide10
    "The Dining Hall is a large, communal space converted from an old factory cafeteria, where residents gather for meals prepared from rationed supplies and greenhouse-grown produce"
    "Long, sturdy tables and benches fill the room, fostering a sense of community as everyone shares stories and plans. The walls are adorned with murals depicting scenes of hope and survival, painted by the settlement’s artists."
    scene slide11
    "The Hospital is a critical facility, located in what was once a small office building, now transformed into a medical center."
    "It is staffed by a team of doctors and nurses who provide care with limited supplies, relying heavily on scavenged medical equipment and herbal remedies. The building's basement serves as an improvised quarantine area for those suffering from radiation sickness or other contagious diseases."
    scene slide12
    "The Greenhouse is an underground facility using hydroponic systems to grow essential crops, ensuring a steady supply of fresh vegetables and herbs."
    "It is managed by a team of agricultural experts who meticulously monitor the plants' health and growth conditions. The Greenhouse is also a place of hope, symbolizing the potential for renewal and life amidst the desolation."
    scene slide13
    "The Workshop is a bustling hub of activity, where engineers and craftsmen repair and create tools, machinery, and other necessary items from scavenged materials."
    "Located in a former auto repair shop, it is filled with the sounds of welding, hammering, and the hum of makeshift generators. This building is vital for maintaining the settlement's infrastructure and innovation efforts."
    scene slide14
    "The Schoolhouse, set in a reinforced classroom building from the pre-apocalyptic era, is where children and adults alike receive education and training."
    "Classes cover basic literacy, survival skills, and technical knowledge crucial for the community’s future. It is a beacon of hope, emphasizing the importance of knowledge and learning even in the direst circumstances."
    scene slide15
    "The Water Purification Plant is a lifeline for Haven's Rest, located in a renovated utility building."
    "It uses a combination of old-world technology and new innovations to purify contaminated water, providing the settlement with a safe drinking supply. Managed by a team of skilled technicians, the plant is crucial for maintaining the health and well-being of all residents."
    scene slide16
    play music "interview.mp3"
    pause
    return

#add the labels for other chars and add the jumps
label chooseNPC:
    scene interview_room
    menu:
        "The Elder – Winston Steel":
            jump winstonInterview
        "The Younger Man - Dante Hawke":
            show dante at left
            "Hi! Unfortunately I'm not yet finished. Try Winston Steel."
            hide dante
            jump chooseNPC
        "The Young Woman – Nova Reed":
            show nova at left
            "Hi! Unfortunately I'm not yet finished. Try Winston Steel."
            hide nova
            jump chooseNPC
        "Make final decision" if interview:
            jump choice

return

label choice:
    menu:
        "Winston Steel" if winstonGood:
            jump winstonchoice
        "Dante Hawke" if dantegood:
            pause
        "Nova Reed" if novagood == True:
            pause
        "Back":
            jump chooseNPC
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
    #no charater given so it is narrated

    if winstinterview == True:
        "You already made interview with him"
        jump chooseNPC

    "First, the elder enters. His eyes, once filled with wisdom, now you get a sense of inner bitterness and deep-seated grief in him."
    " The recent loss of his wife and daughter has twisted his sorrow into a smoldering resentment. He takes a seat, his hands trembling slightly—not from age, but from barely suppressed rage."
    
    #hint button, send the hint message according to the character
    show screen hint_button(hint_text = hint_message_winston)
    
    #dialogue
    show captain at right
    captain "Winston, it's good to see you. I know things have been tough lately. How are you holding up?"
    hide captain
    show winston at left
    winstonText "Captain, I've seen better days, but I'm managing. The settlement needs stability, and I'm here to help, despite everything. How are you settling into your new role?"
    hide winston
    show captain at right
    captain "It's been a whirlwind, to be honest. There's so much to take in, but I'm committed to leading Haven's Rest forward. Let's start with your insights—what do you think our top priority should be right now?"
    jump WinstonStage1
return

label WinstonStage1:
    # menu's are for options
    menu:
        "Winston, amidst the chaos of Neo-Terra, what would you say is your greatest asset that has enabled you to survive and thrive as an elder? ":
            $ winstonPoints = winstonPoints + 2
            $ prevPoint = True
            hide captain
            show winston at left
            winstonText "Survival! That's the only thing that matters! We must gather enough resources and hold on to them. We must ration them if we don't have enough. We must guarantee that we have food to feed our people. I was good at it, pal."

            jump WinstonStage2
        
        "Winston. Your experience is invaluable to us all. I am sure that you will agree that among other important traits for a leader adaptability seems to be crucial. In your tenure as an elder, what challenges have you faced where this trait proved indispensable? ":
            $ winstonPoints =  winstonPoints + 1
            $ prevPoint = True
            hide captain
            show winston at left
            winstonText "The rise and fall of factions, the scarcity of resources, the constant threat of marauders - it all was a great part of our everyday nightmare, kid. But through flexibility and resourcefulness, I've weathered them all."
            jump WinstonStage2
        
        "Winston, what made you take a decision to join me as an advisor for our settlement even though you earlier voluntarily stepped down from the role of a leader yourself?":
            $ winstonPoints -= 2
            $ prevPoint = False
            hide captain
            show winston at left
            winstonText "Listen kid, I think you are not feeling ground under your feet. I was not looking forward for this. I dont want any of this. But at the same time I don’t think that you have what it takes. People asked me, but I am still not sure that I am willing…..and you are not helping either."

            jump WinstonStage2
return

label WinstonStage2:
    hide winston
    show captain at right
    if prevPoint == True:
        menu: 
            "Resourcefulness is a commendable trait. How do you mobilize the remnants of Neo-Terra's society to work towards common goals despite the odds stacked against us? ":
                $ winstonPoints = winstonPoints+1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "It's about instilling a sense of purpose, Captain. Everyone here has felt the sting of loss, but by rallying them around a shared vision of rebuilding, we find strength in unity."

            "My thoughts are that one of the main aspects for common survival - alliance-building - requires a delicate balance. Can you share a specific instance where your diplomatic skills turned a potential conflict into cooperation, showcasing your prowess as a leader?":
                $ winstonPoints = winstonPoints+1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "There was a dispute over territory between two rival factions, both on the brink of open conflict. Through mediation and compromise, I helped them see the mutual benefit of cooperation, averting bloodshed and forging a lasting partnership."
                

    else:
        menu: 
            "Oh I see. I must have guessed myself. Let us proceed. Can you share a specific instance where your diplomatic skills turned a potential conflict into cooperation, showcasing your prowess as a leader?":
                $ winstonPoints = winstonPoints+1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "There was a dispute over territory between two rival factions, both on the brink of open conflict. Through mediation and compromise, I helped them see the mutual benefit of cooperation, averting bloodshed and forging a lasting partnership."
                
            "I see. Allow me to ask something else. How do you mobilize the remnants of Neo-Terra's society to work towards common goals despite the odds stacked against us? ":
                $ winstonPoints = winstonPoints+1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "It's about instilling a sense of purpose, Captain. Everyone here has felt the sting of loss, but by rallying them around a shared vision of rebuilding, we find strength in unity."

            "Maybe adaptability and resourcefulness is important, but I genuinely believe that keeping a high spirit is what brings us to our ultimate success. Don’t you think so?":
                $ prevPoint = False
                hide captain
                show winston at left
                "Winston takes a deep breath in and with a loud sound spits a large oozy matter on the floor in front of him."
                winstonText  "There is nothing as stupid as trying to motivate hungry stomachs with a lousy speech."
                winstonText "If you believe that high spirit can be built without enough resources in your warehouse and without skills to handle the matter when your options are limited, I doubt that we can work together, lad."

    jump WinstonStage3
return


# label WinstonStage2:
    
#     if prevPoint == True:
#         menu: 
#             "Resourcefulness is a commendable trait. How do you mobilize the remnants of Neo-Terra's society to work towards common goals despite the odds stacked against us? ":
#                 $ winstonPoints = winstonPoints+1
#                 $ prevPoint = True
#                 "+1 point"
#                 winstonText "It's about instilling a sense of purpose, Captain. Everyone here has felt the sting of loss, but by rallying them around a shared vision of rebuilding, we find strength in unity."
                       
#     else:
#         menu: 
#             "Oh I see. I must have guessed myself. Let us proceed. Can you share a specific instance where your diplomatic skills turned a potential conflict into cooperation, showcasing your prowess as a leader?":
#                 $ winstonPoints = winstonPoints+1
#                 $ prevPoint = False
#                 "+1 point"
#                 winstonText "There was a dispute over territory between two rival factions, both on the brink of open conflict. Through mediation and compromise, I helped them see the mutual benefit of cooperation, averting bloodshed and forging a lasting partnership."
                

#     if prevPoint == True:
#         menu:
#             "My thoughts are that one of the main aspects for common survival - alliance-building - requires a delicate balance. Can you share a specific instance where your diplomatic skills turned a potential conflict into cooperation, showcasing your prowess as a leader?":
#                 $ winstonPoints = winstonPoints+1
#                 $ prevPoint = True
#                 "+1 point"
#                 winstonText "There was a dispute over territory between two rival factions, both on the brink of open conflict. Through mediation and compromise, I helped them see the mutual benefit of cooperation, averting bloodshed and forging a lasting partnership."
                
#     else:
#         menu:
#             "I see. Allow me to ask something else. How do you mobilize the remnants of Neo-Terra's society to work towards common goals despite the odds stacked against us? ":
#                 $ winstonPoints = winstonPoints+1
#                 $ prevPoint = False
#                 "+1 point"
#                 winstonText "It's about instilling a sense of purpose, Captain. Everyone here has felt the sting of loss, but by rallying them around a shared vision of rebuilding, we find strength in unity."
                
     
#     captain "Maybe adaptability and resourcefulness is important, but I genuinely believe that keeping a high spirit is what brings us to our ultimate success. Don’t you think so?"
#     "Winston takes a deep breath in and with a loud sound spits a large oozy matter on the floor in front of him."
#     winstonText  "There is nothing as stupid as trying to motivate hungry stomachs with a lousy speech."
#     winstonText "If you believe that high spirit can be built without enough resources in your warehouse and without skills to handle the matter when your options are limited, I doubt that we can work together, lad."
#     jump WinstonStage3
# return

label WinstonStage3:
    hide winston
    show captain at right
    if prevPoint == True:
        menu:
            #there are if statments to check the previous question and give points accordingly
            #they are at the end of each option string -------->>>>
            "Unity amidst adversity, a powerful force indeed. In your leadership role, what strategies have you employed to foster this sense of unity among the disparate factions and survivors? ": 
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Diplomacy, negotiation, and occasionally, a show of strength when necessary. By finding common ground and emphasizing our shared humanity, I've been able to bridge divides and forge alliances."

            "Your ability to defuse tensions is admirable. In the face of external threats like mutant raids or environmental catastrophes, how do you inspire confidence and maintain order among the populace?" :
                $ winstonPoints = winstonPoints + 1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Diplomacy, negotiation, and occasionally, a show of strength when necessary. By finding common ground and emphasizing our shared humanity, I've been able to bridge divides and forge alliances."

            "I am confident and agree that food provision is important, but we are not mindless creatures. I still believe that faith and our trust in each other is what really matters. What are your thoughts on this? " :
                $ winstonPoints = winstonPoints - 2
                $ prevPoint = False
                hide captain
                show winston at left
                winstonText "Diplomacy, negotiation, and occasionally, a show of strength when necessary. By finding common ground and emphasizing our shared humanity, I've been able to bridge divides and forge alliances."
    
    else:
        menu:
                        
            "I apologize for my question. You are definitely right, in the current condition we must ensure the bare minimum if we hope to survive. In your leadership role, what strategies have you employed to foster this sense of unity among the disparate factions and survivors? " :
                $ winstonPoints = winstonPoints + 3
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Diplomacy, negotiation, and occasionally, a show of strength when necessary. By finding common ground and emphasizing our shared humanity, I've been able to bridge divides and forge alliances."


            "My bad, truly. I am sorry for that question. As I heard from people your ability to defuse tensions is admirable. In the face of external threats like mutant raids or environmental catastrophes, how do you inspire confidence and maintain order among the populace? " :
                $ winstonPoints = winstonPoints + 1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Diplomacy, negotiation, and occasionally, a show of strength when necessary. By finding common ground and emphasizing our shared humanity, I've been able to bridge divides and forge alliances."
            
            "Anyway. Feeding is important, but we are not animals. I still believe that faith and our trust in each other is what is really important. What are your thoughts on this? " :
                $ winstonPoints = winstonPoints - 5
                $ prevPoint = False
                hide captain
                show winston at left
                winstonText "Diplomacy, negotiation, and occasionally, a show of strength when necessary. By finding common ground and emphasizing our shared humanity, I've been able to bridge divides and forge alliances."

                if winstonPoints <= -5:
                    winstonText "Looking at you and listening to you makes me wonder if we ARE planning to survive after all. "
                    winstonText "But i guess I will not be here to see this happening. Goodbye, young fella, I wish your best in your future endeavors, but I am planning to head north and trust my word: there are those that are going to follow me."
                    "Winstons walks out of the door, with a loud spit on the flour"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText "Looking at you and listening to you makes me wonder if you possess the right skills to lead our people. But i guess time will show this. Mind what you say. In my humble opinion no religion can serve a good purpose when basic needs of our people are not fulfilled."

    jump WinstonStage4
return

label WinstonStage4:
    hide winston
    show captain at right
    if prevPoint == True:
        menu:
            
            "Resilience in the face of adversity - a quality much needed in our world. How do you personally cope with the constant pressure and hardships of leadership without succumbing to despair? " :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "It's about finding solace in the small victories, Captain. Whether it's salvaging a vital resource or witnessing the resilience of our people, I draw strength from these moments to keep pressing forward, no matter how dire the circumstances."

            "Your dedication to the future of Neo-Terra is evident, Winston. Before we conclude, is there anything else you'd like to share about your strengths or aspirations for this land? " :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Only this, Captain - that no matter how bleak the outlook may seem, as long as there are leaders willing to stand tall and fight for what's right, there's always hope for a brighter tomorrow in Neo-Terra."
    else:
        menu:
        
            "I appreciate your honesty. I will definitely think about what you said. Your dedication to the future of Neo-Terra is evident, Winston. Before we conclude, is there anything else you'd like to share about your strengths or aspirations for this land?  " :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Only this, Captain - that no matter how bleak the outlook may seem, as long as there are leaders willing to stand tall and fight for what's right, there's always hope for a brighter tomorrow in Neo-Terra."

            "I appreciate your honesty. I will definitely think about what you said. My another question will be about handling pressure here at Haven`s Rest. Resilience in the face of adversity - a quality much needed in our world. How do you personally cope with the constant pressure and hardships of leadership without succumbing to despair? " :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "It's about finding solace in the small victories, Captain. Whether it's salvaging a vital resource or witnessing the resilience of our people, I draw strength from these moments to keep pressing forward, no matter how dire the circumstances."

            "Yeah Yeah, I hear you, old man. Let us agree to disagree. But overall - how bad are things around here. Do you think I can handle this with your help?":
                hide captain
                show winston at left
                $ prevPoint = False
                winstonText "….?????" 
                "<Winstons once again takes a deep breath in, but this time only exhales with a heavy sound. After a few seconds of silence he speaks>"

                if winstonPoints <= -5:
                    winstonText "Looking at you and listening to you makes me wonder if we ARE planning to survive after all. But i guess I will not be here to see this happening."
                    winstonText "Goodbye, young fella, I wish your best in your future endeavors, but I am planning to head north and trust my word: there are those that are going to follow me."
                    "<Winstons walks out of the door, with a loud spit on the flour>"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText " Listen, Cap, you don’t seem like a bad or evil person, but it takes more to lead people. Confidence in your own strengths and capabilities is invaluable. I appreciate that you are able to question your skills, but you must be strong. So my answer is - I hope yes, but this ain’t gonna be pretty…..kid."
    jump WinstonStage5
return







label WinstonStage5:
    hide winston
    show captain at right
    if prevPoint == True:
        menu:
            
            "Your insights are invaluable, Winston. With the future of Neo-Terra hanging in the balance, what steps do you believe are crucial for us to take immediately to secure our survival and success?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "First and foremost, we must stabilize our resources. Securing food and water supplies is paramount. Next, we need to strengthen our defenses against external threats. Finally, fostering strong alliances and building trust within our community will create a solid foundation for rebuilding and growth."

            "Yes! Yes! This is what I am looking to achieve - a hope for our people. Let's talk about leadership. What qualities do you think are most essential in a leader, especially in such turbulent times?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "A leader must show resilience, some empathy, but sure decisiveness. When we’re in crisis, we look to leaders for direction. Be ready for tough decisions while understanding but remember people - this is crucial. Lead by example and they will follow."

            "Winston, with everything going wrong, do you ever wonder if it's all just a waste of time?":
                $ winstonPoints = winstonPoints - 4
                $ prevPoint = False
                hide captain
                show winston at left
                if winstonPoints <= -5:
                    winstonText "Looking at you and listening to you makes me wonder if we ARE planning to survive after all. But i guess I will not be here to see this happening."
                    winstonText "Goodbye, young fella, I wish your best in your future endeavors, but I am planning to head north and trust my word: there are those that are going to follow me."
                    "<Winstons walks out of the door, with a loud spit on the floor>"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText "<Winston's expression tightens, and he lets out a slow, measured breath.>" 
                    winstonText "Captain, there are moments when we start panicking, but sick thoughts won't get us anywhere. Every effort, every win, brings us closer to a better life. A waste of time??? You mean giving up on everything we've fought for?  We need to keep our focus and remember why we started this in the first place."
                
    else:
        menu:
        
            "True. I sure hope for that myself. Your insights are invaluable, Winston. With the future of Neo-Terra hanging in the balance, what steps do you believe are crucial for us to take immediately to secure our survival and success?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "First and foremost, we must stabilize our resources. Securing food and water supplies is paramount. Next, we need to strengthen our defenses against external threats. Finally, fostering strong alliances and building trust within our community will create a solid foundation for rebuilding and growth."

            "I understand the gravity of our situation better now. Let's talk about leadership. What qualities do you think are most essential in a leader, especially in such turbulent times?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "A leader must show resilience, some empathy, but sure decisiveness. When we’re in crisis, we look to leaders for direction. Be ready for tough decisions while understanding but remember people - this is crucial. Lead by example and they will follow."

            "Winston, with everything going wrong, do you ever wonder if it's all just a waste of time?":
                $ winstonPoints = winstonPoints - 4
                $ prevPoint = False
                hide captain
                show winston at left
                if winstonPoints <= -5:
                    winstonText "Looking at you and listening to you makes me wonder if we ARE planning to survive after all. But i guess I will not be here to see this happening."
                    winstonText "Goodbye, young fella, I wish your best in your future endeavors, but I am planning to head north and trust my word: there are those that are going to follow me."
                    "<Winstons walks out of the door, with a loud spit on the floor>"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText "<Winston's expression tightens, and he lets out a slow, measured breath.>" 
                    winstonText "Captain, there are moments when we start panicking, but sick thoughts won't get us anywhere. Every effort, every win, brings us closer to a better life. A waste of time??? You mean giving up on everything we've fought for?  We need to keep our focus and remember why we started this in the first place."
    jump WinstonStage6
return

label WinstonStage6:
    hide winston
    show captain at right
    if prevPoint == True:
        menu:
            
            "Winston, your dedication and experience are undeniable. As we strive to build a stronger community, what role do you think technological advancements should play in our strategy?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Technology is a double-edged sword, Cap. Yes, it can give efficiency in control and defense. On the other hand, we must not repeat same stupid mistakes of our fathers - don’t rely only on technology. Use it as a tool but keep our core values and resilience."

            "Let's address the elephant in the room, Winston. How do you propose we deal with dissent within our ranks? We can't afford to have internal conflicts when facing external threats." :
                $ winstonPoints = winstonPoints + 1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Dissent is natural for any crowd, especially in times of crisis. Transparency and open communication - this is what I know about dealing with such stuff. We must listen to grievances, handle conflicts, and find the exit from any fight. We build mutual respect and understanding  - we will resolve internal strife and keep our focus on the greater goal."

            " I wonder Winston, do you ever think maybe we're just overthinking all of this? Maybe things would sort themselves out if we just stopped worrying so much?":
                $ winstonPoints = winstonPoints - 5
                $ prevPoint = False
                hide captain
                show winston at left
                if winstonPoints <= -5:
                    winstonText "Looking at you and listening to you makes me wonder if we ARE planning to survive after all. But i guess I will not be here to see this happening."
                    winstonText "Goodbye, young fella, I wish your best in your future endeavors, but I am planning to head north and trust my word: there are those that are going to follow me."
                    "<Winstons walks out of the door, with a loud spit on the floor>"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText "<Winston's face tightens, frustration clear in his eyes.>" 
                    winstonText "My Lord! Kid, the luxury of inaction and blind optimism is not an option. Things will 'sort themselves out' you say???"
                    winstonText "You call a disaster upon us all. Planning, decisive actions, and relentless effort - this is the only way. Leader takes responsibilities seriously - if you’re the one - Stop looking for easy ways out."
                
    else:
        menu:
        
            "Got it. You're right, no panic. We can do this. Before we conclude I want to ask - your dedication and experience are undeniable, as we strive to build a stronger community, what role do you think technological advancements should play in our strategy?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Technology is a double-edged sword, Cap. Yes, it can give efficiency in control and defense. On the other hand, we must not repeat same stupid mistakes of our fathers - don’t rely only on technology. Use it as a tool but keep our core values and resilience."

            "Got it. You're right, no panic. But now let's address the elephant in the room, Winston. How do you propose we deal with dissent within our ranks? We can't afford to have internal conflicts when facing external threats." :
                $ winstonPoints = winstonPoints + 1
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "A leader must show resilience, some empathy, but sure decisiveness. When we’re in crisis, we look to leaders for direction. Be ready for tough decisions while understanding but remember people - this is crucial. Lead by example and they will follow."

            "Who is panicking? I am not, are you? Not even that - do you ever think maybe we're just overthinking all of this? Maybe things would sort themselves out if we just stopped worrying so much?":
                $ winstonPoints = winstonPoints - 5
                $ prevPoint = False
                hide captain
                show winston at left
                if winstonPoints <= -5:
                    winstonText "Looking at you and listening to you makes me wonder if we ARE planning to survive after all. But i guess I will not be here to see this happening."
                    winstonText "Goodbye, young fella, I wish your best in your future endeavors, but I am planning to head north and trust my word: there are those that are going to follow me."
                    "<Winstons walks out of the door, with a loud spit on the floor>"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText "<Winston's face tightens, frustration clear in his eyes.>" 
                    winstonText "My Lord! Kid, the luxury of inaction and blind optimism is not an option. Things will 'sort themselves out' you say???"
                    winstonText "You call a disaster upon us all. Planning, decisive actions, and relentless effort - this is the only way. Leader takes responsibilities seriously - if you’re the one - Stop looking for easy ways out."
    jump WinstonStage7    
return

label WinstonStage7:
    hide winston
    show captain at right
    if prevPoint == True:
        menu:
            
            "Winston, your insights have been invaluable throughout this discussion. As we prepare to face the challenges ahead, what final piece of advice would you give to ensure we stay united and focused on our mission?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Captain, my final advice is simple: never lose sight of our common vision. Always keep open dialogue with the folk, lead with integrity, honesty, and always remember that our strength is in our unity. We all must work together, to have any chance in this harsh reality."

            "Finally, Winston, how do you envision the future of Heaven’s Rest if we successfully implement all the strategies we've discussed today?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "If we stay the course and follow our strategies, I see this settlement to grow strong, self-sufficient, and, heh, who knows, even thriving at some point. A place where children can grow up in peace and safety. People respect each other, fight side by side with each other, survive together. Our struggles today will pave the way for a brighter tomorrow."

            "So, Winston, do you think we should just give up and find a nice cozy cave to hide in until this all blows over?":
                $ winstonPoints = winstonPoints - 10
                $ prevPoint = False
                hide captain
                show winston at left
                if winstonPoints <= -5:
                    winstonText " <Winston's expression hardens into a mask of cold fury.>"
                    winstonText "Captain, it’s clear you have no grasp of the gravity of our situation or the responsibility on your shoulders. Hiding in a cave? That's your solution?"
                    winstonText "You're unfit to lead if that’s your mindset. I’m done wasting my time with you. Goodbye, and good luck—you’ll need it."
                    "<Winston storms out of the room, slamming the door behind him.>"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText "<Winston's face turns red with anger, his eyes narrowing into a fierce glare.>" 
                    winstonText "Captain, your arrogance and dismissive attitude are exactly what's holding us back. Hiding away is not an option and never has been."
                    winstonText "If you think running from our problems will solve anything, you're gravely mistaken. We need leaders who are willing to face challenges head-on, not cowards looking for an easy way out. Get your act together or step aside for someone who will."
                
    else:
        menu:
        
            "Alright, okay. Sure. I was actually just testing you with the question about leaving things to run their course. Winston, your insights have been invaluable throughout this discussion. As we prepare to face the challenges ahead, what final piece of advice would you give to ensure we stay united and focused on our mission?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "Captain, my final advice is simple: never lose sight of our common vision. Always keep open dialogue with the folk, lead with integrity, honesty, and always remember that our strength is in our unity. We all must work together, to have any chance in this harsh reality."

            "Alright, okay. Sure. I was actually just testing you with the question about leaving things to run their course. Finally, how do you envision the future of Heaven’s Rest if we successfully implement all the strategies we've discussed today?" :
                $ winstonPoints = winstonPoints + 2
                $ prevPoint = True
                hide captain
                show winston at left
                winstonText "If we stay the course and follow our strategies, I see this settlement to grow strong, self-sufficient, and, heh, who knows, even thriving at some point. A place where children can grow up in peace and safety."
                winstonText "People respect each other, fight side by side with each other, survive together. Our struggles today will pave the way for a brighter tomorrow"

            "Stop bossing me around, old man, I am not leaving anything out of my control, I know my stuff. But looking at the state of this I want to ask you this -  do you think we should just give up and find a nice cozy cave to hide in until this all blows over?":
                $ winstonPoints = winstonPoints - 10
                $ prevPoint = False
                hide captain
                show winston at left
                if winstonPoints <= -5:
                    winstonText " <Winston's expression hardens into a mask of cold fury.>"
                    winstonText "Captain, it’s clear you have no grasp of the gravity of our situation or the responsibility on your shoulders. Hiding in a cave? That's your solution?"
                    winstonText "You're unfit to lead if that’s your mindset. I’m done wasting my time with you. Goodbye, and good luck—you’ll need it."
                    "<Winston storms out of the room, slamming the door behind him.>"
                    $ villagePopulation -= 25
                    $ villageResources -= 50
                    "You lost a candidate, 25 people from population, and 50 resources."
                    return
                elif winstonPoints > -5:
                    winstonText "<Winston's face turns red with anger, his eyes narrowing into a fierce glare.>" 
                    winstonText "Captain, your arrogance and dismissive attitude are exactly what's holding us back. Hiding away is not an option and never has been."
                    winstonText "If you think running from our problems will solve anything, you're gravely mistaken. We need leaders who are willing to face challenges head-on, not cowards looking for an easy way out. Get your act together or step aside for someone who will."
    jump Decision    
return

label Decision:
    hide winston
    $ interview  = True
    $ winstinterview = True
    if winstonPoints > 10:
        $ winstonGood = True
        "You successfully convinced this candidate to join you as your advisor and additionally you gain a knowledge if his special ability “Stop the Mutiny”."
        "You can either immediately accept him and proceed with the scenario or conduct interview with another candidates to see if you prefer them better (you do not lose the opportunity to hire Winston)"
        menu:
            "Accept":
                jump winstonchoice
            "Decline":
                jump chooseNPC
    elif winstonPoints>0:
        $ winstonNeutral = True
        "Winston is not entirely convinced if he is willing to follow you as an advisor, but you can assign him with your own decision right away and he will join you (scenario continues). However if you opt to review another candidate you lose the chance to hire Winston."
        menu:
            "Accept":
                jump winstonchoice
            "Decline":
                jump chooseNPC
    else:
        $ winstonBad = True
        "Winston refused to join you. Go for the next candidate."
    jump chooseNPC
return

label winstonchoice:
    "After the interviews, you sit alone in the Command Center, contemplating the strengths and weaknesses of each candidate. The elder offers wisdom and stability but risks being hindered by his grief."
    "The young man brings energy and new ideas but lacks connection with the people. The young woman reflects the community’s voice but could challenge your authority."
    scene winstonchoice_aftermath
    "You decide to choose Winston Steel. You believe that his resilience and depth of experience outweigh the potential for conflict. His challenges will keep you sharp and ensure that every decision is thoroughly considered. As he re-enters the room, you look him in the eyes and say:"
    show captain at right
    captain "Haven's Rest needs someone who understands its heart and soul. I believe that person is you. I trust you to stand by my side, to challenge me when necessary, and to help lead our people to a better future. Will you accept this responsibility?"
    hide captain
    "His facial expression is empty and you can not read his emotions. After a brief moment, he nods resolutely."
    show winston at left
    winstonText "Yes, I will."
    hide winston
    "With your new advisor by your side, you feel a renewed sense of purpose, ready to guide Haven's Rest through the perils of Neo-Terra."
    jump first_task
return

label first_task:
    scene first_task_defences
    "Your early priorities include addressing the emotional and physical wounds left by the recent bandit attack, rallying the settlement to rebuild and fortify their defenses."
    "You must focus on establishing a security committee, enhancing patrols and setting up better warning systems to prevent future attacks. Your leadership style is inclusive, always seeking input from different factions within the settlement, ensuring that everyone feels heard and valued."
    scene first_task_resources
    "In the daily operations of Haven's Rest, you oversee the distribution of resources, ensuring fair and efficient use of supplies. You work closely with the heads of each key building—the Command Center, the Dining Hall, the Hospital, the Greenhouse, the Workshop, the Schoolhouse, and the Water Purification Plant—to coordinate efforts and address any issues promptly."
    "Your strategic mind is focused on long-term sustainability, pushing for advancements in agriculture, water purification, and energy production."
    scene first_task_study
    "Despite the heavy responsibilities, you make it a point to be approachable, often seen walking through the settlement, talking to residents, and addressing their concerns directly."
    "You also prioritize education and training, understanding that knowledge and skills are crucial for the community's resilience and future prosperity. Under your leadership, the morale in Haven's Rest has begun to lift, with people finding renewed purpose and hope."
    "Ultimately, your role is not just to lead but to empower others, fostering a sense of collective responsibility and determination to thrive despite the harsh realities of Neo-Terra."
return

#Main start point of the game
label start:
    call introduction
    #change this scene to interview background 
    scene black
    call chooseNPC
    hide winston with dissolve
    
    "End of demo. Thanks for playing!"
return