# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Voice", kind=nvl, color="#FFFFFF")
define y = Character("You", kind=nvl, color="#BDB5D5")
define s = Character("Sakuya", kind=nvl, color="#770737")
define narrator = nvl_narrator

default hallway = False

# The game starts here.

label start:
    play music "Forever Lost.wav"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    narrator "You woke up. You heard people yelling, but your parents don't argue much. You assume it's people from the outside."

    nvl clear

    v "It’s suffocating, isn’t it?"
    v "You lay in bed, thinking about finally doing it, ending it all. You should."
    v "It won’t be a loss for anyone anyway. But you can’t even do that…"
    v "How pathetic. You should just end your life, loser."

    nvl clear

    narrator "You lay in bed a little longer, even if standing up would distract you from your thoughts. You hear water from the bathroom."
    narrator "You can't move an inch, but it doesn't matter. You wonder when the last time was you had a normal conversation with your parents."
    narrator "You used to talk about so many things with your mother. You used to play volleyball with your dad on the weekends."
    narrator "You get multiple notifications on your phone at the same time, which pulls you out of your thoughts. You shiver. You wonder what that was."

    nvl clear

    y "What..."

    v "That’s weird. You should ignore that. Probably just scam."

    nvl clear

menu phone:

    "check your phone":
        jump check

    "ignore your phone":
        jump ignore


label check:

    narrator "Sakuya sent you a message."

    v "I don’t know why you did that, but Sakuya messaged you."

    nvl clear

    stop music

    play music "Whispering Eyes.wav"

    s "Your parents told me that you are dead. No way, right?"
    s "Answer me, please. They won’t let me check on you and you never answer me."
    s "Please do, if you live. Which you do, right?"
    s "Please. I miss you…"

    v "Oh, look! She pities you. She does her duty as someone that knew you once. She has to check on you. Don’t think she actually cares or misses you."

    nvl clear

    narrator "The messages tug at you. You can't believe that someone cared enough to reach out."

    y "Yeah, she probably doesn't care..."

    nvl clear

menu reply:

    "I am sorry.":
        jump sorry

    "act like parents.":
        jump dead

    "please leave me alone.":
        jump alone

    "let's talk.":
        jump talk

    "don't reply":
        jump ignore

label sorry:

    y "I am sorry, Sakuya-chan. I don't know what to say to you."

    s "Please just... I don't know. Can we talk? In person, I mean."

    y "I don't know if I can do that."

    jump leave

label dead:

    y "This is Takada-san. Stop messaging him. We are grieving."

    s "You are lying... You can't not be lying, right? Why would you say that?"
    s "Do you hate me?"
    s "Sorry, I shouldn't say that..."
    s "You probably feel terrible enough..."

    jump leave

label alone:

    y "Please, Sakuya-chan. Leave me alone."

    s "What?"
    s "Why would I do that?"
    s "I understand that you are going through something."
    s "I want to be there for you."
    s "Let's just talk in person, okay? I will go to your window!"

    jump leave

label talk:

    y "Are you still here? Come to my window, Sakuya-chan. Let's talk."

    jump leave

label ignore:

    y "It won’t be important anyway. Who would want to tell me anything?"

    v "That’s precisely it! Everyone forgot about you already. I bet it was a notification from one of your bajillion apps."

    narrator "you lay in bed. you stare at the wall. you stare at the ceiling."

    v "You’re doing so much already! You don’t need to leave your room if you’re being productive. Your parents will argue with you again."

    nvl clear

    "Do you leave your room?"

menu leave:

    "leave your room":
        jump hallway

    "don't leave your room":
        jump room


label hallway:
    $ hallway = True

    nvl clear

    v "Why would you that? Are you insane? Go back to your room immediately."

    nvl clear

menu returnroom:
    "Do you return to your room?"

    "return to your room":
        jump room

    "stay here":
        jump ways

menu ways:
    narrator "It sounds like your dad is cooking in the kitchen. Your mom is probably taking a bath. You're hungry and need to pee. Where do you go?"

    "go to the bathroom":
        jump bathroom

    "go to the living room":
        jump livingroom

    "go to the kitchen":
        jump kitchen

label room:
    if hallway:
        narrator "You returned to your room. It's colder than out in the hallway."

    if not hallway:
        narrator "Your room is as cold as ever."

menu window:

    narrator "You hear something on your window. Do you want to check your window?"

    "go to your window":
        jump sakuya

    "lay in bed":
        jump bed

    "stare at your window from afar":
        jump far

label sakuya:

    narrator "You go to your window. Sakuya-chan stares at you in disbelieve as you appear in front of her, opening the window."

    s "How could you do that to me? I missed you. We were... we were so close, yet you never once replied."
    s "I do understand though. You don't have to explain. Those things happen. Life is hard."

    y "You don't... actually care, do you?"

    s "Of course I do! We're friends. We're supposed to be there for each other, right?"

label bed:

    narrator "You lay into your bed, still hearing somebody knocking at your window. You know who it is, but you can't face Sakuya-chan anymore."

label far:

    narrator "You stare at your window. You see a familiar face you haven't seen in a while looking inside. Sakuya-chan wants to talk with you, but you just stare at her."

label bathroom:

    narrator "it's locked. You don't want to enter anyway because you hear the water running."

    v "That was kinda weird. Are you deaf? You clearly heard the water, didn't you? What a creep. You should really just stop existing."

    nvl clear

    jump ways

label livingroom:

    "livingroom test"

    nvl clear

label kitchen:

    "kitchen test"

    nvl clear

    # This ends the game.

    return
