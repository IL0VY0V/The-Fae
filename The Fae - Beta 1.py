import time
import sys
import os
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.075)
def print_slower(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.25)
print_slow('\033[1;33;40m Hello and welcome to The Fae - Beta One. If you played the demo, then this will continue that story, as well as contain more information and choices. \n')
print_slow('I understand that this code currently looks messy. I learned the print command in class and then bridged from it. Most of this I copied online. \n')
print_slow('Write a random input to continue. \n')
x = input()
os.system('cls' if os.name == 'nt' else 'clear')
print_slow("\033[1;31;40m You are wandering through a thick, misty forest. It is cold, and in the distance you hear the faint hissing of a local legend. \n")
print_slow("The trees copy, distorting your sense of directions. You realize you are lost. Do you go forward, left or right? \n")
voroodi = input('\033[1;34;40m Left, Right or Forward: ')
if voroodi == 'Left' or voroodi == 'left':
    time.sleep(0.15)
    print_slow('\033[1;31;40m You went left. The darkness sinks and the moon howls with a shiny glow. \n')
    print_slow("You know you are getting closer. You can feel it. Feel his presence. \n")
elif voroodi == 'Right' or voroodi == 'right':
    time.sleep(0.015)
    print_slow('\033[1;31;40m You went right. The mist gets thicker, collapsing your lungs. \n')
    print_slow("\033[1;31;40m You know you are getting closer. You can feel it. Feel his presence. Deep within your bones.\n ")
elif voroodi == 'Forward' or voroodi == 'forward' or voroodi == 'fwd':
    print_slow('\033[1;31;40m You went forward. You see faint shadows dance around your ill gaze. \n')
    print_slow('Trees continue to blur your view. Were you here already? \n')
    print_slow('However, you know you are getting closer. You can feel it. Feel him. Feel his eyes against your skin. \n')
print_slow("You hear his laughter louder and louder. He's everywhere. \n")
print_slower("\033[1;35;40m Suddenly... ")
time.sleep(0.15)
print_slow("\033[1;34;40m Everything went quiet. Should you say something? \n")
voroodi = input('\033[1;34;40m Yes or No: ')
if voroodi == 'Yes' or voroodi == 'yes':
    time.sleep(0.15)
    print_slow('\033[1;31;40m You speak the damnest words. \033[1;36;40m "I came for my mother! She is deathly ill." \n')
    print_slow("\033[1;31;40m The mist clouds your vision. You hear a deep, raspy voice echo in the cold wind. \n")
    time.sleep(0.50)
    print_slow('\033[1;32;40m "I can sense you are scared, little bunny. But you come with good intentions. \n')
    print_slow('\033[1;31;40m You wonder if he is trying to sound ghastly or calming. You cannot tell; his voice is emotionless, but not monotone. \n')
    print_slow('\033[1;32;40m "Yeah? And what is in it for me?" \n')
    voroodi = input('\033[1;34;40m Offer your soul (1) or Offer your life (2): ')
    if voroodi == '1':
        time.sleep(0.15)
        print_slow('\033[1;36;40m "I will give you...my soul. You can feed off my life force, grow stronger." \n ')
        print_slower('\033[1;36;40m "Anything for my mother..." \n ')
        time.sleep(0.50)
        print_slow('\033[1;32;40m "Do not make such foolish statements. A mortal''s soul is worthless to kind such as myself." \n ')
        print_slow("\033[1;31;40m To Be Contiuned... \n")
    if voroodi == '2':
        time.sleep(0.15)
        print_slow('\033[1;36;40m "I offer my life." \n ')
        time.sleep(0.50)
        print_slow('\033[1;32;40m "Do not make such foolish statements. What would I do with such a pure mortal?" \n ')
        print_slow("\033[1;31;40m To Be Contiuned... \n")
elif voroodi == 'No' or voroodi == 'no':
    time.sleep(0.15)
    print_slow("\033[1;31;40m You stay slient. Your thoughts echo through your mind as a haunting whisper plagues your ears. \n ")
    print_slow("\033[1;31;40m Your silence upsets the Fae. \n ")
    print_slow("Feeling the air getting thicker, you run, as far as you can go.\n ")
    print("You got the Coward Ending! \n")
print("More coming soon! \n")
z=input("press enter to exit")