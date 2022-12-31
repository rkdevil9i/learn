import random

# n=int(input())
# i=2
# while(i<=n):
#   flag=0
#   for var in range(2,i):
#     if(i%var==0):
#       flag=1
#       break
#   if(flag==0):
#     print(i,end=' ')
#   i=i+1


def super_func(*arg):
  print(arg)
  return sum(arg)


# print(super_func(1,2,3,4))

             
'''----Max even number----'''
def highest_even(li):
  even = []
  for item in li:
    if item % 2 == 0:
      even.append(item)
  return max(even)


# print(highest_even([1,2,3,4,10,20,11]))

  
'''------odd and even number diferenciator------'''
def odd_even():
  tem = [int(item) for item in input("Enter the list numbers : ").split()]
  odd=[]
  even=[]
  for item in tem:
     if item % 2 == 0:
      even.append(item)
     else:
      odd.append(item)
  print(f'odd number:- {odd}')
  print(f'even number:- {even}')
 
# odd_even()

  
 
  

'''For list of integers'''
# lst1 = []

''' For list of strings/chars'''
# lst2 = []

# lst1 = [int(item) for item in input("Enter the list items : ").split()]

# lst2 = [item for item in input("Enter the list items : ").split()]

# print(lst1)
# print(lst2)


'''---take input and convert in list---'''

# item=[]
# item=[int(item) for item in input(' enter number- ').split()]
# print(item)





        
# while True:
#   print('****login****')
#   print(' for start enter:- run \n for stop enter:- exit')
#   d=input(' :-')
#   if d=='run':
#       email=input('enter your email')
#       password=input('enter your password')
#       if '@'in email:
        
#         if email=="rahul356.98@gmail.com"and password=="8140":
#           print('welcome')
#         elif email=="rahul356.98@gmail.com"and password!="8140":
#           print('password incorect')
#           password=input('enter you passwor')
#           if password=="8140":
#             print("finaly correct")
#           else:
#             print("paswword incorrect")
#         else:
#           ('incorrect')
#       else:
#         print('email wrong')
#   else:
#     break
def table():
  while True:
    print('****Table****')
    print(' for start enter:- run \n for stop enter:- exit')
    d=input(' :-')
    if d=='run':
      number= int(input('enter number'))
      i=1
      while i<11:
        print(number*i)
        i+=1
    else:
      break
# table()

def jackpotgame():
  while True:
  
    print('****jackpot game****')
    print(' for start enter:- run \n for stop enter:- exit\n guess number 1 to 100 \n attempt=1 winprice is 10,00,000\n attempt 2 to 5 win price 1,00,000\n attempt 5 to 10 win price 10,000\n attempt>10 win price 0')
    d=input(' :-')
    if d=='run':
      jackpot=random.randint(1,100)
      guess= int(input('chal guess kar'))
      counter=1
      while guess!=jackpot:
        if guess<jackpot:
          print('gusess highr')
        else:
          print ('guess lower')
        guess=int(input('chal guess kar'))
        counter+=1
      if counter==1:
        print('win price 10,00,000')
      elif counter<=5:
        print('win price 1,00,000')
      elif counter<=10:
        print('win price 10,000')
      else:
        print('so many attempt')
      print('your attempt is ',counter)
     
    elif d=='exit':
      break
    else:
      print('pls enter correct comand')
# jackpotgame()
def pattern():
  while True:
    print('****pattern****')
    print(' for start enter:- run \n for stop enter:- exit')
    d=input(' :-')
    if d=='run':
      row= int(input('enter rows'))
      for i in range(1,row+1):
        for j in range(0,i):
          print('*', end=' ')
        print('')
    elif d=='exit':
      break
    else:
      print('pls enter correct comand')
# pattern()
# for i in range(0,1):
#   print('rahul')
#   print(id(i))


      

def word_guess():
  while True:
    print('****H.A.N.G.M.A.N****')
    print(   '    ------------- ')
    print(   '         O_|   ')
    print(   '        /|\    ')
    print(   '        / \    ')
    print(' for start enter:- run \n for stop enter:- exit')
    d=input(' :-')
    if d=='run':
      name= input('what is yor name?:- ')
      print('good luck',name,'and save the kind man')
      
      words=['apple','ball','cat']
      
      word=random.choice(words)
      
      print("Guess the characters")
      guess2=''
      turn = 12

      while turn>0:
        
        faild=0 
      
        for char in word:
          if char in guess2:
            print(char,end=' ')
          else:
            print('_', end =" ")
            faild+=1
        if faild==0:
          print('\nwon')
          print('word is ',word)
          break
          
        guess=input("\nGuess the characters:- ")
        guess2 += guess
        if guess not in word:
          turn -= 1
          print('wrong')
          print('you have',turn,'more guess')
          if turn == 1:
            print(  '--------- bhai acha le ')
            print(  '    O_|   ')
            print(  '   /|\    ')
            print(  '   / \    ')

          if turn == 2:
            print(  '--------- bhai acha le ')
            print(  '    O_|   ')
            print(  '   /|\    ')
            print(  '   / \    ')


          
          if turn == 0:
            print(  '------|--- bhai...... ')
            print(  '    O_|   ')
            print(  '   /|\    ')
            print(  '   / \    ')
            
            print('you let the kind men die')
    elif d=='exit':
      break
    else:
      print('pls enter correct comand')  
word_guess()