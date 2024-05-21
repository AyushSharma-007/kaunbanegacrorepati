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

## print("-----------WELCOME TO THE GAME OF KBC----------")
flag = 1;
variable = 0;
p1 = (input("Enter the players name:"))
print("----------CHALIYIEN SHURU KARTEY HAIN---------")
for i in range(0,len(questions)):
    print()
    print("Question",i+1)
    print(i+1,questions[i])
    print("Options:")
    for j in range(0,4):
            print('\t',j+1,options[i][j])
    right = int(input("Enter the correct options number :\n"))
        # print('i---->', i)
        # print('option i---->', options[i])
    if options[i][right-1] == correct[i]:
            print("Hence your option is correct\n")
    elif i<=4:
        print("Incorrect")
        print("You got 0 rupees")
        break
    elif i>=4 and i<=8:
        print("Incorrect")
        print("You won the cash prize of :", prize[4])
        break
    elif i>=8:
        print("incorrect")
        print("You won the cash prize of :", prize[8])
        break
    else:
        print("Incorrect")
        print("You lose the game , you are getting:",prize[i])
        break
    if i == 4 or i == 8:
        print("You have completed the level and you won the cash prize of:");
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
    print("-------------Hence you won the game -----")
print("-------------AAP GHR LEKE JAA RHE HAI----- ")
print(prize[i])
