// lifeline will be added to it
questions = ["What is the capital of Finland?",
             "What is the name of Bridget Jones' baby in the third Bridget Jones film?",
             "Which five colours make up the Olympic rings?",
             "In which decade was Madonna born?",
             "What is the most sold flavour of Walker's crisps?",
             "Grand Central Terminal, Park Avenue, New York is the world's",
            "Entomology is the science that studies",
            "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of",
            "Garampani sanctuary is located at",
             "For which of the following disciplines is Nobel Prize awarded?",         
            "Hitler party which came into power in 1933 is known as?",
             "FFC stands for ?"
            
            ]
options = [['Oulu','Helsinki','Kuopio','Jeonsu'],
           ["William","Armstrong","Stuart","Jinski"],
           ["Black, green, blue, white and red","Blue, green, orange, yellow and safforn","Black, green, blue, yellow and red","Black, grey, blue, yellow and pink"],
           ["The 1940s (1949)","The 1960s (1965)","The 1970s (1978)","The 1950s (1958)"],
           ["Cheese and Onion" ,"Cheese and pasta","tomato and Onion","Cheese and garlic"],
            ["largest railway station","highest railway station","longest railway station","None of the above"],         
          ["Behavior of human beings","Insects","The origin and history of technical and scientific terms","The formation of rocks"],
           ["Asia","Africa","Europe","Australia"],
           ["Junagarh, Gujarat", "Diphu, Assam", "Kohima, Nagaland", "Gangtok, Sikkim"],
           ["Physics and Chemistry","Physiology or Medicine","Literature Peace and Economics","All of the above"],
            ["Labour Party","Nazi Party","Ku-Klux-Klan","Democratic Party"],
           ["Foreign Finance Corporation","Film Finance Corporation","Federation of Football Council","None of the above"]
          ]
correct = ['Helsinki','William','Black, green, blue, yellow and red','The 1950s (1958)','Cheese and Onion','largest railway station','Insects',
            'Africa','Diphu, Assam','Physiology or Medicine','Nazi Party','Film Finance Corporation']

prize = ['0','1000','2000','5000','10000','20000','1000000','200000','500000','1000000','5000000','10000000']
import pyttsx3 
converter = pyttsx3.init()  
converter.setProperty('rate', 125) 
converter.setProperty('volume', 1.0) 
# converter.setProperty('language',hindi) 
converter.say("WELCOME TO THE GAME !!! OF WHO WILL BECOME THE MILLIONAIRE ") 
converter.say("I'M YOUR HOST! THE AI") 



converter.runAndWait() 

voices = converter.getProperty('voices') 
  
for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender:female %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages)
import numpy as np
import pyrebase as pb   
print("-----------SWAGAT HAI AAPKA KAUN BANEGA CROREPATI ME ----------")
flag = 1;
variable = 0;
p1 = (input("MANYAWAR KA NAAM:"))
print("----------CHALIYIEN SHURU KARTEY HAIN---------")
for i in range(0,len(questions)):
    ques = np.random.choice(questions,12,replace = False).tolist()
    print()
    print("Yeh Sawaal ",prize[i],"ruppes ke liye hai")
    print("Question",i+1)
    print(i+1,ques[i])
    tql=ques[i]
    qos=questions.index(tql)
    print("Options:")
    for j in range(0,4):
            print('\t',j+1,options[qos][j])
    right = int(input("Enter the correct options number :\n"))
    if options[qos][right-1] == correct[qos]:
            print("Hence your option is correct\n")
    elif i<=4:
        print("Incorrect")
        print("AAP AAJ GHR LEKE JAA RHE HAI SHUNYA RASHI")
        break
    elif i>=4 and i<=8:
        print("MANYAWAR YEH UTTAR GALAT HAI:")
        print("AAP AAJ GHR LEKE JAA RHE HAI:",prize[4],"RUPPES")
        break
    elif i>=8:
        print("MANYAWAR YEH UTTAR GALAT HAI:")
        print("AAP AAJ GHR LEKE JAA RHE HAI:",prize[8],"RUPPES")
        break
    if i == 4 or i == 8:
        print("AAPNE YEH PADAV PAAR KR LIYA HAI AUR AB AAP GHR LEKE HI JAYENGEY KUCH MULYA KI RASHI:");
        print(prize[i])
    if i<len(questions)-1:
        ask = input("Do You Want to Proceed :Y/N").upper()
        if ask == 'Y':
            flag = 1
        else:
            flag = 0;
            print("Hence you won cash prize if ",prize[i])
            break  
            
if(i==len(questions)):
    print("-------------MANYAWAR AAP JEET GYE HAI POOREY EK CRORE RUPPPES -----")
    print("-------------AAP GHR LEKE JAA RHE HAI----- ")
    print(prize[i])


