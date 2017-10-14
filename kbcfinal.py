#part-1
##Ek question naam ki list banao jisme 5 apni pasand ke questions daalo.

questions=["Q.1 In which date international yoga day is held.",
         "Q.2 How many  times India won the Cricket WorldCup.",
         "Q.3 Who Wrote the National Anthem of India.",
         "Q.4 who was the First Nobel prize winner of India.",
         "Q.5 Who is the CEO of Facebook."]

#part-2
##Saare questions ki pehli option, first_options naam ki list mein daalo.

first_options=["23 march","1 times ","jawaharlal nehru ","Ravindranath tegore","satya nadela "]

##Saare questions ki dusri option, second_options naam ki list mein daalo.

second_options=["21 december ","2 times ","Bankim Chandra Chattopadhyay","Amratya sen","Mark Zuckerberg"]

##Saare questions ki teesri option, third_options naam ki list mein daalo.

third_options=["21 june","3 times","Ravindra nath tegore ","c.v.raman","sundar pichai", ]

##Saare questions ki chauthi option, fourth_options naam ki list mein daalo.

fourth_options=["24jan.","4 times ","bhagat singh","mother teresa","koi nhi"]
#part-3
##Ek LIST banao jiska naam ho all_options jiske ITEMS first_options, second_options, v aur fourth_options wali list ho. Iss list mein dusri lists hongi.

all_options=[first_options,second_options,third_options,fourth_options]

##Part 4

ans_key =['2','1','2','0','1']

#kbc-2

#Part 1
##question_list variable ko use kar ke second question ko use karo.
print question_list[1]

#part-2
##first_options, second_options, third_options, fourth_options ka use kar pehle question ki chaaron options ko print karo.
all_options=[first_options[0],second_options[0],third_options[0],fourth_ options[0]]
print all_options

#part-3
##Ab all_options waali lsit ka use kar ke third question ki saari options ka print karo.
all_options=[first_options[2],second_options[2],third_options[2],fourth_ options[2]]
print all_options

#part-4
##pop function use karke questions_list mein se last question aur chaaron, first_options, second_options, third_options, fourth_options mein se uski saari options ko delete karo.

questions.pop()
print questions
first_options.pop()
second_options.pop()
third_options.pop()
fourth_options.pop()

#part-5
##questions_list ki length print karo
print len(questions)

#part-6
##append function use kar ke questions_list mein ek naya question aur first_options, second_options, third_options, fourth_options mein uski ek ek option add karo.

questions.append('Q.5 What is the new capital of Shri lanka?')
first_options.append('colombo')
second_options.append('Sri Jayawardanapura Kote')
third_options.append('chennai')
fourth_option.append('dhaka')

#part-7
##second_options waali list ke second element ko ek option2 naam ke variable mein store kar ke print karo.
option2=second_options[1]
print option2

#pART-8
##Check karo ki kya option2 variable ki value third_options waali list mein hai ya nahi.

"2 times" in third_options


####kbc-3

#part-1
##Apni questions_list pe iterate kar ke saare questions aur unki corresponding options print karo. Options print karne ke liye aapko first_options, second_options, third_options, fourth_options lists ka use karna padega.

index=0
questions_length=len(questions)
while index<questions_length:
    print questions[index]
    print first_options[index]
    print second_options[index]
    print third_options[index]
    print fourth_options[index]
    index=index+1


#part-2
##Upar Part 1 waale code ko aise modify karo ki aap har question ke liye raw_input use kar ke user se uska answer input lein. User option ka number daalega answer mein. Jaise upar waale question mein Delhi sahi javab hai toh user 0 daalega. Agar Mumbai hota toh 1 daalta, Jaipur hota
index=0
questions_length=len(questions)
while index<questions_length:
    print questions[index]
    print first_options[index]
    print second_options[index]
    print third_options[index]
    print fourth_options[index]
    options=raw_input('input your answer ')
    index=index+1

#Part 3
##Ab ek answers_list naam ka empty list banao aur jab bhi user answer daale to user ke answer ko iss answers_list mein append kar de.

answers_list=[]
answers_list.append(options)

#part-4
##Iterate karte hue jab bhi aap question print karte ho, toh saath saath question ki length bhi print karo len function ka use kar ke. Jaise agar question What is the capital of India hai, toh aapko har question aise print karna hai:

answers_list=[]
   index=0
   questions_length=len(questions)
   while index<questions_length:
       print questions[index],'-',len(questions[index])
       print first_options[index]
       print second_options[index]
       print third_options[index]
       print fourth_options[index]
       options=raw_input('input your answer ')
       answers_list.append(options)
       index=index+1




#Part 1

##Pichle part mein aapne har question aur uske options print karne ka code likha tha. Ab usko modify kar ke aise karo:
#What is the capital of India?
#1. Delhi
#2. Mumbai
#3. Jaipur
#4. Chandigarh

index=0
questions_length=len(questions)
while index<questions_length:
    print questions[index]
    print '1.',first_options[index]
    print '2.',second_options[index]
    print '3.',third_options[index]
    print '4.',fourth_options[index]
    options=raw_input('input your answer ')
    index=index+1

#Part 2

#Pichle part mein aapne user se answer ka input toh le liya tha lekin ab check bhi karna hai ki user ne sahi answer daala hai ya nahi. ans_key waali list ka use kar ke check karo aur agar sahi hai toh print karo "Congrats! Aapka answer sahi hai" nahi toh print karo Sadly aapka javab galat hai.

index=0
answer_key =[3,2,3,1,2]# me answer_key ko 
questions_length=len(questions)
while index<questions_length:
    print questions[index]
    print '1.',first_options[index]
    print '2.',second_options[index]
    print '3.',third_options[index]
    print '4.',fourth_options[index]
    options=int(raw_input('input your answer '))
    if answer_key[index] == options:
        print "congrants! aapka answer sahi h"
    else:
        print "sadly aapka javab galat hai"
    index=index+1

#Part 3
#Ek correct_answers naam ka variable banao aur uski value humesha 1 se increment karo jab bhi user sahi answer deta hai.

correct_answers=0
index=0
answer_key =[3,2,3,1,2]# me answer_key ko phle string me le rha tha isliye mera answer sahi nhi aa rha tha .
questions_length=len(questions)
while index<questions_length:
    print questions[index]
    print '1.',first_options[index]
    print '2.',second_options[index]
    print '3.',third_options[index]
    print '4.',fourth_options[index]
    options=int(raw_input('input your answer '))
    if answer_key[index] == options:
    correct_answers=correct_answers+1
        print "congrants! aapka answer sahi h"

    else:
        print "sadly aapka javab galat hai"
    index=index+1
print"aapke**  ", correct_answers,"  **sahi javab hain."


#*********kbc-final********

#patr-1
#Apni questions_list aur first_options, second_options, third_options, fourth_options ko update karo ki aapke paas 10 questions ho aur saaro ke corresponding questions.
questions=["Q.1 In which date international yoga day is held?",
         "Q.2 How many  times India won the Cricket WorldCup?",
         "Q.3 Who Wrote the National Anthem of India?",
         "Q.4 who was the First Nobel prize winner of India?",
         "Q.5 Who is the CEO of Facebook?",
         "Q.6 who is the present defence minister of india?",
         "Q.7 who known as  the Missile Man ?",
         "Q.8 who is the writer of harrypotter?",
         "Q.9 who is the Richest person in the world?",
         "Q.10 which bird is known as  the national birds of india?"  ]

##Saare questions ki pehli option, first_options naam ki list mein daalo.

first_options=["23 march","1 times ","jawaharlal nehru ","Ravindranath tegore","satya nadela ","narendra modi","mahatma gandhi","H.g wells","mark zuckerberg","peacock"]

##Saare questions ki dusri option, second_options naam ki list mein daalo.

second_options=["21 december ","2 times ","Bankim Chandra Chattopadhyay","Amratya sen","Mark Zuckerberg","shusma swaraj","c.v raman","chetan bhagat","mukesh ambani","sparrow"]

##Saare questions ki teesri option, third_options naam ki list mein daalo.

third_options=["21 june","3 times","Ravindra nath tegore ","c.v.raman","sundar pichai","sitaraman","ramanujan","ramond swift","billgats","duck" ]

##Saare questions ki chauthi option, fourth_options naam ki list mein daalo.

fourth_options=["24jan.","4 times ","bhagat singh","mother teresa","koi nhi","arun jetli","a. p.j abdul kalam","jk rollins","carlos","cock"]

#Part 2
##Ab aap apne KBC game mei har ek question ka alag alag prize rakhoge. Jaise pehle question ke liye ₹1000, doosre question ke liye ₹2000 ...
correct_answers=0
index=0
prize=0
answer_key =[3,2,3,1,2,3,4,4,3,1]
questions_length=len(questions)
while index<questions_length:
    print questions[index]
    print '1.',first_options[index]
    print '2.',second_options[index]
    print '3.',third_options[index]
    print '4.',fourth_options[index]
    options=int(raw_input('input your answer '))
    if answer_key[index] == options:
        correct_answers=correct_answers+1
        prize=prize+1000
        print "congrants! aapka answer sahi h","aap***  ",prize,"Rs  *** prize jeet chuke ho"
    if answer_key[index] != options:  
        print "sadly aapka javab galat hai"
    if index == 3:
        print 'Congrats! aapka phla padav pura ho gya hai.'
    if index == 5: 
        print  "Congrates! aapka dusra padav pura ho gya h."
    if index ==9:
        print "Congrates! your game is over. "  
         
            

    index=index+1
print"aapke**  ", correct_answers,"  **sahi javab hain."

#part-3
##Abhi user galat javab deta hai toh game chalti rehti hai. Lekin humein aisa nahi chaiye. Jaise hi user galat javab de toh game khatam ho jaani chaiye. Yeh karne ke liye break statement ke baare mein padho aur jaise hi user galat javab do toh Aap KBC haar chuke hain print ho jana chaiye.


correct_answers=0
index=0
prize=0
answer_key =[3,2,3,1,2,3,4,4,3,1]
questions_length=len(questions)
while index<questions_length:
    print questions[index]
    print '1.',first_options[index]
    print '2.',second_options[index]
    print '3.',third_options[index]
    print '4.',fourth_options[index]
    options=int(raw_input('input your answer '))
    if answer_key[index] == options:
        correct_answers=correct_answers+1
        prize=prize+1000000
        print "congrants! aapka answer sahi h","aap***  ",prize,"Rs  *** prize jeet chuke ho"
    if answer_key[index] != options:  
        print "sadly aapka javab galat hai"
        print "aap kbc har chuke ho" 
        break
      
    if index == 3:
        print '*****   Congrats! aapka phla padav pura ho gya hai    *****.'
    if index == 5: 
        print  "*****  Congrates! aapka dusra padav pura ho gya h.  *****"
    if index ==9:
        print "Congrates! your game is over. "       

 
    index=index+1
print"aapke**  ", correct_answers,"  **sahi javab hain \n". "Aap***   ",prize,"RS   ***jeet chuke ho!" 


