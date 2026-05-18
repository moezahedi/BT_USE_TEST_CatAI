init python:
    
    if persistent.progress is None:
        persistent.progress = {
            "suspects": ["Dr. Cassian Block", "Dr. Liam Short", "Allie Berg", "Dr. Beatrice Hellgon", "Dr. Egon Cloud"],
            "clues": [],
            "current_level": 1
        }

define d = Character("CatAI",color="#FFA500", image="cat")
define p = Character("You",color="#5ed41a")
define h = Character("Hint", image="bulb")
define l = Character("Liam Short")
define b = Character("Beatrice Hellgon")

image splash = "splash.png"
label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return

label start:
    play music "audio/veil of secrets.mp3" loop volume 0.4
   
    $ player_name = renpy.input("Enter your name:").strip()
    if not player_name:
        $ player_name = "Detective"  


    scene black
    "Welcome to the game, [player_name]! I hope you will solve the case."
    "Each choice you make will affect the case. If you make the wrong decision, the game stops, and you have to start all over again."
    "Let me introduce you to your partner, CatAI. He is your partner in the murder case of Dr. Sommer and will try to put the pieces of the puzzle together for you."
   
    scene bg hallway
    show dcat
    "Hi, I'm CatAI, and I'm your partner on this case. I can help you in some situations to get us closer to the perpetrator. However, even I can't do everything, and in some places, it's better if you try to solve the mystery without my help."
    "When I heard about the case this morning, I couldn't get over the shock."
    "Dr. Sommer's death is a tragedy. She was a famous researcher in the field of AI and was currently working on Athena, a top-secret AI project that was supposed to push the boundaries of human-AI collaboration."
    "Unfortunately, she didn't finish it before she died. It is now up to us to solve this case. Shall we begin?"

   
    menu:
        "Yes, let’s go to the laboratory.":
            jump scene_of_crime
        "Can you tell me more about Athena?":
            show dcat
            "Athena is a robot that can perform human-like actions, such as reaching for things, nodding, and moving individual joints."
            "Dr. Sommer also wanted to improve the AI in ethical and emotional areas and create a human-like AI that acts ethically on its own. She also wanted to create a seamless collaboration between humans and AI."
            "Let's get started and learn more about the death of Dr. Sommer."
            jump scene_of_crime

label scene_of_crime:
    scene bg crime
    with fade
    "CatAI and you have now arrived at the scene of the crime, in Dr. Sommer's laboratory."
    jump level_1

# Level 1:Fingerprint Analysis
label level_1:
    scene bg finger time clock
    "You and CatAI investigate the laboratory for possible clues that could lead you to Dr. Sommer's murderer. There are several laboratories in the building."
    "In the wing where Dr. Sommer had her laboratory, entry is only possible with a registered fingerprint."
    "You soon realize that a fingerprint analysis is necessary to reduce the number of suspects."
    # show dcat
    d "The lab has hundreds of fingerprints. Analyzing them manually would take days. I can filter the fingerprints in seconds and match them with the lab's credentials. Should I do the fingerprint analysis?"

    scene bg finger
    menu:
        "That's a good idea, please analyze the fingerprints.":
            #show dcat at right
            d cat "Good decision! CatAI is able to process large data sets such as fingerprints quickly."
            d "I have found five fingerprints, which are now the only possible suspects. Only these five people had access to the wing on the day of the murder and were there."
            
            show cb1
            d "1. Dr. Cassian Block - he is the old partner of Dr. Sommer and was excluded from their secret project this year."
            hide cb1
            show ls
            d "2. Dr. Liam Short - he's only been employed by the company for three months and was personally poached by Dr. Sommer from another company."
            hide ls
            show ab
            d "3. Allie Berg - she and Dr. Sommer have been friends for 10 years. Allie only got the job because of her."
            hide ab
            show bh
            d "4. Dr. Beatrice Hellgon - she is also a renowned scientist and is currently working on a secret project."
            hide bh
            show ec
            d "5. Dr. Egon Cloud - he's a scientist and a big fan of Dr. Sommer, which is why he's happy to be doing research so close to her."
            hide ec
            play sound "audio/right.mp3"
            window hide
            $ renpy.pause(1.5)
            "You successfully analyzed the fingerprints and narrowed down the suspects!"
            $ renpy.movie_cutscene("video/level1.webm")
            
            "Well done let‘s move on!"
            window show
            $ renpy.pause(2.0)
            window hide

            $ persistent.progress["clues"].append("fingerprints")
            jump level_2
        "No thank you. I will analyze the fingerprints manually.":
            play sound "audio/gamefail.mp3"
            scene bg over with fade
            "You take too long to analyze the fingerprints manually. In the meantime, the perpetrator has realized their mistake and deleted their fingerprint from the system."
            h "AI organizes data efficiently by recognizing patterns or categories."
            h "In many cases, it is faster and more accurate at analyzing and categorizing data than humans. AI systems are also characterized by the recognition of patterns in large data sets."
            h "You can click the Back Button to change your choice."
            return  # Game over
            

# Level 2: Surveillance Footage
label level_2:
    scene bg crime
    with fade
    d "You now have a list of suspects. The next step is to gather more evidence to narrow it down further."
    scene bg surveillance room
    "You find a surveillance camera that wasn't switched off."
    #show dcat
    d "Should I analyze the footage for you?"
    #hide dcat
    menu:
        "Yes, please analyze the footage.":
            d "Unfortunately, I don't see anyone on the footage. Maybe we should try again?"
            menu:
                "You're right, I'll analyze it manually.":
                    python:
                        already_removed = False
                        if "Allie Berg" in persistent.progress["suspects"]:
                            persistent.progress["suspects"].remove("Allie Berg")
                        else:
                            already_removed = True
                    scene bg monitoring4
                    if already_removed:
                        show ab at left
                        "Well done! You see Allie Berg in a different lab at the time of the murder, confirming she is not a suspect."
                        play sound "audio/right.mp3"
                        $ renpy.movie_cutscene("video/level2.webm")
                    else:
                        "Well done! You see Allie Berg in a different lab at the time of the murder."
                        play sound "audio/right.mp3"
                        $ renpy.movie_cutscene("video/level2.webm")
                    
                    jump level_3
                "Yes, try analyzing again.":
                    scene bg over with fade
                    "Game over! AI missed the suspect due to headgear. A manual evaluation would have been better."
                    play sound "audio/gamefail.mp3"
                    h "Computers represent images as matrices of pixel values, which is much simpler than the way humans perceive visual information."
                    h "AI's understanding of the world is limited by the way the data is represented - it doesn't “see” like humans do." 
                    h "Context and perspective in images often require a deeper understanding, which can be difficult for narrow AI systems."
                    h "You can click the Back Button to change your choice."
                    return
        "No thanks, I'll check the footage myself.":
            python:
                already_removed = False
                if "Allie Berg" in persistent.progress["suspects"]:
                    persistent.progress["suspects"].remove("Allie Berg")
                else:
                    already_removed = True
            scene bg monitoring4
            if already_removed:
                play sound "audio/right.mp3"
                "Well done! You see Allie Berg in a different lab at the time of the murder, confirming she is not a suspect."
                $ renpy.movie_cutscene("video/level2.webm")
            else:
                "Well done! You see Allie Berg in a different lab at the time of the murder."
                play sound "audio/right.mp3"
            
            jump level_3



# Level 3: Voice Recognition
label level_3:
    scene bg recording with fade
    #$ renpy.sound.music.set_volume(1.0)
    play sound "audio/phonecall.mp3"
    "After your success in eliminating another suspect, you set off in search of new clues."
    "In Dr. Sommer's lab, you find a recording device that could possibly reveal clues."
    "You listen to the last recordings of Dr. Sommer."
    scene bg phone with fade
    #$ renpy.sound.music.set_volume(1.0)
    play sound "audio/recording.mp3"
    "Apparently she forgot to turn off the recorder at a certain time on the day she died."
    "You wait and continue listening to the recordings."
    "Suddenly you hear a voice that does not match Dr. Sommer."
    "Moreover, the person does not speak English."
    menu:
        "CatAI, can you please translate the conversation?":
            "CatAI translates the conversation effortlessly in a few seconds."
            "......"
            scene bg recording with fade
            d "The conversation is in Swedish. I'll translate it for you."
            d "\"Hello Cristy! Yes, I'll be at the restaurant at 5:30 pm. No, I haven't forgotten our anniversary! I have to get back to work, but I'll be on my way in a minute\""
            p "Wow, so we can rule out another suspect, right? I mean the person wasn't at the scene at the time of the murder."
            show cb1 at right
            d "Yes that's right. The only suspect who speaks Swedish according to the records is Dr. Cassian Block. So we can cross him off the suspect list."
            hide cb1

            python:
                suspects = persistent.progress["suspects"]
                if "Dr. Cassian Block" in suspects:
                    suspects.remove("Dr. Cassian Block")

            play sound "audio/right.mp3"
            "Good Job!"
            $ renpy.movie_cutscene("video/level3.webm")
            jump level_4
        "I'll try to decode the conversation myself.":
            scene bg over with fade
            "Game over! You couldn't translate the Swedish conversation. You need the help of CatAI." 
            play sound "audio/gamefail.mp3"
            "AI is able to understand voices and the meaning of words in any language and can translate the dialog within a few seconds."
            h "AI excels at identifying patterns in sound, like speech, pitch, and tone, using advanced algorithms." 
            h "Machine learning enables AI to recognize voices, accents, and even emotions in speech by detecting consistent patterns in training data. Sound by converting audio waves into digital signals, such as frequency and amplitude patterns." 
            h "Voice sensors transform speech into a format that AI can process, making it possible to detect patterns and features."
            h "You can click the Back Button to change your choice."
            return



# Level 4: Calculating Angles
label level_4:
    scene bg crime
    d "Great, now we only have three suspects left. Let's look for more clues."
    "You continue to search for clues for three hours, but without success."
    "The perpetrator was thorough and eliminated all other clues. The coroners have now examined Dr. Sommer."
    "And now it's your turn to look at the dead Dr. Sommer."
    "......"
    scene bg gunshot with fade
    d "Maybe we can find more clues by calculating the angle of the gunshot."

    menu:
        "CatAI, can you calculate the angle?":
           
            "CatAI scans the surroundings using sensors and can determine the angle of the shot within a few seconds."
            "Together, you look at the angle of the shot and the suspects."
            "......"
            p "The angle indicates someone who is slightly taller. Isn't Dr. Egon Cloud in a wheelchair?"
            d "Who do you think we can rule out based on this calculation?"
            show ec at right
            p "I think we can cross Dr. Egon Cloud off the list of suspects. According to the calculated angle, he could not have fired the shot from his wheelchair."
            
            # Remove Dr. Egon Cloud from the suspect list
            python:
                suspects = persistent.progress["suspects"]
                if "Dr. Egon Cloud" in suspects:
                    suspects.remove("Dr. Egon Cloud")

            play sound "audio/right.mp3"
            "Well done! Only two suspects remain."
            
            $ renpy.movie_cutscene("video/level4.webm")
            jump level_5  

        "I'll calculate the angle myself.":
            scene bg over with fade 
            play sound "audio/gamefail.mp3"
            "Game over! Due to the fact that you are not really familiar with math and physics, you are not able to solve such a complex formula."
            "AI is able to solve complex tasks within a few seconds and determine the correct launch angle."
            h "AI processes large datasets much faster than humans, enabling it to solve complex calculations quickly." 
            h "Mathematical models and algorithms allow AI to efficiently handle calculations that would take humans much longer." 
            h "In addition to that AI can identify patterns in massive datasets that humans might overlook, which is crucial for solving complex problems."
            h "You can click the Back Button to change your choice."
            return


# Level 5: Interrogation
label level_5:
    scene bg whiteboard with fade
    #show dcat at left
    d "Very good! Things are going really well, there are only two suspects left. It's time for an interrogation."
    d "I've gone through all the clues again and summarized the most important details for the interrogation."
    d "But human interaction and emotional analysis are not my strengths, so you'll have to lead the interrogation."
    
    menu:
        "Let's question Dr. Liam Short first.":
            jump interrogate_liam
        "Let's question Dr. Beatrice Hellgon first.":
            jump interrogate_hellgon

# Interrogating Dr. Liam Short
label interrogate_liam:
    scene bg room with fade
    "Dr. Liam Short looks tense and agitated."
    "Based on the fingerprint, we were able to determine that he was in the same wing as Dr. Sommer on the day of the murder."
    "He had only been with the company for three months and was poached by Dr. Sommer from another company."
    
    menu:
        "What was your relationship with Dr. Sommer like?":
            show ls1
            l "Dr. Sommer was brilliant, but she monitored everything and everyone, which made me very nervous as a new colleague. "
            l "In general, she didn't see that AI should be free from human influence."
            menu:
                "Do you think AI should work without human supervision?":
                    hide ls1
                    show ls2
                    l "Yes, absolutely! AI should not be bound by human fear. It should be different from the Athena project."
                    hide ls2
                    p "Okay, I've heard enough for now. Would you like to question someone else?"
                    menu:
                        "Yes, let's question Dr. Beatrice Hellgon.":
                            jump interrogate_hellgon
                        "No, let's move on and decide who to arrest.":
                            jump arrest_decision

# Interrogating Dr. Beatrice Hellgon
label interrogate_hellgon:
    scene bg room with fade
    d "Dr. Beatrice Hellgon remains calm and composed."
    d "She is a renowned scientist and is currently working on a secret project."
    
    menu:
        "What was your relationship with Dr. Sommer like?":
            show bh
            b "Dr. Sommer was an inspiration to me. We often debated the ethical implications of AI, but it was always respectful. "
            b "I admired her vision for AI and was excited to work with her."
            menu:
                "Did you ever disagree with Dr. Sommer on anything?":
                    b "We disagreed on some aspects of AI development, especially on the integration of AI into human society. "
                    b "But we always found a way to work through our differences."
                    hide bh
                    d "Okay, I've heard enough for now. Would you like to question someone else?"
                    menu:
                        "Yes, let's question Dr. Liam Short.":
                            jump interrogate_liam
                        "No, let's move on and decide who to arrest.":
                            jump arrest_decision

# Arrest Decision
label arrest_decision:
    scene bg hallway with fade
    d "Who do you think committed the murder of Dr. Sommer?"
    menu:
        "Arrest Dr. Liam Short.":
            scene bg handcuff with fade
            play sound "audio/right.mp3"
            d "Good work, [player_name]. After a background check, here's what I found out. Dr. Liam Short murdered Dr. Sommer. It was all premeditated."
            $ renpy.movie_cutscene("video/level5.webm")
            scene bg car with fade
            "The company he was poached from was also behind it."
            "He had himself poached specifically to get more information about 'Athena'."
            "When he had enough information and wanted to prevent Dr. Sommer from developing 'Athena' faster than his old company, to whom he had sold the information, he killed her."
            return  # Game ends with this correct decision

        "Arrest Dr. Beatrice Hellgon.":
            d "Are you sure, [player_name]? The evidence and the statements speak more in favor of Dr. Liam Short. He was much more involved in the company's motives."
            play sound "audio/gamefail.mp3"
            scene bg over with fade
            "Game over! Dr. Beatrice Hellgon is not the murderer. Dr. Liam Short is the true culprit."
            h "AI decisions are based on algorithms and data, not intuition or emotional judgment." 
            h "Ethical decisions often require weighing values beyond logical analysis, which AI cannot do, as ethical decisions often involve complex dilemmas and conflicting values." 
            h "Moral reasoning is a human strength that requires judgment beyond the capabilities of an algorithm. While AI assists humans, its inability to empathize makes emotional intelligence essential in ethical situations. "
            h "You can click the Back Button to change your choice."
            return  # Game ends with the wrong decision

