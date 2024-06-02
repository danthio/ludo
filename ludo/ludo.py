import tkinter as tk
import random
from PIL import Image,ImageTk
import math

def home_and_away(col):

	global game1,game2
	home=[]
	away=[]


	for i in game2:
		col_=i.split("_")[0]

		if col_==col:
			if game2[i][0]==col_[0]:
				home.append(i)

			else:
				away.append(i)

	return [home,away]

val1_=0
val1=0
st1=1
sel_1=""
_st1=0


def one():
	global val1,val1_,st1,st1_,_st1,game_mode,game1,game2,sel_1,m1,m_1,turn
	global dice_1_st

	if st1==0:
		con=0

		if game_mode=="rush_mode":
			col=game1[0]

			h,a=home_and_away(col)

			if len(h)==4 and val1==6:
				con=1
				st1=1
				sel_1=h[random.randint(0,len(h)-1)]

				#print(sel_1)
				val1=0
				val1_=0
				m1=0
				m_1=0
				st1_=0

				
				
			elif len(a)>0:

				if len(h)>0 and val1==6:

					ha=random.randint(0,1)

					if ha==0:
						con=1
						st1=1
						sel_1=h[random.randint(0,len(h)-1)]
						val1=0
						val1_=0
						m1=0
						m_1=0
						st1_=0
						
						
						
					else:
						con=1
						st1=1
						sel_1=a[random.randint(0,len(a)-1)]
						val1_=game2[sel_1][-2]
						m1=0
						m_1=game2[sel_1][-3]
						st1_=0
						
						
				else:
					con=1
					st1=1				
					sel_1=a[random.randint(0,len(a)-1)]
					val1_=game2[sel_1][-2]
					m1=0
					m_1=game2[sel_1][-3]
					st1_=0
		if con==0:
			dice_1_st=0


					

	root.after(1,one)





st1_=1
m1=0
m_1=0
def move_1():
	global st1,st1_,_st1,val1,val1_,sel_1,m1,m_1,dice_1_st
	global game1,game2


	if st1_==0:

		if 0<=val1_<=4:
			game2[sel_1]=[1+m_1,0,game1[0],m_1,val1_,0]

		elif 5<=val1_<=10:

			if val1_==5:
				m_1=0


			game2[sel_1]=[5-m_1,2,game1[1],m_1,val1_,0]


		elif val1_==11:
			game2[sel_1]=[0,1,game1[1],m_1,val1_,0]
		elif 12<=val1_<=17:
			if val1_==12:
				m_1=0

			game2[sel_1]=[m_1,0,game1[1],m_1,val1_,0]
		elif 18<=val1_<=23:
			if val1_==18:
				m_1=0

			game2[sel_1]=[5-m_1,2,game1[2],m_1,val1_,0]
		elif val1_==24:
			game2[sel_1]=[0,1,game1[2],m_1,val1_,0]
		elif 25<=val1_<=30:
			if val1_==25:
				m_1=0

			game2[sel_1]=[m_1,0,game1[2],m_1,val1_,0]

		elif 31<=val1_<=36:
			if val1_==31:
				m_1=0
			game2[sel_1]=[5-m_1,2,game1[3],m_1,val1_,0]
		elif val1_==37:
			game2[sel_1]=[0,1,game1[3],m_1,val1_,0]
		elif 38<=val1_<=43:
			if val1_==38:
				m_1=0

			game2[sel_1]=[m_1,0,game1[3],m_1,val1_,0]


		elif 44<=val1_<=49:
			if val1_==44:
				m_1=0

			game2[sel_1]=[5-m_1,2,game1[0],m_1,val1_,0]
		elif 50<=val1_<= 55:
			if val1_==50:
				m_1=0

			game2[sel_1]=[m_1,1,game1[0],m_1,val1_,0]		
		elif val1_==56:
			game2[sel_1]=[6,1,game1[0],m_1,val1_,0]

		main()


		
		#print(game2[sel_1])
		if m1==val1:
			st1_=1
			game2[sel_1][-1]=1

			dice_1_st=0
			

		

		m1+=1
		m_1+=1
		val1_+=1




	root.after(500,move_1)











val2=0
st2=1
def two():
	global val2


	pass



val3=0
st3=1
def three():
	global val3


	pass



val4=0
st4=1
def four():
	global val4


	pass





dd1=0
def _dice_1():
	global dice_1,dice_1_st,dd1,val1,st1

	if dice_1_st==0:

		v=random.randint(1,6)

		_dice_(dice_1,v)

		dd1+=1

		if dd1==10:
			dd1=0
			dice_1_st=1
			val1=v
			st1=0
			#print(val1)

	root.after(100,_dice_1)



dd2=0
def _dice_2():
	global dice_2,dice_2_st,dd2,val2,st2

	if dice_2_st==0:

		v=random.randint(1,6)

		_dice_(dice_2,v)

		dd2+=1

		if dd2==10:
			dd2=0
			dice_2_st=1
			val2=v
			st2=0

	root.after(200,_dice_2)


dd3=0
def _dice_3():
	global dice_3,dice_3_st,dd3,val3,st3

	if dice_3_st==0:

		v=random.randint(1,6)

		_dice_(dice_3,v)

		dd3+=1

		if dd3==10:
			dd3=0
			dice_3_st=1
			val3=v
			st3=0

	root.after(200,_dice_3)


dd4=0
def _dice_4():
	global dice_4,dice_4_st,dd4,val4,st4

	if dice_4_st==0:

		v=random.randint(1,6)

		_dice_(dice_4,v)

		dd4+=1

		if dd4==10:
			dd4=0
			dice_4_st=1
			val4=v
			st4=0

	root.after(200,_dice_4)



def _dice_(dd,v):

	dd.delete("all")	

	dd.create_arc(0,0,20,20,start=90,extent=90,style="arc",outline="#000000",width=2)
	dd.create_arc(50-21,0,50-1,20,start=0,extent=90,style="arc",outline="#000000",width=2)
	dd.create_arc(0,50-21,20,50-1,start=180,extent=90,style="arc",outline="#000000",width=2)
	dd.create_arc(50-21,50-21,50-1,50-1,start=270,extent=90,style="arc",outline="#000000",width=2)

	dd.create_line(10,1, 40,1,fill="#000000",width=2)
	dd.create_line(10,49, 40,49,fill="#000000",width=2)
	dd.create_line(1,10,1,40,fill="#000000",width=2)
	dd.create_line(49,10,49,40,fill="#000000",width=2)


	

	if v==1:

		dd.create_oval(25-4,25-4, 25+4,25+4,fill="#000000",outline="#000000")


	elif v==2:
		dd.create_oval(50-10-8,10, 50-10,10+8,fill="#000000",outline="#000000"	)
		dd.create_oval(10,50-10-8, 18,50-10,fill="#000000",outline="#000000")

	elif v==3:

		dd.create_oval(50-10-8,10, 50-10,10+8,fill="#000000",outline="#000000"	)
		dd.create_oval(10,50-10-8, 18,50-10,fill="#000000",outline="#000000")	

		dd.create_oval(25-4,25-4, 25+4,25+4,fill="#000000",outline="#000000")	
	elif v==4:	

		dd.create_oval(50-10-8,10, 50-10,10+8,fill="#000000",outline="#000000"	)
		dd.create_oval(10,50-10-8, 18,50-10,fill="#000000",outline="#000000")	

		dd.create_oval(50-10-8,50-10-8, 50-10,50-10,fill="#000000",outline="#000000"	)
		dd.create_oval(10,10, 18,10+8,fill="#000000",outline="#000000")


			
	elif v==5:	

		dd.create_oval(50-10-8,10, 50-10,10+8,fill="#000000",outline="#000000"	)
		dd.create_oval(10,50-10-8, 18,50-10,fill="#000000",outline="#000000")	

		dd.create_oval(50-10-8,50-10-8, 50-10,50-10,fill="#000000",outline="#000000"	)
		dd.create_oval(10,10, 18,10+8,fill="#000000",outline="#000000")

		dd.create_oval(25-4,25-4, 25+4,25+4,fill="#000000",outline="#000000")



	elif v==6:	

		dd.create_oval(50-10-8,10, 50-10,10+8,fill="#000000",outline="#000000"	)
		dd.create_oval(10,50-10-8, 18,50-10,fill="#000000",outline="#000000")	

		dd.create_oval(50-10-8,50-10-8, 50-10,50-10,fill="#000000",outline="#000000"	)
		dd.create_oval(10,10, 18,10+8,fill="#000000",outline="#000000")

		dd.create_oval(10,25-4, 18,25+4,fill="#000000",outline="#000000")
		dd.create_oval(50-10-8,25-4, 50-10,25+4,fill="#000000",outline="#000000")


def main():
	global state


	if state=="game":
		draw_bg()

	#root.after(500,main)





im=Image.open("data/quit.png")
im=im.resize((30,30))
im.save("data/quit.png")



im=Image.open("data/back.png")
im=im.resize((30,30))
im.save("data/back.png")

def draw_bg():
	global game1,game2,s,can,wd,st_

	global a1,a2,a3,a4

	global state,quit



	st=Image.open("data/star.png")
	st=st.resize((int(s*3/4),int(s*3/4)))
	st.save("data/st.png")

	st_=ImageTk.PhotoImage(file="data/st.png")
	can.delete("all")


	state="game"


	quit=ImageTk.PhotoImage(file="data/quit.png")


	can.create_image(wd-10-30,10,image=quit,anchor="nw")




	x,y=70,70
	

	can.create_rectangle(x,y, x+s*15,y+s*15,outline="#000000")

	can.create_rectangle(x,y+s*9,x+s*6,y+s*15,fill=game1[0],outline="#000000")
	can.create_rectangle(x+s,y+s*10,x+s*5,y+s*14,fill="#ffffff",outline="#000000")



	d=(s*4-2*s)/3

	x_,y_=x+s,y+s*10

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill=game1[0],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill=game1[0],outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill=game1[0],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill=game1[0],outline="#000000")


	can.create_rectangle(x,y,x+s*6,y+s*6,fill=game1[1],outline="#000000")
	can.create_rectangle(x+s,y+s,x+s*5,y+s*5,fill="#ffffff",outline="#000000")

	x_,y_=x+s,y+s

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill=game1[1],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill=game1[1],outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill=game1[1],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill=game1[1],outline="#000000")


	
	can.create_rectangle(x+s*9,y,x+s*15,y+s*6,fill=game1[2],outline="#000000")
	can.create_rectangle(x+s*10,y+s,x+s*14,y+s*5,fill="#ffffff",outline="#000000")

	x_,y_=x+s*10,y+s

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill=game1[2],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill=game1[2],outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill=game1[2],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill=game1[2],outline="#000000")





	can.create_rectangle(x+s*9,y+s*9,x+s*15,y+s*15,fill=game1[3],outline="#000000")
	can.create_rectangle(x+s*10,y+s*10,x+s*14,y+s*14,fill="#ffffff",outline="#000000")


	x_,y_=x+s*10,y+s*10

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill=game1[3],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill=game1[3],outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill=game1[3],outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill=game1[3],outline="#000000")






	#1

	x_=x+s*6
	y_=y+s*9
	for _y in range(6):

		col="#ffffff"

		if _y==4:
			col=game1[0]

		can.create_rectangle(x_,y_, x_+s,y_+s,fill=col)


		y_+=s




	x_=x+s*7
	y_=y+s*9
	for _y in range(6):

		col=game1[0]

		if _y==5:
			col="#ffffff"

		can.create_rectangle(x_,y_, x_+s,y_+s,fill=col)


		y_+=s


	x_=x+s*8
	y_=y+s*9
	for _y in range(6):

		col="#ffffff"

		can.create_rectangle(x_,y_, x_+s,y_+s,fill=col)


		y_+=s


	arrow=Image.open("data/"+str(game1[0][0])+".png")

	a1=arrow.rotate(90)
	a1=a1.resize((int(s*3/4),int(s*3/4)))
	a1.save("data/"+game1[0][0]+"1.png")



	a1=ImageTk.PhotoImage(file="data/"+game1[0][0]+"1.png")

	can.create_image(x+s*7+s*1/8,y+s*14+s*1/8,image=a1,anchor="nw")


	draw_star(x+s*8+s*1/8,y+s*12+s*1/8)



	#2

	x_,y_=x,y+s*6

	for _x in range(6):
		col="#ffffff"

		if _x==1:
			col=game1[1]


		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")

		x_+=s


	x_,y_=x,y+s*7

	for _x in range(6):
		col=game1[1]

		if _x==0:
			col="#ffffff"


		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")

		x_+=s


	x_,y_=x,y+s*8

	for _x in range(6):
		col="#ffffff"

		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")

		x_+=s








	arrow=Image.open("data/"+str(game1[1][0])+".png")

	#a=arrow.rotate(90)
	a=arrow.resize((int(s*3/4),int(s*3/4)))
	a.save("data/"+game1[1][0]+"1.png")



	a2=ImageTk.PhotoImage(file="data/"+game1[1][0]+"1.png")

	can.create_image(x+s*1/8,y+s*7+s*1/8,image=a2,anchor="nw")


	draw_star(x+s*2+s*1/8,y+s*8+s*1/8)



	x_=x+s*6
	y_=y

	for _y in range(6):
		col="#ffffff"


		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")
		y_+=s


	x_=x+s*7
	y_=y

	for _y in range(6):
		col=game1[2]

		if _y==0:
			col="#ffffff"


		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")
		y_+=s



	x_=x+s*8
	y_=y

	for _y in range(6):
		col="#ffffff"

		if _y==1:
			col=game1[2]


		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")
		y_+=s




	arrow=Image.open("data/"+str(game1[2][0])+".png")

	a=arrow.rotate(270)
	a=a.resize((int(s*3/4),int(s*3/4)))
	a.save("data/"+game1[2][0]+"1.png")



	a3=ImageTk.PhotoImage(file="data/"+game1[2][0]+"1.png")

	can.create_image(x+s*7+s*1/8,y+s*1/8,image=a3,anchor="nw")


	draw_star(x+s*6+s*1/8,y+s*2+s*1/8)



	x_=x+s*9
	y_=y+s*6

	for _x in range(6):
		col="#ffffff"

		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")

		x_+=s


	x_=x+s*9
	y_=y+s*7

	for _x in range(6):
		col=game1[3]
		if _x==5:
			col="#ffffff"


		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")

		x_+=s


	x_=x+s*9
	y_=y+s*8

	for _x in range(6):
		col="#ffffff"
		if _x==4:
			col=game1[3]


		can.create_rectangle(x_,y_,x_+s,y_+s,fill=col,outline="#000000")

		x_+=s





	arrow=Image.open("data/"+str(game1[3][0])+".png")

	a=arrow.rotate(180)
	a=a.resize((int(s*3/4),int(s*3/4)))
	a.save("data/"+game1[3][0]+"1.png")



	a4=ImageTk.PhotoImage(file="data/"+game1[3][0]+"1.png")

	can.create_image(x+s*14+s*1/8,y+s*7+s*1/8,image=a4,anchor="nw")


	draw_star(x+s*12+s*1/8,y+s*6+s*1/8)



	x_=x+s*6
	y_=y+s*6
	can.create_polygon(x_,y_, x_+s+s/2, y_+s+s/2, x_,y_+s*3,fill=game1[1],outline="#000000")
	can.create_polygon(x_,y_, x_+s+s/2, y_+s+s/2, x_+s*3,y_,fill=game1[2],outline="#000000")
	x_=x+s*9
	y_=y+s*9
	can.create_polygon(x_,y_, x_-s-s/2, y_-s-s/2, x_,y_-s*3,fill=game1[3],outline="#000000")
	can.create_polygon(x_,y_, x_-s-s/2, y_-s-s/2, x_-s*3,y_,fill=game1[0],outline="#000000")

	x,y=70,70

	h_ar=[[x+s,y+s*10],[x+s,y+s],[x+s*10,y+s],[x+s*10,y+s*10]]


	ar=[]

	for i in game2:
		if game2[i][0]==col[0]:

			pass
		else:
			pass	

	for i in game2:
		col=i.split("_")[0]


		if game2[i][0]==col[0]:
			p=game2[i][1]

			x_,y_=h_ar[game1.index(col)]


			_s=s*2/3
			if int(p)==1:

				draw_pointer(x_+_s+s/2,y_+_s+s/2,25,col)

			elif int(p)==2:
				draw_pointer(x_+_s*2+s+s/2,y_+_s+s/2,25,col)

			elif int(p)==3:
				draw_pointer(x_+_s+s/2,y_+_s*2+s+s/2,25,col)
			elif int(p)==4:
				draw_pointer(x_+_s*2+s+s/2,y_+_s*2+s+s/2,25,col)
		else:
			g_ar=game2[i]

			xx=g_ar[0]
			yy=g_ar[1]

			p=game1.index(g_ar[2])

			if p==0:
				x_,y_=x+s*6,y+s*15

				v="b"

			elif p==1:
				x_,y_=x,y+s*6

				v="l"


			elif p==2:
				x_,y_=x+s*9,y

				v="t"


			elif p==3:
				x_,y_=x+s*15,y+s*9

				v="r"







			if v=="b":

				_xx=x_+yy*s+s/2
				_yy=y_-xx*s-s/2
			elif v=="l":

				_xx=x_+xx*s+s/2
				_yy=y_+yy*s+s/2

			elif v=="t":

				_xx=x_-yy*s-s/2
				_yy=y_+xx*s+s/2
			elif v=="r":

				_xx=x_-xx*s-s/2
				_yy=y_-yy*s-s/2

			


			draw_pointer(_xx,_yy,25,col)


def draw_star(x,y):
	global can,st_

	can.create_image(x,y,image=st_,anchor="nw")




def sel_game_mode():
	global can,state
	global wd,ht,bg


	state="game_mode"
	can.delete("all")

	im=Image.open("data/ludo.jpg")
	x,y=im.size

	r=y/590

	x=int(x*r)
	y=590

	xx=(x-590)/2

	bg=ImageTk.PhotoImage(file="data/ludo.jpg")

	can.create_image(-xx,0,image=bg,anchor="nw")

	create_rectangle(can,0, 0, 590, 590, fill='#000000', alpha=.5)


	can.create_arc(wd/2-100,ht/2-30, wd/2-100+30,ht/2,style="arc",start=90,extent=180,outline="#ffffff",width=1)
	can.create_arc(wd/2+100-30,ht/2-30,wd/2+100,ht/2,style="arc",start=270,extent=180,outline="#ffffff",width=1)


	can.create_line(wd/2-100+15,ht/2-30,  wd/2+100-15,ht/2-30,fill="#ffffff",width=1)
	can.create_line(wd/2-100+15,ht/2,  wd/2+100-15,ht/2,fill="#ffffff",width=1)



	can.create_arc(wd/2-100,ht/2-30+60, wd/2-100+30,ht/2+60,style="arc",start=90,extent=180,outline="#ffffff",width=1)
	can.create_arc(wd/2+100-30,ht/2-30+60,wd/2+100,ht/2+60,style="arc",start=270,extent=180,outline="#ffffff",width=1)


	can.create_line(wd/2-100+15,ht/2-30+60,  wd/2+100-15,ht/2-30+60,fill="#ffffff",width=1)
	can.create_line(wd/2-100+15,ht/2+60,  wd/2+100-15,ht/2+60,fill="#ffffff",width=1)




	can.create_text(wd/2,ht/2-30+15,text="Classic",font=("FreeMono",13),fill="#ffffff")
	can.create_text(wd/2,ht/2-30+15+60,text="Rush Mode",font=("FreeMono",13),fill="#ffffff")


def sel_col():
	global can,state
	global wd,ht,bg,choice,back


	state="sel_col"
	can.delete("all")

	im=Image.open("data/ludo.jpg")
	x,y=im.size

	r=y/590

	x=int(x*r)
	y=590

	xx=(x-590)/2

	bg=ImageTk.PhotoImage(file="data/ludo.jpg")

	back=ImageTk.PhotoImage(file="data/back.png")

	can.create_image(-xx,0,image=bg,anchor="nw")



	create_rectangle(can,0, 0, 590, 590, fill='#000000', alpha=.5)


	can.create_image(wd-40,10,image=back,anchor="nw")

	can.create_text(wd/2, ht/4,text="Select Side",font=("FreeMono",20),fill="#ffffff")




	xx=(wd-100*4)/5
	x_=xx

	ar=["red","green","yellow","blue"]


	for _ in range(4):

		can.create_oval(x_,ht/2-50, x_+100,ht/2+50,outline="#ffffff")

		if not choice=="":
			if _==ar.index(choice):

				can.create_oval(x_,ht/2-50, x_+100,ht/2+50,outline="#ffffff",fill="#ffffff")


		#print(x_+50)


		draw_pointer(x_+50,ht/2+30,50,ar[_])
		x_+=100+xx

	can.create_arc(wd/2-100,ht-50-30, wd/2-100+30,ht-50,start=90,extent=180,style="arc",outline="#ffffff")
	can.create_arc(wd/2+100-30,ht-50-30, wd/2+100,ht-50,start=270,extent=180,style="arc",outline="#ffffff")


	can.create_line(wd/2-100+15,ht-50-30, wd/2+100-15,ht-50-30,fill="#ffffff") 
	can.create_line(wd/2-100+15,ht-50, wd/2+100-15,ht-50,fill="#ffffff")

	can.create_text(wd/2,ht-50-30+15,text="Start Game",font=("FreeMono",13),fill="#ffffff")		

def draw_pointer(x,y,sz,col):
	global can

	a=90-20

	ar=[x,y]

	cx=x
	cy=y-sz*0.7
	for _ in range(220):

		x=sz/3*math.sin(math.radians(a))+cx
		y=sz/3*math.cos(math.radians(a))+cy


		ar.append(x)
		ar.append(y)

		a+=1


	can.create_polygon(ar,fill="#ffffff",outline="#000000")
	can.create_oval(cx-sz/5,cy-sz/5, cx+sz/5,cy+sz/5, fill=col,outline="#000000")








def can_commands(e):
	global state,game_mode,game1,turn
	global wd,ht,choice,sx
	global dice_1_st,dice_2_st,dice_3_st,dice_4_st
	global dice_1,dice_2,dice_3,dice_4

	if state=="game":
		cx=wd-10-15
		cy=10+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
		if r<=15:
			choice=""
			sx=0
			game1=["red","green","yellow","blue"]
			sel_game_mode()

			turn=""

			dice_1.delete("all")
			dice_2.delete("all")
			dice_3.delete("all")
			dice_4.delete("all")


			dice_1.place_forget()
			dice_2.place_forget()	
			dice_3.place_forget()
			dice_4.place_forget()								

	elif state=="sel_col":
		

		

		cx=wd-10-15
		cy=10+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
		if r<=15:
			choice=""
			sel_game_mode()



		cy=ht/2



		cx=88
		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
		if r<=50:
			choice="red"
			sel_col()
			return


		cx=226
		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
		if r<=50:
			choice="green"
			sel_col()
			return

		cx=364
		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
		if r<=50:
			choice="yellow"
			sel_col()
			return

		cx=502
		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
		if r<=50:
			choice="blue"
			sel_col()
			return


		#195.0 510 395.0 540

		if choice != "":


			if 195+15<=e.x<=395-15:
				if 510<=e.y<=540:
					shift(choice)
					choice=""
					draw_bg()

					dice_1.place(in_=root,x=70-60,y=590-70-50)
					dice_2.place(in_=root,x=70-60,y=70)
					dice_3.place(in_=root,x=590-70+10,y=70)
					dice_4.place(in_=root,x=590-70+10,y=590-70-50)

					if game_mode=="rush_mode":

						dice_1_st=0
						dice_2_st=0
						dice_3_st=0
						dice_4_st=0
					else:
						dice_1_st=0
						turn=game1[0]



					return

			cx=195+15
			cy=510+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:
				shift(choice)
				choice=""
				draw_bg()

				dice_1.place(in_=root,x=70-60,y=590-70-50)
				dice_2.place(in_=root,x=70-60,y=70)
				dice_3.place(in_=root,x=590-70+10,y=70)
				dice_4.place(in_=root,x=590-70+10,y=590-70-50)

				if game_mode=="rush_mode":

					dice_1_st=0
					dice_2_st=0
					dice_3_st=0
					dice_4_st=0

				else:
					dice_1_st=0
					turn=game1[0]
				return

			cx=395-15
			cy=510+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:
				shift(choice)
				choice=""
				draw_bg()



				dice_1.place(in_=root,x=70-60,y=590-70-50)
				dice_2.place(in_=root,x=70-60,y=70)
				dice_3.place(in_=root,x=590-70+10,y=70)
				dice_4.place(in_=root,x=590-70+10,y=590-70-50)

				if game_mode=="rush_mode":

					dice_1_st=0
					dice_2_st=0
					dice_3_st=0
					dice_4_st=0


				else:
					dice_1_st=0
					turn=game1[0]
				return


	elif state=="game_mode":

		if wd/2-100+15<=e.x<=wd/2+100-15:
			if ht/2-30<=e.y<=ht/2:
				game_mode="classic"
				sel_col()

				return

			if ht/2-30+60<=e.y<=ht/2+60:
				game_mode="rush_mode"
				sel_col()

				return

		cx,cy=wd/2-100+15,ht/2-30+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			game_mode="classic"
			sel_col()

			return


		cx,cy=wd/2+100-30+15,ht/2-30+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			game_mode="classic"
			sel_col()

			return

		


		cx,cy=wd/2-100+15,ht/2-30+15+60

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			game_mode="rush_mode"
			sel_col()

			return


		cx,cy=wd/2+100-30+15,ht/2-30+15+60

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			game_mode="rush_mode"
			sel_col()

			return



def shift(c):
	global game1

	if c!="red":

		v=game1.index(c)

		game1[0]=c

		game1[v]="red"

		




images = []  # to hold the newly created image

def create_rectangle(can,x1, y1, x2, y2, **kwargs):
	global images
	if 'alpha' in kwargs:
		alpha = int(kwargs.pop('alpha') * 255)
		fill = kwargs.pop('fill')
		fill = root.winfo_rgb(fill) + (alpha,)
		image = Image.new('RGBA', (x2-x1, y2-y1), fill)
		images.append(ImageTk.PhotoImage(image))
		can.create_image(x1, y1, image=images[-1], anchor='nw')




wd=590
ht=590


bg=0
state="game_mode"
game_mode=""


s=30

turn=""


game1=["red","green","yellow","blue"]
game2={"red_1":"r1",
		"red_2":"r2",
		"red_3":"r3",
		"red_4":"r4",

		"green_1":"g1",
		"green_2":"g2",
		"green_3":"g3",
		"green_4":"g4",		

		"yellow_1":"y1",
		"yellow_2":"y2",
		"yellow_3":"y3",
		"yellow_4":"y4",

		"blue_1":"b1",
		"blue_2":"b2",
		"blue_3":"b3",
		"blue_4":"b4"

		}




a1=0
a2=0
a3=0
a4=0



def star__():
	global st_



st_=0



choice=""


quit=0
back=0

root=tk.Tk()
root.geometry(str(wd)+"x"+str(ht)+"+20+20")
root.title("hludo")

can=tk.Canvas(width=wd,height=ht,relief="flat",highlightthickness=0,border=0,
	bg="#ffffff")
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_commands)

dice_1=tk.Canvas(width=50,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
dice_1_st=1

dice_2=tk.Canvas(width=50,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
dice_2_st=1

dice_3=tk.Canvas(width=50,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
dice_3_st=1

dice_4=tk.Canvas(width=50,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
dice_4_st=1




_dice_1()
_dice_2()
_dice_3()
_dice_4()



one()
move_1()



main()
sel_game_mode()
root.mainloop()