#cli game Gladiator Ark made by lavadamage
#more comments will be added to the code

import subprocess
import random
from termcolor import colored

#function to clear the terminal and refresh
def clear():
	subprocess.run(["clear"])
	print('Gladiator Ark')
	print('')
	print('')

def prnt(cn, health, bsp, eh, ssp, ed, d1, d2, d3, d4, c, coins, c1, c2, c3, c4):
	clear()
	print("Cave", cn)
	print("")
	print("Your health:", health, bsp, "Enemy health:",eh)
	print("")
	print(".---------------------------.")
	print("| Abilities | Damage | Cost |", ssp, "Enemy Damage:", ed)
	print("|     -     |   -    | In   |")
	print("| Spels     | Heal   | Coins|")
	print(".---------------------------.")
	
	if c1 >= 10:
		print("|   Roar    |", d1, "    |", c1, "  |")
	else:
		print("|   Roar    |", d1, "    |", c1, "   |")

	print("|   Flash   |", d2, "    |", c2, "  |")
	
	if c3 >= 10:
		print("|   Heal    |", d3, "    |", c3, "  |")
	else:
		print("|   Heal    |", d3, "    |", c3, "   |")
		
	print("|   Dodge   |", d4, "     |", c4, "  |")
	print(".---------------------------.")
	print("")
	print(c, coins)
	print("")
	print("Use ability 1, 2, 3 or 4.")
	print("")
	print("")

clear()

print('Hello player!')
print('')
print('1) Play')
print('2) View seed stats')
print('3) About')
print('')
print('Press ENTER to exit.')
print('')

ch = input('Select: ')

if ch == '1':
	clear()
	print("Welcome to Gladiator Ark...")
	print("")
	print("Good luck surviving!")
	print("")
	print("")

	usr = input("Your name: ")

	print("")
	temp = input("Press ENTER to continue... ")

	health = 300
	coins = random.randint(80,151)
	cn = 0
	td = 0
	tc = 0

	bsp = "                  "
	ssp = "     "

	sc = random.randint(20,51)

	while health > 0:
	    eh = random.randint(50,101)
	    ed = random.randint(5,26)
	    s1 = random.randint(10,21)
	    s2 = random.randint(15,26)
	    s3 = random.randint(10,21)
    
	    d1 = colored(s1, 'red')
	    d2 = colored(s2, 'red')
	    d3 = colored(s3, 'green')
	    d4 = colored('0', 'green')
 	   
	    c = colored('Coins:', 'yellow')
    
	    c1 = random.randint(8,13)
	    c2 = random.randint(15,26)
    
	    ch = 1
    
	    if coins <= c1 or coins <= c2:
 	       break
        
	    cn += 1

	    while health > 0 and eh > 0 and coins > 0:
        
	        c1 = random.randint(8,13)
	        c2 = random.randint(15,26)
	        c3 = random.randint(6,16)
	        c4 = random.randint(20,36)
	        
	        while True:
	        	prnt(cn, health, bsp, eh, ssp, ed, d1, d2, d3, d4, c, coins, c1, c2, c3, c4)
	        	ch = int(input(usr + " --> "))
        	
	        	if ch == 1:
	        		coins = coins - c1
	        		tc += c1
	        		eh = eh - s1
	        		td += s1
	        		health = health - ed
	        	elif ch == 2:
	        		coins = coins - c2
	        		tc += c2
	        		eh = eh - s2
	        		td += s2
	        		health = health - ed
	        	elif ch == 3:
	        		coins = coins - c3
	        		tc += c3
	        		health = health + s3
	        		health = health - ed
	        	elif ch == 4:
	        		coins = coins - c4
	        		tc += c4
	        		health = health + ed
	        		health = health - ed
	        	elif ch == 5:
	        		if cn == 2:
	        			print('')
	        			print('')
	        			temp = input('You discovered a secret passage and found!', sc,'coins !')
        				coins += sc
        			
        			else:
        				print("unknown input")
        		
        		if ch == 1 or ch == 2 or ch == 3 or ch == 4 or ch == 5:
        			break

	clear()

	if health <= 0:
		print("You died! Better luck next time...")
	else:
		print("You ran out of coins!")
		print('')
		print('')
		print('')



	ch = input('Press ENTER to exit. Press 1 to view stats and seed.  ')

	#print stats and seed

	if ch == '1':
		clear()
		cn -= 1
	
		cn = str(cn)
		td = str(td)
		tc = str(tc)
	
		print('Total Caves won:', cn)
		print('Total Damage dealt:', td)
		print('Total Coins spent:', tc)
	
		seed = ''
		seed += cn
		seed += td
		seed += tc
	
		print('Seed:', seed)
		print('')
		print('')
		ch = input('Press ENTER to exit the game ')
elif ch == '2':
	clear()
	
	seed = '12345'
	while len(seed) != 6:
		seed = input('Enter seed: ')
		clear()
		if len(seed) != 6:
			print('Wrong seed')
			print('')
	
	cn = seed[:2]
	td = seed[2:4]
	tc = seed[4:]
	
	clear()
	
	print('Seed:', seed)
	print('')
	print('Total Caves won:', cn)
	print('Total Damage dealt:', td)
	print('Total Coins spent:', tc)
	
	temp = input('Press ENTER to exit. ')
	
elif ch == '3':
	clear()
	print('About page')
	print('')
	temp = input('Press ENTER to exit. ')