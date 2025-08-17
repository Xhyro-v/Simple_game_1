import random

while True:
	perintah = input("Tanyakan sesuatu: ")
	
	if perintah == "EXIT":
		print("Assistant: Bye bro👋")
		break
		
	elif perintah == "Hai":
	    jawaban = ["Hai juga broo", "supp G", "yo homie"]
	    print("Assistant:", random.choice(jawaban))
	      
	elif perintah == "Cara dapat pacar":
	    jawaban = [
	        "Lu nanya gw? Gw aja kaga punya oon",
	        "Kaga tau gw, tanya aja temen lu yang punya",
	        "Janganlah kau berpacaran anak muda🫂"
	    ]
	    print("Assistant:", random.choice(jawaban))
	         
	else:
	    print("Belom di coding buat gituan gw, yang ngodingnya males")