import turtle
import random
import time
import os
from PIL import Image


#Deborah
dough_options = ['Thin crust','Thick Crust']
pizza_toppings = ["Pepperoni", "Pineapple","Green Peppers", "Mushroom", "Olives", "Cheese"]
cheese = ['Mozzarella', 'Cheddar','Parmesan']


#Davina
screen = turtle.Screen()
screen.title('PYTHON PIZZERIA')


img = Image.open('start.gif')
resizedimg = img.resize((250,100))
resizedimg.save('start_new.gif')


userimg = Image.open('startgame.gif')
reuserimg = userimg.resize((1400,800))
reuserimg.save('startgame.gif')


orderimg = Image.open('order.gif')
reorderimg = orderimg.resize((250,100))
reorderimg.save('order_button.gif')


startimg = Image.open('startorder.gif')
restartimg = startimg.resize((250,100))
restartimg.save('start_order.gif')


topimg = Image.open('toppingsbutton.gif')
resizetop = topimg.resize((250,100))
resizetop.save('toppings_button.gif')


mush = Image.open('mushroom2.gif')
mushroom = mush.resize((100,100))
mushroom.save('mushroom_topping.gif')


oli = Image.open('olives.gif')
olive = oli.resize((100,100))
olive.save('olive.gif')


grp = Image.open('greenpep.gif')
greenp = grp.resize((100,100))
greenp.save('green_pep.gif')


pineapp = Image.open('pineapple.gif')
pineapple = pineapp.resize((100,100))
pineapple.save('pineapples.gif')


pepp = Image.open('pepperoni1.gif')
pepperonis = pepp.resize((100,100))
pepperonis.save('pepperoni.gif')


che = Image.open('cheese.gif')
chh = che.resize((100,100))
chh.save('cheese1.gif')


play = Image.open('playagain.gif')
plays = play.resize((250,100))
plays.save('playagain.gif')


pick = Image.open('pickup.gif')
pickup = pick.resize((250,100))
pickup.save('pickup1.gif')


fi = Image.open('final_order.gif')
fif = fi.resize((350,100))
fif.save('final_order.gif')


topp = Image.open('selecttop.gif')
tops = topp.resize((450,100))
tops.save('selecttop.gif')


t = turtle.Turtle()
start = turtle.Turtle()
order_button = turtle.Turtle()
startorder = turtle.Turtle()
top = turtle.Turtle()
mushrooms = turtle.Turtle()
olv = turtle.Turtle()
green_p = turtle.Turtle()
pine = turtle.Turtle()
pep = turtle.Turtle()
ch = turtle.Turtle()
fire = turtle.Turtle()
play = turtle.Turtle()
pickup = turtle.Turtle()
finalorder = turtle.Turtle()
to = turtle.Turtle()


fireworks = turtle.Turtle()
fireworks.hideturtle()
fireworks.speed(0)
fireworks.penup()


t.hideturtle()
t.speed(10)
start.hideturtle()
fire.speed(0)
fire.hideturtle()


#Deborah
topping_objects = {}
correct_dough = None
correct_toppings = None
correct_cheese = None




screen = turtle.Screen()
screen.setup(width = 1200, height = 600)
screen.title('WELCOME TO PYTHON PIZZERIA')
screen.bgpic('start_game.gif')


#Zoya
def generate_random_order():
   global correct_dough, correct_toppings,correct_cheese
   dough_options = ['Thin crust','Thick Crust']
   pizza_toppings = ["Pepperoni", "Pineapple","Green Peppers", "Mushroom", "Olives", "Cheese"]
   cheese = ['Mozarella', 'Cheddar','Parmesan']
   dough = random.choice(dough_options)
   toppings = random.sample(pizza_toppings,2)
   cheese_type = random.choice(cheese)
   if dough_options is not None :
       print(f'The order is: {dough}, Cheese: {cheese_type}, Toppings: {toppings}')
   t.clear()
   t.goto(0,200)
   # t.clear()
   toppings_str = ", ".join(toppings)
   if toppings is not None:
       order = (f' The order is :{dough} Cheese: {cheese_type},Toppings: {toppings_str}')
   #t.write(order, align= 'center', font =("Georgia", 16, "normal"))


   # return dough,cheese,toppings
   #box behind the text
   width = 900
   height = 90
   t.penup()
   t.goto(-width // 2, -200)
   t.pendown()
   t.begin_fill()
   for i in range(2):
       t.color('white')
       t.forward(width)
       t.left(90)
       t.forward(height)
       t.left(90)
   t.end_fill()
   t.penup()
   t.goto(0, -200 + height //2)
   t.color('black')
   t.write(order, align= 'center', font =("Georgia", 18, "normal"))
   # return dough,cheese_type,toppings


#Davina   
def create_start_button(): #Start button
   start.penup()
   turtle.addshape('start_new.gif')
   start.shape('start_new.gif')
   start.goto(-50,50)
   start.showturtle()


def start_order_button(): #Order button
   startorder.penup()
   turtle.addshape('start_order.gif')
   startorder.shape('start_order.gif')
   startorder.goto(-50,-250)
   startorder.showturtle()
   startorder.onclick(order_screen)
  
def toppings_button(): #Toppings button
   top.penup()
   turtle.addshape('toppings_button.gif')
   top.shape('toppings_button.gif')
   top.goto(-50,-300)
   top.showturtle()
   top.onclick(toppings_screen)


def create_order_button():
   order_button.penup()
   turtle.addshape('order_button.gif')
   order_button.shape('order_button.gif')
   order_button.goto(-50,50)
   order_button.showturtle()
   order_button.onclick(order_button_click)


def pickup_button():
   pickup.penup()
   turtle.addshape('pickup1.gif')
   pickup.shape('pickup1.gif')
   pickup.goto(-50,-300)
   pickup.showturtle()




def mushroom():
   mushrooms.penup()
   turtle.addshape('mushroom_topping.gif')
   mushrooms.shape('mushroom_topping.gif')
   mushrooms.goto(-50,50)
   mushrooms.showturtle()
   mushrooms.onclick(final_screen)


def olives():
   olv.penup()
   turtle.addshape('olive.gif')
   olv.shape('olive.gif')
   olv.goto(-150,50)
   olv.showturtle()
   olv.onclick(final_screen)


def green_pepperoni():
   green_p.penup()
   turtle.addshape('green_pep.gif')
   green_p.shape('green_pep.gif')
   green_p.goto(-250,50)
   green_p.showturtle()
   green_p.onclick(final_screen)


def pineapple():
   pine.penup()
   turtle.addshape('pineapples.gif')
   pine.shape('pineapples.gif')
   pine.goto(50,50)
   pine.showturtle()
   pine.onclick(final_screen)


def pepperoni():
   pep.penup()
   turtle.addshape('pepperoni.gif')
   pep.shape('pepperoni.gif')
   pep.goto(150,50)
   pep.showturtle()
   pep.onclick(final_screen)


def cheese():
   ch.penup()
   turtle.addshape('cheese1.gif')
   ch.shape('cheese1.gif')
   ch.goto(250,50)
   ch.showturtle()
   ch.onclick(final_screen)


def select_toppings():
   to.penup()
   turtle.addshape('selecttop.gif')
   to.shape('selecttop.gif')
   to.goto(-50,300)
   to.showturtle()


def fireworks(x,y):
   fire.penup()
   fire.goto(x,y)
   fire.pendown()
   fire.color(color)
   for i in range(36):
       fire.forward(50)
       fire.backward(50)
       fire.left(10)


  
#Zoya/Davina
def order_button_click(x,y):
   generate_random_order()


def select_dough(x,y):
   #this is a placeholder
   print("Dough selected")


def select_topping(x,y):
   #this is a placeholder
   print("Topping selected")


def start_order_and_generate():
   order_screen(x,y)
   generate_random_order()


def display_order():
   global correct_dough, correct_cheese, correct_topping
   if correct_dough is not None:
       correct_dough, correct_cheese, correct_toppings = generate_random_order()
   t.goto(0,200)
   t.clear()
   t.write(f"Order: {correct_dough}\nCheese: {correct_cheese}\nToppings: {correct_toppings}", align = 'center', font = ("Georgia", 16, "normal"))




#Zoya
#Dough options screen
img = Image.open('classiccrust.gif')
resizedimg = img.resize((200,200))
resizedimg.save('classiccrust.gif')


img = Image.open('thin.gif')
resizedimg = img.resize((200,200))
resizedimg.save('thin.gif')


img = Image.open('deep.gif')
resizedimg = img.resize((200,200))
resizedimg.save('deep.gif')


def classic_crust():
   classic = turtle.Turtle()
   classic.penup()
   turtle.addshape('classiccrust.gif')
   classic.shape('classiccrust.gif')
   classic.goto(-195,140)
   classic.showturtle()
   classic.onclick(toppings_screen)


def thin_crust():
   thin = turtle.Turtle()
   thin.penup()
   turtle.addshape('thin.gif')
   thin.shape('thin.gif')
   thin.goto(15,140)
   thin.showturtle()
   thin.onclick(toppings_screen)


def deep_crust():
   deep = turtle.Turtle()
   deep.penup()
   turtle.addshape('deep.gif')
   deep.shape('deep.gif')
   deep.goto(230,140)
   deep.showturtle()
   deep.onclick(toppings_screen)


#Davina
def start_game(x,y): #Start Screen 1
   screen.clear()
   screen.bgpic('start_game.gif')
   create_order_button()
   start_order_button()
   display_order()


def order_screen(x,y): #Order Screen 2
   screen.clear()
   screen.bgpic('lvl1.gif')
   classic_crust()
   toppings_button()
   deep_crust()
   thin_crust()
   top.onclick(toppings_screen) 


def toppings_screen(x,y): #Toppings Screen 3
   screen.clear()
   screen.bgpic('toppingscreen.gif')
   olives()
   mushroom()
   green_pepperoni()
   pineapple()
   pepperoni()
   cheese()
   select_toppings()
  
def play_again_button():
   play.penup()
   turtle.addshape('playagain.gif')
   play.shape('playagain.gif')
   play.goto(-50,350)
   play.showturtle()
   play.onclick(order_screen)


def final_order():
   finalorder.penup()
   turtle.addshape('final_order.gif')
   finalorder.shape('final_order.gif')
   finalorder.goto(-50,350)
   finalorder.showturtle()


def starts_game(x,y):
   screen.clear()
   screen.bgpic('start_game.gif')
   play_again_button
   create_order_button()
   start_order_button()
   display_order()


def fireworks(x,y,color):
   fire.penup()
   fire.goto(x,y)
   fire.color(color)
   for i in range(30):
       fire.forward(random.randint(50,100))
       fire.backward(random.randint(50,100))
       fire.left


def final_screen(x,y):
   screen.clear()
   screen.bgpic('final_screen.gif')
   play_again_button()
   pickup_button()
   final_order()
   for i in range(10):
       x = random.randint(-300,300)
       y = random.randint(100,300)
       color = random.choice(['red','orange','yellow','blue','green','purple','white'])
       fire.penup()
       fire.goto(x,y)
       fire.pendown()
       fire.color(color)
       fire.circle(5)
       fire.fireworks(x,y,color)
       fire.sleep(0.5)
   fire.done()


create_start_button()
start.onclick(start_game)
screen.mainloop()
import turtle
import random
import time
import os
from PIL import Image


#Deborah
dough_options = ['Thin crust','Thick Crust']
pizza_toppings = ["Pepperoni", "Pineapple","Green Peppers", "Mushroom", "Olives", "Cheese"]
cheese = ['Mozzarella', 'Cheddar','Parmesan']


#Davina
screen = turtle.Screen()
screen.title('PYTHON PIZZERIA')


img = Image.open('start.gif')
resizedimg = img.resize((250,100))
resizedimg.save('start_new.gif')


userimg = Image.open('startgame.gif')
reuserimg = userimg.resize((1400,800))
reuserimg.save('startgame.gif')


orderimg = Image.open('order.gif')
reorderimg = orderimg.resize((250,100))
reorderimg.save('order_button.gif')


startimg = Image.open('startorder.gif')
restartimg = startimg.resize((250,100))
restartimg.save('start_order.gif')


topimg = Image.open('toppingsbutton.gif')
resizetop = topimg.resize((250,100))
resizetop.save('toppings_button.gif')


mush = Image.open('mushroom2.gif')
mushroom = mush.resize((100,100))
mushroom.save('mushroom_topping.gif')


oli = Image.open('olives.gif')
olive = oli.resize((100,100))
olive.save('olive.gif')


grp = Image.open('greenpep.gif')
greenp = grp.resize((100,100))
greenp.save('green_pep.gif')


pineapp = Image.open('pineapple.gif')
pineapple = pineapp.resize((100,100))
pineapple.save('pineapples.gif')


pepp = Image.open('pepperoni1.gif')
pepperonis = pepp.resize((100,100))
pepperonis.save('pepperoni.gif')


che = Image.open('cheese.gif')
chh = che.resize((100,100))
chh.save('cheese1.gif')


play = Image.open('playagain.gif')
plays = play.resize((250,100))
plays.save('playagain.gif')


pick = Image.open('pickup.gif')
pickup = pick.resize((250,100))
pickup.save('pickup1.gif')


fi = Image.open('final_order.gif')
fif = fi.resize((350,100))
fif.save('final_order.gif')


topp = Image.open('selecttop.gif')
tops = topp.resize((450,100))
tops.save('selecttop.gif')


t = turtle.Turtle()
start = turtle.Turtle()
order_button = turtle.Turtle()
startorder = turtle.Turtle()
top = turtle.Turtle()
mushrooms = turtle.Turtle()
olv = turtle.Turtle()
green_p = turtle.Turtle()
pine = turtle.Turtle()
pep = turtle.Turtle()
ch = turtle.Turtle()
fire = turtle.Turtle()
play = turtle.Turtle()
pickup = turtle.Turtle()
finalorder = turtle.Turtle()
to = turtle.Turtle()


fireworks = turtle.Turtle()
fireworks.hideturtle()
fireworks.speed(0)
fireworks.penup()


t.hideturtle()
t.speed(10)
start.hideturtle()
fire.speed(0)
fire.hideturtle()


#Deborah
topping_objects = {}
correct_dough = None
correct_toppings = None
correct_cheese = None




screen = turtle.Screen()
screen.setup(width = 1200, height = 600)
screen.title('WELCOME TO PYTHON PIZZERIA')
screen.bgpic('start_game.gif')


#Zoya
def generate_random_order():
   global correct_dough, correct_toppings,correct_cheese
   dough_options = ['Thin crust','Thick Crust']
   pizza_toppings = ["Pepperoni", "Pineapple","Green Peppers", "Mushroom", "Olives", "Cheese"]
   cheese = ['Mozarella', 'Cheddar','Parmesan']
   dough = random.choice(dough_options)
   toppings = random.sample(pizza_toppings,2)
   cheese_type = random.choice(cheese)
   if dough_options is not None :
       print(f'The order is: {dough}, Cheese: {cheese_type}, Toppings: {toppings}')
   t.clear()
   t.goto(0,200)
   # t.clear()
   toppings_str = ", ".join(toppings)
   if toppings is not None:
       order = (f' The order is :{dough} Cheese: {cheese_type},Toppings: {toppings_str}')
   #t.write(order, align= 'center', font =("Georgia", 16, "normal"))


   # return dough,cheese,toppings
   #box behind the text
   width = 900
   height = 90
   t.penup()
   t.goto(-width // 2, -200)
   t.pendown()
   t.begin_fill()
   for i in range(2):
       t.color('white')
       t.forward(width)
       t.left(90)
       t.forward(height)
       t.left(90)
   t.end_fill()
   t.penup()
   t.goto(0, -200 + height //2)
   t.color('black')
   t.write(order, align= 'center', font =("Georgia", 18, "normal"))
   # return dough,cheese_type,toppings


#Davina   
def create_start_button(): #Start button
   start.penup()
   turtle.addshape('start_new.gif')
   start.shape('start_new.gif')
   start.goto(-50,50)
   start.showturtle()


def start_order_button(): #Order button
   startorder.penup()
   turtle.addshape('start_order.gif')
   startorder.shape('start_order.gif')
   startorder.goto(-50,-250)
   startorder.showturtle()
   startorder.onclick(order_screen)
  
def toppings_button(): #Toppings button
   top.penup()
   turtle.addshape('toppings_button.gif')
   top.shape('toppings_button.gif')
   top.goto(-50,-300)
   top.showturtle()
   top.onclick(toppings_screen)


def create_order_button():
   order_button.penup()
   turtle.addshape('order_button.gif')
   order_button.shape('order_button.gif')
   order_button.goto(-50,50)
   order_button.showturtle()
   order_button.onclick(order_button_click)


def pickup_button():
   pickup.penup()
   turtle.addshape('pickup1.gif')
   pickup.shape('pickup1.gif')
   pickup.goto(-50,-300)
   pickup.showturtle()




def mushroom():
   mushrooms.penup()
   turtle.addshape('mushroom_topping.gif')
   mushrooms.shape('mushroom_topping.gif')
   mushrooms.goto(-50,50)
   mushrooms.showturtle()
   mushrooms.onclick(final_screen)


def olives():
   olv.penup()
   turtle.addshape('olive.gif')
   olv.shape('olive.gif')
   olv.goto(-150,50)
   olv.showturtle()
   olv.onclick(final_screen)


def green_pepperoni():
   green_p.penup()
   turtle.addshape('green_pep.gif')
   green_p.shape('green_pep.gif')
   green_p.goto(-250,50)
   green_p.showturtle()
   green_p.onclick(final_screen)


def pineapple():
   pine.penup()
   turtle.addshape('pineapples.gif')
   pine.shape('pineapples.gif')
   pine.goto(50,50)
   pine.showturtle()
   pine.onclick(final_screen)


def pepperoni():
   pep.penup()
   turtle.addshape('pepperoni.gif')
   pep.shape('pepperoni.gif')
   pep.goto(150,50)
   pep.showturtle()
   pep.onclick(final_screen)


def cheese():
   ch.penup()
   turtle.addshape('cheese1.gif')
   ch.shape('cheese1.gif')
   ch.goto(250,50)
   ch.showturtle()
   ch.onclick(final_screen)


def select_toppings():
   to.penup()
   turtle.addshape('selecttop.gif')
   to.shape('selecttop.gif')
   to.goto(-50,300)
   to.showturtle()


def fireworks(x,y):
   fire.penup()
   fire.goto(x,y)
   fire.pendown()
   fire.color(color)
   for i in range(36):
       fire.forward(50)
       fire.backward(50)
       fire.left(10)


  
#Zoya/Davina
def order_button_click(x,y):
   generate_random_order()


def select_dough(x,y):
   #this is a placeholder
   print("Dough selected")


def select_topping(x,y):
   #this is a placeholder
   print("Topping selected")


def start_order_and_generate():
   order_screen(x,y)
   generate_random_order()


def display_order():
   global correct_dough, correct_cheese, correct_topping
   if correct_dough is not None:
       correct_dough, correct_cheese, correct_toppings = generate_random_order()
   t.goto(0,200)
   t.clear()
   t.write(f"Order: {correct_dough}\nCheese: {correct_cheese}\nToppings: {correct_toppings}", align = 'center', font = ("Georgia", 16, "normal"))




#Zoya
#Dough options screen
img = Image.open('classiccrust.gif')
resizedimg = img.resize((200,200))
resizedimg.save('classiccrust.gif')


img = Image.open('thin.gif')
resizedimg = img.resize((200,200))
resizedimg.save('thin.gif')


img = Image.open('deep.gif')
resizedimg = img.resize((200,200))
resizedimg.save('deep.gif')


def classic_crust():
   classic = turtle.Turtle()
   classic.penup()
   turtle.addshape('classiccrust.gif')
   classic.shape('classiccrust.gif')
   classic.goto(-195,140)
   classic.showturtle()
   classic.onclick(toppings_screen)


def thin_crust():
   thin = turtle.Turtle()
   thin.penup()
   turtle.addshape('thin.gif')
   thin.shape('thin.gif')
   thin.goto(15,140)
   thin.showturtle()
   thin.onclick(toppings_screen)


def deep_crust():
   deep = turtle.Turtle()
   deep.penup()
   turtle.addshape('deep.gif')
   deep.shape('deep.gif')
   deep.goto(230,140)
   deep.showturtle()
   deep.onclick(toppings_screen)


#Davina
def start_game(x,y): #Start Screen 1
   screen.clear()
   screen.bgpic('start_game.gif')
   create_order_button()
   start_order_button()
   display_order()


def order_screen(x,y): #Order Screen 2
   screen.clear()
   screen.bgpic('lvl1.gif')
   classic_crust()
   toppings_button()
   deep_crust()
   thin_crust()
   top.onclick(toppings_screen) 


def toppings_screen(x,y): #Toppings Screen 3
   screen.clear()
   screen.bgpic('toppingscreen.gif')
   olives()
   mushroom()
   green_pepperoni()
   pineapple()
   pepperoni()
   cheese()
   select_toppings()
  
def play_again_button():
   play.penup()
   turtle.addshape('playagain.gif')
   play.shape('playagain.gif')
   play.goto(-50,350)
   play.showturtle()
   play.onclick(order_screen)


def final_order():
   finalorder.penup()
   turtle.addshape('final_order.gif')
   finalorder.shape('final_order.gif')
   finalorder.goto(-50,350)
   finalorder.showturtle()


def starts_game(x,y):
   screen.clear()
   screen.bgpic('start_game.gif')
   play_again_button
   create_order_button()
   start_order_button()
   display_order()


def fireworks(x,y,color):
   fire.penup()
   fire.goto(x,y)
   fire.color(color)
   for i in range(30):
       fire.forward(random.randint(50,100))
       fire.backward(random.randint(50,100))
       fire.left


def final_screen(x,y):
   screen.clear()
   screen.bgpic('final_screen.gif')
   play_again_button()
   pickup_button()
   final_order()
   for i in range(10):
       x = random.randint(-300,300)
       y = random.randint(100,300)
       color = random.choice(['red','orange','yellow','blue','green','purple','white'])
       fire.penup()
       fire.goto(x,y)
       fire.pendown()
       fire.color(color)
       fire.circle(5)
       fire.fireworks(x,y,color)
       fire.sleep(0.5)
   fire.done()


create_start_button()
start.onclick(start_game)
screen.mainloop()
