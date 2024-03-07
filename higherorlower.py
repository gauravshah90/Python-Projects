#link to the flowchart: https://app.diagrams.net/#G1cJ30mSTviDpejXmaGJ1_C_G6f7AW_UC2#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

import random

db = {"Shakira":50,
     "Neymar":60,
     "Rihana": 80,
     "Messi": 120,
     "Amit": 70,
     "Sachin":110}

db_list = ['Shakira', 'Rihana', 'Neymar','Messi', 'Amit', 'Sachin']

shown_list =[]
image_1 = random.choice(db_list)
shown_list.append(image_1)

def image_selection():
  image_2 = random.choice(db_list)
  while image_2 in shown_list:
    image_2 = random.choice(db_list)
  shown_list.append(image_2)
  return(image_2)
  
image_2=image_selection()
correct_answer = True

while correct_answer ==True:
  cnt_list = len(shown_list)-2
  user_input = input(f"Compare A: {image_1} vs Compare B:{image_2}\n Who has more followers? Type 'A' or 'B'")
  
  if (db[image_1]>db[image_2] and user_input == 'A'):
    print(f"Correct! your score is {cnt_list+1}")
    image_2 = image_selection()
  elif (db[image_1]<db[image_2] and user_input == 'B') :
    print(f"Correct! your score is {cnt_list+1}")
    image_1 = image_2
    image_2 = image_selection()
  else:
    print(f"gameover! your score is {cnt_list}")
    correct_answer = False
