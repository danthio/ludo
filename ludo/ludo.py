import tkinter as tk
import random
from PIL import Image,ImageTk
import math
def wins():
	global game1,winners

	for c in game1:

		try:
			b=winners.index(c)
		except:

			e=det(c)
			if e==0:
				winners.append(c)


	root.after(1,wins)

def det(c):
	global game2

	con=0

	for i in game2:

		col=i.split("_")[0]

		if col==c:

			if len(game2[i])==2:
				con=1
				break
			else:
				if game2[i][-2]!=56:
					con=1
					break




	return con

ones_=[]

def return_home_1():
	global game1,game2,ones_

	con=[0]

	for n in range(len(ones_)):
		

		i=ones_[n][0]

		if ones_[n][1]==0:
			ones_[n].append(game2[i][-2])
			ones_[n].append(game2[i][-3])

			ones_[n][1]=1




		if 0<=ones_[n][-2]<=4:

			if ones_[n][-2]==4:
				ones_[n][-1]=4
			game2[i]=[1+ones_[n][-1],0,game1[0],ones_[n][-1],ones_[n][-2],0]

		elif 5<=ones_[n][-2]<=10:

			if ones_[n][-2]==10:
				ones_[n][-1]=5


			game2[i]=[5-ones_[n][-1],2,game1[1],ones_[n][-1],ones_[n][-2],0]


		elif ones_[n][-2]==11:
			game2[i]=[0,1,game1[1],ones_[n][-1],ones_[n][-2],0]
		elif 12<=ones_[n][-2]<=17:
			if ones_[n][-2]==17:
				ones_[n][-1]=5

			game2[i]=[ones_[n][-1],0,game1[1],ones_[n][-1],ones_[n][-2],0]
		elif 18<=ones_[n][-2]<=23:
			if ones_[n][-2]==23:
				ones_[n][-1]=5

			game2[i]=[5-ones_[n][-1],2,game1[2],ones_[n][-1],ones_[n][-2],0]
		elif ones_[n][-2]==24:
			game2[i]=[0,1,game1[2],ones_[n][-1],ones_[n][-2],0]
		elif 25<=ones_[n][-2]<=30:
			if ones_[n][-2]==30:
				ones_[n][-1]=5

			game2[i]=[ones_[n][-1],0,game1[2],ones_[n][-1],ones_[n][-2],0]

		elif 31<=ones_[n][-2]<=36:
			if ones_[n][-2]==36:
				ones_[n][-1]=5
			game2[i]=[5-ones_[n][-1],2,game1[3],ones_[n][-1],ones_[n][-2],0]
		elif ones_[n][-2]==37:
			game2[i]=[0,1,game1[3],ones_[n][-1],ones_[n][-2],0]
		elif 38<=ones_[n][-2]<=43:
			if ones_[n][-2]==43:
				ones_[n][-1]=5

			game2[i]=[ones_[n][-1],0,game1[3],ones_[n][-1],ones_[n][-2],0]


		elif 44<=ones_[n][-2]<=49:
			if ones_[n][-2]==49:
				ones_[n][-1]=5

			game2[i]=[5-ones_[n][-1],2,game1[0],ones_[n][-1],ones_[n][-2],0]


		elif 50:

			game2[i]=[ones_[n][-1],1,game1[0],ones_[n][-1],ones_[n][-2],0]	



		if ones_[n][-2]==-1:
			game2[i]=i[0]+i[-1]

			con=[1,i]


		ones_[n][-2]-=1
		ones_[n][-1]-=1
		main()	
	if con[0]==1:
		v=0

		for _ in range(len(ones_)):

			if ones_[_][0]==con[1]:
				v=_
				break
		ones_.pop(v)

	root.after(50,return_home_1)



twos_=[]

def return_home_2():
	global game1,game2,twos_

	con=[0]

	for n in range(len(twos_)):
		

		i=twos_[n][0]

		if twos_[n][1]==0:
			twos_[n].append(game2[i][-2])
			twos_[n].append(game2[i][-3])

			twos_[n][1]=1




		if 0<=twos_[n][-2]<=4:

			if twos_[n][-2]==4:
				twos_[n][-1]=4
			game2[i]=[1+twos_[n][-1],0,game1[1],twos_[n][-1],twos_[n][-2],0]

		elif 5<=twos_[n][-2]<=10:

			if twos_[n][-2]==10:
				twos_[n][-1]=5


			game2[i]=[5-twos_[n][-1],2,game1[2],twos_[n][-1],twos_[n][-2],0]


		elif twos_[n][-2]==11:
			game2[i]=[0,1,game1[2],twos_[n][-1],twos_[n][-2],0]
		elif 12<=twos_[n][-2]<=17:
			if twos_[n][-2]==17:
				twos_[n][-1]=5

			game2[i]=[twos_[n][-1],0,game1[2],twos_[n][-1],twos_[n][-2],0]
		elif 18<=twos_[n][-2]<=23:
			if twos_[n][-2]==23:
				twos_[n][-1]=5

			game2[i]=[5-twos_[n][-1],2,game1[3],twos_[n][-1],twos_[n][-2],0]
		elif twos_[n][-2]==24:
			game2[i]=[0,1,game1[3],twos_[n][-1],twos_[n][-2],0]
		elif 25<=twos_[n][-2]<=30:
			if twos_[n][-2]==30:
				twos_[n][-1]=5

			game2[i]=[twos_[n][-1],0,game1[3],twos_[n][-1],twos_[n][-2],0]

		elif 31<=twos_[n][-2]<=36:
			if twos_[n][-2]==36:
				twos_[n][-1]=5
			game2[i]=[5-twos_[n][-1],2,game1[0],twos_[n][-1],twos_[n][-2],0]
		elif twos_[n][-2]==37:
			game2[i]=[0,1,game1[0],twos_[n][-1],twos_[n][-2],0]
		elif 38<=twos_[n][-2]<=43:
			if twos_[n][-2]==43:
				twos_[n][-1]=5

			game2[i]=[twos_[n][-1],0,game1[0],twos_[n][-1],twos_[n][-2],0]


		elif 44<=twos_[n][-2]<=49:
			if twos_[n][-2]==49:
				twos_[n][-1]=5

			game2[i]=[5-twos_[n][-1],2,game1[1],twos_[n][-1],twos_[n][-2],0]


		elif 50:

			game2[i]=[twos_[n][-1],1,game1[1],twos_[n][-1],twos_[n][-2],0]	




		if twos_[n][-2]==-1:
			game2[i]=i[0]+i[-1]

			con=[1,i]


		twos_[n][-2]-=1
		twos_[n][-1]-=1
		main()	
	if con[0]==1:
		v=0

		for _ in range(len(twos_)):

			if twos_[_][0]==con[1]:
				v=_
				break
		twos_.pop(v)

	root.after(50,return_home_2)




threes_=[]

def return_home_3():
	global game1,game2,threes_

	con=[0]

	for n in range(len(threes_)):
		

		i=threes_[n][0]

		if threes_[n][1]==0:
			threes_[n].append(game2[i][-2])
			threes_[n].append(game2[i][-3])

			threes_[n][1]=1




		if 0<=threes_[n][-2]<=4:

			if threes_[n][-2]==4:
				threes_[n][-1]=4
			game2[i]=[1+threes_[n][-1],0,game1[2],threes_[n][-1],threes_[n][-2],0]

		elif 5<=threes_[n][-2]<=10:

			if threes_[n][-2]==10:
				threes_[n][-1]=5


			game2[i]=[5-threes_[n][-1],2,game1[3],threes_[n][-1],threes_[n][-2],0]


		elif threes_[n][-2]==11:
			game2[i]=[0,1,game1[3],threes_[n][-1],threes_[n][-2],0]
		elif 12<=threes_[n][-2]<=17:
			if threes_[n][-2]==17:
				threes_[n][-1]=5

			game2[i]=[threes_[n][-1],0,game1[3],threes_[n][-1],threes_[n][-2],0]
		elif 18<=threes_[n][-2]<=23:
			if threes_[n][-2]==23:
				threes_[n][-1]=5

			game2[i]=[5-threes_[n][-1],2,game1[0],threes_[n][-1],threes_[n][-2],0]
		elif threes_[n][-2]==24:
			game2[i]=[0,1,game1[0],threes_[n][-1],threes_[n][-2],0]
		elif 25<=threes_[n][-2]<=30:
			if threes_[n][-2]==30:
				threes_[n][-1]=5

			game2[i]=[threes_[n][-1],0,game1[0],threes_[n][-1],threes_[n][-2],0]

		elif 31<=threes_[n][-2]<=36:
			if threes_[n][-2]==36:
				threes_[n][-1]=5
			game2[i]=[5-threes_[n][-1],2,game1[1],threes_[n][-1],threes_[n][-2],0]
		elif threes_[n][-2]==37:
			game2[i]=[0,1,game1[1],threes_[n][-1],threes_[n][-2],0]
		elif 38<=threes_[n][-2]<=43:
			if threes_[n][-2]==43:
				threes_[n][-1]=5

			game2[i]=[threes_[n][-1],0,game1[1],threes_[n][-1],threes_[n][-2],0]


		elif 44<=threes_[n][-2]<=49:
			if threes_[n][-2]==49:
				threes_[n][-1]=5

			game2[i]=[5-threes_[n][-1],2,game1[2],threes_[n][-1],threes_[n][-2],0]


		elif 50:

			game2[i]=[threes_[n][-1],1,game1[2],threes_[n][-1],threes_[n][-2],0]	


		if threes_[n][-2]==-1:
			game2[i]=i[0]+i[-1]

			con=[1,i]


		threes_[n][-2]-=1
		threes_[n][-1]-=1
		main()	
	if con[0]==1:
		v=0

		for _ in range(len(threes_)):

			if threes_[_][0]==con[1]:
				v=_
				break
		threes_.pop(v)

	root.after(50,return_home_3)

fours_=[]

def return_home_4():
	global game1,game2,fours_

	con=[0]

	for n in range(len(fours_)):
		

		i=fours_[n][0]

		if fours_[n][1]==0:
			fours_[n].append(game2[i][-2])
			fours_[n].append(game2[i][-3])

			fours_[n][1]=1




		if 0<=fours_[n][-2]<=4:

			if fours_[n][-2]==4:
				fours_[n][-1]=4
			game2[i]=[1+fours_[n][-1],0,game1[3],fours_[n][-1],fours_[n][-2],0]

		elif 5<=fours_[n][-2]<=10:

			if fours_[n][-2]==10:
				fours_[n][-1]=5


			game2[i]=[5-fours_[n][-1],2,game1[0],fours_[n][-1],fours_[n][-2],0]


		elif fours_[n][-2]==11:
			game2[i]=[0,1,game1[0],fours_[n][-1],fours_[n][-2],0]
		elif 12<=fours_[n][-2]<=17:
			if fours_[n][-2]==17:
				fours_[n][-1]=5

			game2[i]=[fours_[n][-1],0,game1[0],fours_[n][-1],fours_[n][-2],0]
		elif 18<=fours_[n][-2]<=23:
			if fours_[n][-2]==23:
				fours_[n][-1]=5

			game2[i]=[5-fours_[n][-1],2,game1[1],fours_[n][-1],fours_[n][-2],0]
		elif fours_[n][-2]==24:
			game2[i]=[0,1,game1[1],fours_[n][-1],fours_[n][-2],0]
		elif 25<=fours_[n][-2]<=30:
			if fours_[n][-2]==30:
				fours_[n][-1]=5

			game2[i]=[fours_[n][-1],0,game1[1],fours_[n][-1],fours_[n][-2],0]

		elif 31<=fours_[n][-2]<=36:
			if fours_[n][-2]==36:
				fours_[n][-1]=5
			game2[i]=[5-fours_[n][-1],2,game1[2],fours_[n][-1],fours_[n][-2],0]
		elif fours_[n][-2]==37:
			game2[i]=[0,1,game1[2],fours_[n][-1],fours_[n][-2],0]
		elif 38<=fours_[n][-2]<=43:
			if fours_[n][-2]==43:
				fours_[n][-1]=5

			game2[i]=[fours_[n][-1],0,game1[2],fours_[n][-1],fours_[n][-2],0]


		elif 44<=fours_[n][-2]<=49:
			if fours_[n][-2]==49:
				fours_[n][-1]=5

			game2[i]=[5-fours_[n][-1],2,game1[3],fours_[n][-1],fours_[n][-2],0]


		elif 50:

			game2[i]=[fours_[n][-1],1,game1[3],fours_[n][-1],fours_[n][-2],0]	


		if fours_[n][-2]==-1:
			game2[i]=i[0]+i[-1]

			con=[1,i]


		fours_[n][-2]-=1
		fours_[n][-1]-=1
		main()	
	if con[0]==1:
		v=0

		for _ in range(len(fours_)):

			if fours_[_][0]==con[1]:
				v=_
				break
		fours_.pop(v)

	root.after(50,return_home_4)

def return_home(p):
	global game1,game2
	global ones_,twos_,threes_,fours_


	ar=[]

	ar2=game2[p][:3]
	for i in game2:
		c1=p.split("_")[0]
		c2=i.split("_")[0]

		if i==p:
			continue

		if c1==c2:
			continue

		if game2[i][:3]==ar2:

			ar.append(i)


	ar3=[]
	for a in ar:

		#if a.split("_")[0]==ar2[-1]:
		#	if game2[a][:2]==[1,0]:
		#		ar3.append(a)


		if game2[a][:2]==[2,2]:
			ar3.append(a)

	for a in ar3:

		v=ar.index(a)
		ar.pop(v)


	for a in ar:

		if game2[a][-1]==1:

			n=a.split("_")[1]
			c=a[0]

			#game2[a]=c+n

			col=a.split("_")[0]

			if game1.index(col)==0:
				ones_.append([a,0])

			elif game1.index(col)==1:
				twos_.append([a,0])


			elif game1.index(col)==2:
				threes_.append([a,0])


			elif game1.index(col)==3:
				fours_.append([a,0])

	main()






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


def one():

	global st1,game_mode,dice_1_st,dice_2_st,st1,st1_,val1,game2,turn


	if st1==0:



		
		h,a=home_and_away(game1[0])

		con2=0


		if len(h)==4 and val1!=6:
			con2=1

			if game_mode=="classic":

				st1=1
				st1_=1
				
				dice_1_st=2
				dice_2_st=0
				turn=game1[1]
				main()


			

			else:
				st1=1
				st1_=1

				dice_1_st=0


		con=0

		if con2==0:

			if val1==6:
				for xh in h:
					con=1

			for xa in a:

				if game2[xa][-2]+val1<=56 and game2[xa][-1]==1:
					con=1
					break
			if con==0:


				if game_mode=="classic":

					st1=1
					st1_=1

					dice_1_st=2
					dice_2_st=0
					turn=game1[1]
					main()



				

				else:
					st1=1
					st1_=1

					dice_1_st=0



				


	root.after(1,one)





st1_=1
m1=0
m_1=0
def move_1():
	global st1,st1_,_st1,val1,val1_,sel_1,m1,m_1,dice_1_st,turn
	global game1,game2
	global game_mode,dice_2_st,winners


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


			if game_mode=="rush_mode":
				
				game2[sel_1][-1]=1

				return_home(sel_1)

				dice_1_st=0
			elif game_mode=="classic":
				
				game2[sel_1][-1]=1

				return_home(sel_1)
				if val1==0:
					dice_1_st=0
				else:
					dice_2_st=0
					dice_1_st=2		
					turn=game1[1]
			main()
			st1_=1

				

		

		m1+=1
		m_1+=1
		val1_+=1




	root.after(100,move_1)

























val2_=0
val2=0
st2=1
sel_2=""
_st2=0


def two():
	global val2,val2_,st2,st2_,_st2,game_mode,game1,game2,sel_2,m2,m_2,turn
	global dice_2_st,dice_3_st

	

	if st2==0:
		con=0
		
		col=game1[1]

		h,a=home_and_away(col)

		if len(h)==4 and val2==6:
			con=1
			st2=1
			sel_2=h[random.randint(0,len(h)-1)]

			#print(sel_2)
			val2=0
			val2_=0
			m2=0
			m_2=0
			st2_=0

			
			
		elif len(a)>0:

			if len(h)>0 and val2==6:

				ha=random.randint(0,1)

				if ha==0:
					con=1
					st2=1
					sel_2=h[random.randint(0,len(h)-1)]
					val2=0
					val2_=0
					m2=0
					m_2=0
					st2_=0
					
					
					
				else:
					
					
					sel_2=a[random.randint(0,len(a)-1)]
					val2_=game2[sel_2][-2]


					while 1:


						if val2_+val2>56:

							aa=a.index(sel_2)
							a.pop(aa)


							if len(a)==0:
								con=0
								break

							sel_2=a[random.randint(0,len(a)-1)]
							val2_=game2[sel_2][-2]
						else:

							if game2[sel_2][-1]==0:

								aa=a.index(sel_2)
								a.pop(aa)


								if len(a)==0:
									con=0
									break

								sel_2=a[random.randint(0,len(a)-1)]
								val2_=game2[sel_2][-2]
							else:


								con=1
								st2=1
								m2=0

								m_2=game2[sel_2][-3]
								st2_=0

								break

					if con==0 and len(h)>0:

						con=1
						st2=1
						sel_2=h[random.randint(0,len(h)-1)]
						val2=0
						val2_=0
						m2=0
						m_2=0
						st2_=0






					





					
					
			else:
				sel_2=a[random.randint(0,len(a)-1)]
				val2_=game2[sel_2][-2]


				while 1:





					if val2_+val2>56:

						aa=a.index(sel_2)
						a.pop(aa)

						if len(a)==0:
							con=0
							break



						sel_2=a[random.randint(0,len(a)-1)]
						val2_=game2[sel_2][-2]
					else:



						if game2[sel_2][-1]==0:

							aa=a.index(sel_2)
							a.pop(aa)


							if len(a)==0:
								con=0
								break

							sel_2=a[random.randint(0,len(a)-1)]
							val2_=game2[sel_2][-2]
						else:
							con=1
							st2=1
							m2=0

							m_2=game2[sel_2][-3]
							st2_=0

							break



		if con==0:


			st2=1
			st2_=1
			con2=0

			


			h,a=home_and_away(game1[1])

			if len(h)>0:
				con2=1
			else:
				if len(a)<4:
					con2=1
				elif len(a)==4:
					for _ in range(4):

						


						if game2[game1[1]+"_"+str(_+1)][-2]!=56:


							con2=1
			if game_mode=="rush_mode":

				if con2==1:

					dice_2_st=0
				elif con2==0:
					dice_2_st=2
			elif game_mode=="classic":

				dice_2_st=2

				dice_3_st=0
				turn=game1[2]
				main()


				

	root.after(1,two)





st2_=1
m2=0
m_2=0
def move_2():
	global st2,st2_,_st2,val2,val2_,sel_2,m2,m_2,dice_2_st,turn
	global game1,game2
	global game_mode,dice_3_st,winners


	if st2_==0:

		if 0<=val2_<=4:
			game2[sel_2]=[1+m_2,0,game1[1],m_2,val2_,0]

		elif 5<=val2_<=10:

			if val2_==5:
				m_2=0


			game2[sel_2]=[5-m_2,2,game1[2],m_2,val2_,0]


		elif val2_==11:
			game2[sel_2]=[0,1,game1[2],m_2,val2_,0]
		elif 12<=val2_<=17:
			if val2_==12:
				m_2=0

			game2[sel_2]=[m_2,0,game1[2],m_2,val2_,0]
		elif 18<=val2_<=23:
			if val2_==18:
				m_2=0

			game2[sel_2]=[5-m_2,2,game1[3],m_2,val2_,0]
		elif val2_==24:
			game2[sel_2]=[0,1,game1[3],m_2,val2_,0]
		elif 25<=val2_<=30:
			if val2_==25:
				m_2=0

			game2[sel_2]=[m_2,0,game1[3],m_2,val2_,0]

		elif 31<=val2_<=36:
			if val2_==31:
				m_2=0
			game2[sel_2]=[5-m_2,2,game1[0],m_2,val2_,0]
		elif val2_==37:
			game2[sel_2]=[0,1,game1[0],m_2,val2_,0]
		elif 38<=val2_<=43:
			if val2_==38:
				m_2=0

			game2[sel_2]=[m_2,0,game1[0],m_2,val2_,0]


		elif 44<=val2_<=49:
			if val2_==44:
				m_2=0

			game2[sel_2]=[5-m_2,2,game1[1],m_2,val2_,0]
		elif 50<=val2_<= 55:
			if val2_==50:
				m_2=0

			game2[sel_2]=[m_2,1,game1[1],m_2,val2_,0]		
		elif val2_==56:
			game2[sel_2]=[6,1,game1[1],m_2,val2_,0]

		main()


		
		#print(game2[sel_2])
		if m2==val2:

			if game_mode=="rush_mode":
				
				game2[sel_2][-1]=1

				return_home(sel_2)

				dice_2_st=0
			elif game_mode=="classic":
				
				game2[sel_2][-1]=1

				return_home(sel_2)
				if val2==0:
					dice_2_st=0
				else:
					
					dice_2_st=2
					dice_3_st=0
					turn=game1[2]
			main()
			st2_=1

					
						

		m2+=1
		m_2+=1
		val2_+=1




	root.after(100,move_2)



























val3_=0
val3=0
st3=1
sel_3=""
_st3=0


def three():
	global val3,val3_,st3,st3_,_st3,game_mode,game1,game2,sel_3,m3,m_3,turn
	global dice_3_st,dice_4_st

	if st3==0:
		con=0
		col=game1[2]

		h,a=home_and_away(col)

		if len(h)==4 and val3==6:
			con=1
			st3=1
			sel_3=h[random.randint(0,len(h)-1)]

			#print(sel_3)
			val3=0
			val3_=0
			m3=0
			m_3=0
			st3_=0

			
			
		elif len(a)>0:

			if len(h)>0 and val3==6:

				ha=random.randint(0,1)

				if ha==0:
					con=1
					st3=1
					sel_3=h[random.randint(0,len(h)-1)]
					val3=0
					val3_=0
					m3=0
					m_3=0
					st3_=0
					
					
					
				else:
					
					
					sel_3=a[random.randint(0,len(a)-1)]
					val3_=game2[sel_3][-2]


					while 1:


						if val3_+val3>56:

							aa=a.index(sel_3)
							a.pop(aa)


							if len(a)==0:
								con=0
								break

							sel_3=a[random.randint(0,len(a)-1)]
							val3_=game2[sel_3][-2]
						else:


							if game2[sel_3][-1]==0:

								aa=a.index(sel_3)
								a.pop(aa)


								if len(a)==0:
									con=0
									break

								sel_3=a[random.randint(0,len(a)-1)]
								val3_=game2[sel_3][-2]
							else:
								con=1
								st3=1
								m3=0

								m_3=game2[sel_3][-3]
								st3_=0

								break

					if con==0 and len(h)>0:

						con=1
						st3=1
						sel_3=h[random.randint(0,len(h)-1)]
						val3=0
						val3_=0
						m3=0
						m_3=0
						st3_=0






					





					
					
			else:
				sel_3=a[random.randint(0,len(a)-1)]
				val3_=game2[sel_3][-2]


				while 1:





					if val3_+val3>56:

						aa=a.index(sel_3)
						a.pop(aa)

						if len(a)==0:
							con=0
							break



						sel_3=a[random.randint(0,len(a)-1)]
						val3_=game2[sel_3][-2]
					else:

						if game2[sel_3][-1]==0:

							aa=a.index(sel_3)
							a.pop(aa)


							if len(a)==0:
								con=0
								break

							sel_3=a[random.randint(0,len(a)-1)]
							val3_=game2[sel_3][-2]
						else:

							con=1
							st3=1
							m3=0

							m_3=game2[sel_3][-3]
							st3_=0

							break



		if con==0:


			st3=1
			st3_=1
			con2=0

			


			h,a=home_and_away(game1[2])

			if len(h)>0:
				con2=1
			else:
				if len(a)<4:
					con2=1
				elif len(a)==4:
					for _ in range(4):

						


						if game2[game1[2]+"_"+str(_+1)][-2]!=56:


							con2=1

			if game_mode=="rush_mode":

				if con2==1:

					dice_3_st=0
				elif con2==0:
					dice_3_st=2
			elif game_mode=="classic":

				dice_3_st=2

				dice_4_st=0
				turn=game1[3]
				main()


				

	root.after(1,three)





st3_=1
m3=0
m_3=0
def move_3():
	global st3,st3_,_st3,val3,val3_,sel_3,m3,m_3,dice_3_st,turn
	global game1,game2
	global game_mode,dice_4_st,winners



	if st3_==0:

		if 0<=val3_<=4:
			game2[sel_3]=[1+m_3,0,game1[2],m_3,val3_,0]

		elif 5<=val3_<=10:

			if val3_==5:
				m_3=0


			game2[sel_3]=[5-m_3,2,game1[3],m_3,val3_,0]


		elif val3_==11:
			game2[sel_3]=[0,1,game1[3],m_3,val3_,0]
		elif 12<=val3_<=17:
			if val3_==12:
				m_3=0

			game2[sel_3]=[m_3,0,game1[3],m_3,val3_,0]
		elif 18<=val3_<=23:
			if val3_==18:
				m_3=0

			game2[sel_3]=[5-m_3,2,game1[0],m_3,val3_,0]
		elif val3_==24:
			game2[sel_3]=[0,1,game1[0],m_3,val3_,0]
		elif 25<=val3_<=30:
			if val3_==25:
				m_3=0

			game2[sel_3]=[m_3,0,game1[0],m_3,val3_,0]

		elif 31<=val3_<=36:
			if val3_==31:
				m_3=0
			game2[sel_3]=[5-m_3,2,game1[1],m_3,val3_,0]
		elif val3_==37:
			game2[sel_3]=[0,1,game1[1],m_3,val3_,0]
		elif 38<=val3_<=43:
			if val3_==38:
				m_3=0

			game2[sel_3]=[m_3,0,game1[1],m_3,val3_,0]


		elif 44<=val3_<=49:
			if val3_==44:
				m_3=0

			game2[sel_3]=[5-m_3,2,game1[2],m_3,val3_,0]
		elif 50<=val3_<= 55:
			if val3_==50:
				m_3=0

			game2[sel_3]=[m_3,1,game1[2],m_3,val3_,0]		
		elif val3_==56:
			game2[sel_3]=[6,1,game1[2],m_3,val3_,0]

		#print(game2["yellow_4"],dice_3_st)

		main()



		
		#print(game2[sel_3])
		if m3==val3:


			if game_mode=="rush_mode":
				
				game2[sel_3][-1]=1

				return_home(sel_3)

				dice_3_st=0
			elif game_mode=="classic":
				
				game2[sel_3][-1]=1

				return_home(sel_3)
				if val3==0:
					dice_3_st=0
				else:
					
					dice_3_st=2
					dice_4_st=0
					turn=game1[3]
			main()
			st3_=1
						




		

		m3+=1
		m_3+=1
		val3_+=1




	root.after(100,move_3)





















val4_=0
val4=0
st4=1
sel_4=""
_st4=0


def four():
	global val4,val4_,st4,st4_,_st4,game_mode,game1,game2,sel_4,m4,m_4,turn
	global dice_4_st,dice_1_st

	if st4==0:
		con=0
		col=game1[3]

		h,a=home_and_away(col)

		if len(h)==4 and val4==6:
			con=1
			st4=1
			sel_4=h[random.randint(0,len(h)-1)]

			#print(sel_4)
			val4=0
			val4_=0
			m4=0
			m_4=0
			st4_=0

			
			
		elif len(a)>0:

			if len(h)>0 and val4==6:

				ha=random.randint(0,1)

				if ha==0:
					con=1
					st4=1
					sel_4=h[random.randint(0,len(h)-1)]
					val4=0
					val4_=0
					m4=0
					m_4=0
					st4_=0
					
					
					
				else:
					
					
					sel_4=a[random.randint(0,len(a)-1)]
					val4_=game2[sel_4][-2]


					while 1:


						if val4_+val4>56:

							aa=a.index(sel_4)
							a.pop(aa)


							if len(a)==0:
								con=0
								break

							sel_4=a[random.randint(0,len(a)-1)]
							val4_=game2[sel_4][-2]
						else:
							if game2[sel_4][-1]==0:

								aa=a.index(sel_4)
								a.pop(aa)


								if len(a)==0:
									con=0
									break

								sel_4=a[random.randint(0,len(a)-1)]
								val4_=game2[sel_4][-2]
							else:
								con=1
								st4=1
								m4=0

								m_4=game2[sel_4][-3]
								st4_=0

								break

					if con==0 and len(h)>0:

						con=1
						st4=1
						sel_4=h[random.randint(0,len(h)-1)]
						val4=0
						val4_=0
						m4=0
						m_4=0
						st4_=0






					





					
					
			else:
				sel_4=a[random.randint(0,len(a)-1)]
				val4_=game2[sel_4][-2]


				while 1:





					if val4_+val4>56:

						aa=a.index(sel_4)
						a.pop(aa)

						if len(a)==0:
							con=0
							break



						sel_4=a[random.randint(0,len(a)-1)]
						val4_=game2[sel_4][-2]
					else:
						if game2[sel_4][-1]==0:

							aa=a.index(sel_4)
							a.pop(aa)


							if len(a)==0:
								con=0
								break

							sel_4=a[random.randint(0,len(a)-1)]
							val4_=game2[sel_4][-2]
						else:
							con=1
							st4=1
							m4=0

							m_4=game2[sel_4][-3]
							st4_=0

							break



		if con==0:


			st4=1
			st4_=1
			con2=0

			


			h,a=home_and_away(game1[3])

			if len(h)>0:
				con2=1
			else:
				if len(a)<4:
					con2=1
				elif len(a)==4:
					for _ in range(4):

						


						if game2[game1[3]+"_"+str(_+1)][-2]!=56:


							con2=1

			if game_mode=="rush_mode":

				if con2==1:

					dice_4_st=0
				elif con2==0:
					dice_4_st=2
			elif game_mode=="classic":

				dice_4_st=2

				dice_1_st=0
				turn=game1[0]
				main()

				

	root.after(1,four)





st4_=1
m4=0
m_4=0
def move_4():
	global st4,st4_,_st4,val4,val4_,sel_4,m4,m_4,dice_4_st,turn
	global game1,game2
	global game_mode,dice_1_st,winners


	if st4_==0:

		if 0<=val4_<=4:
			game2[sel_4]=[1+m_4,0,game1[3],m_4,val4_,0]

		elif 5<=val4_<=10:

			if val4_==5:
				m_4=0


			game2[sel_4]=[5-m_4,2,game1[0],m_4,val4_,0]


		elif val4_==11:
			game2[sel_4]=[0,1,game1[0],m_4,val4_,0]
		elif 12<=val4_<=17:
			if val4_==12:
				m_4=0

			game2[sel_4]=[m_4,0,game1[0],m_4,val4_,0]
		elif 18<=val4_<=23:
			if val4_==18:
				m_4=0

			game2[sel_4]=[5-m_4,2,game1[1],m_4,val4_,0]
		elif val4_==24:
			game2[sel_4]=[0,1,game1[1],m_4,val4_,0]
		elif 25<=val4_<=30:
			if val4_==25:
				m_4=0

			game2[sel_4]=[m_4,0,game1[1],m_4,val4_,0]

		elif 31<=val4_<=36:
			if val4_==31:
				m_4=0
			game2[sel_4]=[5-m_4,2,game1[2],m_4,val4_,0]
		elif val4_==37:
			game2[sel_4]=[0,1,game1[2],m_4,val4_,0]
		elif 38<=val4_<=43:
			if val4_==38:
				m_4=0

			game2[sel_4]=[m_4,0,game1[2],m_4,val4_,0]


		elif 44<=val4_<=49:
			if val4_==44:
				m_4=0

			game2[sel_4]=[5-m_4,2,game1[3],m_4,val4_,0]
		elif 50<=val4_<= 55:
			if val4_==50:
				m_4=0

			game2[sel_4]=[m_4,1,game1[3],m_4,val4_,0]		
		elif val4_==56:
			game2[sel_4]=[6,1,game1[3],m_4,val4_,0]

		main()


		
		#print(game2[sel_4])
		if m4==val4:
			if game_mode=="rush_mode":
				
				game2[sel_4][-1]=1

				return_home(sel_4)

				dice_4_st=0
			elif game_mode=="classic":
				
				game2[sel_4][-1]=1

				return_home(sel_4)
				if val4==0:
					dice_4_st=0
				else:
					dice_4_st=2
					dice_1_st=0
					turn=game1[0]
			main()
			st4_=1
						

		

		m4+=1
		m_4+=1
		val4_+=1




	root.after(100,move_4)





dd1=0
def _dice_1():
	global dice_1,dice_1_st,dd1,val1,st1,turn
	global game1,game_mode,dice_2_st



	if dice_1_st==0:
		v=det(game1[0])

		if v==0:
			dice_1_st=2
			if game_mode=="classic":
				dice_2_st=0
				turn=game1[1]
				main()

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
	elif dice_1_st==2:
		dice_1.delete("all")



		dice_1.create_arc(0,0,20,20,start=90,extent=90,style="arc",outline="#000000",width=2)
		dice_1.create_arc(50-21,0,50-1,20,start=0,extent=90,style="arc",outline="#000000",width=2)
		dice_1.create_arc(0,50-21,20,50-1,start=180,extent=90,style="arc",outline="#000000",width=2)
		dice_1.create_arc(50-21,50-21,50-1,50-1,start=270,extent=90,style="arc",outline="#000000",width=2)

		dice_1.create_line(10,1, 40,1,fill="#000000",width=2)
		dice_1.create_line(10,49, 40,49,fill="#000000",width=2)
		dice_1.create_line(1,10,1,40,fill="#000000",width=2)
		dice_1.create_line(49,10,49,40,fill="#000000",width=2)

		dice_1_st=1



	root.after(50,_dice_1)



dd2=0
def _dice_2():
	global dice_2,dice_2_st,dd2,val2,st2,turn

	global game1,game_mode,dice_3_st



	if dice_2_st==0:
		v=det(game1[1])

		if v==0:
			dice_2_st=2
			if game_mode=="classic":
				dice_3_st=0
				turn=game1[2]
				main()






	if dice_2_st==0:

		v=random.randint(1,6)

		_dice_(dice_2,v)

		dd2+=1

		if dd2==10:
			dd2=0
			dice_2_st=1
			val2=v
			st2=0

	elif dice_2_st==2:
		dice_2.delete("all")



		dice_2.create_arc(0,0,20,20,start=90,extent=90,style="arc",outline="#000000",width=2)
		dice_2.create_arc(50-21,0,50-1,20,start=0,extent=90,style="arc",outline="#000000",width=2)
		dice_2.create_arc(0,50-21,20,50-1,start=180,extent=90,style="arc",outline="#000000",width=2)
		dice_2.create_arc(50-21,50-21,50-1,50-1,start=270,extent=90,style="arc",outline="#000000",width=2)

		dice_2.create_line(10,1, 40,1,fill="#000000",width=2)
		dice_2.create_line(10,49, 40,49,fill="#000000",width=2)
		dice_2.create_line(1,10,1,40,fill="#000000",width=2)
		dice_2.create_line(49,10,49,40,fill="#000000",width=2)

		dice_2_st=1


	root.after(50,_dice_2)


dd3=0
def _dice_3():
	global dice_3,dice_3_st,dd3,val3,st3,turn
	global game1,game_mode,dice_4_st



	if dice_3_st==0:
		v=det(game1[2])

		if v==0:
			dice_3_st=2
			if game_mode=="classic":
				dice_4_st=0
				turn=game1[3]
				main()


	if dice_3_st==0:

		v=random.randint(1,6)

		_dice_(dice_3,v)

		dd3+=1

		if dd3==10:
			dd3=0
			dice_3_st=1
			val3=v
			st3=0

	elif dice_3_st==2:
		dice_3.delete("all")



		dice_3.create_arc(0,0,20,20,start=90,extent=90,style="arc",outline="#000000",width=2)
		dice_3.create_arc(50-21,0,50-1,20,start=0,extent=90,style="arc",outline="#000000",width=2)
		dice_3.create_arc(0,50-21,20,50-1,start=180,extent=90,style="arc",outline="#000000",width=2)
		dice_3.create_arc(50-21,50-21,50-1,50-1,start=270,extent=90,style="arc",outline="#000000",width=2)

		dice_3.create_line(10,1, 40,1,fill="#000000",width=2)
		dice_3.create_line(10,49, 40,49,fill="#000000",width=2)
		dice_3.create_line(1,10,1,40,fill="#000000",width=2)
		dice_3.create_line(49,10,49,40,fill="#000000",width=2)

		dice_3_st=1



	root.after(50,_dice_3)


dd4=0
def _dice_4():
	global dice_4,dice_4_st,dd4,val4,st4,turn
	global game1,game_mode,dice_1_st



	if dice_4_st==0:
		v=det(game1[3])

		if v==0:
			dice_4_st=2
			if game_mode=="classic":
				dice_1_st=0
				turn=game1[0]
				main()


	if dice_4_st==0:

		v=random.randint(1,6)

		_dice_(dice_4,v)

		dd4+=1

		if dd4==10:
			dd4=0
			dice_4_st=1
			val4=v
			st4=0


	elif dice_4_st==2:
		dice_4.delete("all")



		dice_4.create_arc(0,0,20,20,start=90,extent=90,style="arc",outline="#000000",width=2)
		dice_4.create_arc(50-21,0,50-1,20,start=0,extent=90,style="arc",outline="#000000",width=2)
		dice_4.create_arc(0,50-21,20,50-1,start=180,extent=90,style="arc",outline="#000000",width=2)
		dice_4.create_arc(50-21,50-21,50-1,50-1,start=270,extent=90,style="arc",outline="#000000",width=2)

		dice_4.create_line(10,1, 40,1,fill="#000000",width=2)
		dice_4.create_line(10,49, 40,49,fill="#000000",width=2)
		dice_4.create_line(1,10,1,40,fill="#000000",width=2)
		dice_4.create_line(49,10,49,40,fill="#000000",width=2)

		dice_4_st=1



	root.after(50,_dice_4)



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





def arrows():
	global a1,a2,a3,a4,game1


	arrow=Image.open("data/"+str(game1[0][0])+".png")

	a=arrow.rotate(90)
	a=a.resize((int(s*3/4),int(s*3/4)))
	a.save("data/"+game1[0][0]+"1.png")



	a1=ImageTk.PhotoImage(file="data/"+game1[0][0]+"1.png")




	arrow=Image.open("data/"+str(game1[1][0])+".png")

	#a=arrow.rotate(90)
	a=arrow.resize((int(s*3/4),int(s*3/4)))
	a.save("data/"+game1[1][0]+"1.png")



	a2=ImageTk.PhotoImage(file="data/"+game1[1][0]+"1.png")



	arrow=Image.open("data/"+str(game1[2][0])+".png")

	a=arrow.rotate(270)
	a=a.resize((int(s*3/4),int(s*3/4)))
	a.save("data/"+game1[2][0]+"1.png")



	a3=ImageTk.PhotoImage(file="data/"+game1[2][0]+"1.png")




	arrow=Image.open("data/"+str(game1[3][0])+".png")

	a=arrow.rotate(180)
	a=a.resize((int(s*3/4),int(s*3/4)))
	a.save("data/"+game1[3][0]+"1.png")



	a4=ImageTk.PhotoImage(file="data/"+game1[3][0]+"1.png")	

def draw_bg():
	global game1,game2,s,can,wd,st_,turn,game_mode

	global a1,a2,a3,a4

	global state,quit,winners,crown



	st=Image.open("data/star.png")
	st=st.resize((int(s*3/4),int(s*3/4)))
	st.save("data/st.png")

	st_=ImageTk.PhotoImage(file="data/st.png")
	can.delete("all")


	state="game"


	quit=ImageTk.PhotoImage(file="data/quit.png")


	can.create_image(wd-10-30,10,image=quit,anchor="nw")

	can.create_text(70,530,text="User",font=("FreeMono",15),anchor="w")



	conv=0

	if det(game1[0])==0 and det(game1[1])==0 and det(game1[2])==0 and det(game1[3])==0:
		conv=1

	if game_mode=="classic" and conv==0:


		can.create_text(10,570,text="Turn",font=("FreeMono",15),anchor="w")

		can.create_rectangle(100-30-10,570-10, 130-30-10-10,570+10,fill=turn,outline="#000000")

	crown=ImageTk.PhotoImage(file="data/crown.png")

	for winner in range(len(winners)):

		wv=game1.index(winners[winner])

		if wv==0:

			x=10
			y=590-70-50-30-50

			can.create_image(x,y,image=crown,anchor="nw")

			can.create_text(35,y+60,text=str(winner+1),font=("FreeMono",15,"bold"))
		elif wv==3:
			x=590-60
			y=590-70-50-30-50

			can.create_image(x,y,image=crown,anchor="nw")

			can.create_text(590-35,y+60,text=str(winner+1),font=("FreeMono",15,"bold"))


		elif wv==1:

			x=10
			y=70+50+10

			can.create_image(x,y,image=crown,anchor="nw")

			can.create_text(35,y+60,text=str(winner+1),font=("FreeMono",15,"bold"))
		elif wv==2:
			x=590-60
			y=70+50+10

			can.create_image(x,y,image=crown,anchor="nw")

			can.create_text(590-35,y+60,text=str(winner+1),font=("FreeMono",15,"bold"))



	x,y=70,70
	

	#can.create_rectangle(x,y, x+s*15,y+s*15,outline="#000000")

	#can.create_rectangle(x,y+s*9,x+s*6,y+s*15,fill=game1[0],outline="#000000")
	can.create_oval(x+s,y+s*10,x+s*5,y+s*14,fill=game1[0],outline="#000000")



	d=(s*4-2*s)/3

	x_,y_=x+s,y+s*10

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill="#ffffff",outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill="#ffffff",outline="#000000")


	#can.create_rectangle(x,y,x+s*6,y+s*6,fill=game1[1],outline="#000000")
	can.create_oval(x+s,y+s,x+s*5,y+s*5,fill=game1[1],outline="#000000")

	x_,y_=x+s,y+s

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill="#ffffff",outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill="#ffffff",outline="#000000")


	
	#can.create_rectangle(x+s*9,y,x+s*15,y+s*6,fill=game1[2],outline="#000000")
	can.create_oval(x+s*10,y+s,x+s*14,y+s*5,fill=game1[2],outline="#000000")

	x_,y_=x+s*10,y+s

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill="#ffffff",outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill="#ffffff",outline="#000000")





	#can.create_rectangle(x+s*9,y+s*9,x+s*15,y+s*15,fill=game1[3],outline="#000000")
	can.create_oval(x+s*10,y+s*10,x+s*14,y+s*14,fill=game1[3],outline="#000000")


	x_,y_=x+s*10,y+s*10

	can.create_oval(x_+d,y_+d, x_+d+s,y_+d+s, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d, x_+d*2+s*2,y_+d+s, fill="#ffffff",outline="#000000")

	can.create_oval(x_+d,y_+d*2+s, x_+d+s,y_+d*2+s*2, fill="#ffffff",outline="#000000")
	can.create_oval(x_+d*2+s,y_+d*2+s, x_+d*2+s*2,y_+d*2+s*2, fill="#ffffff",outline="#000000")






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
		col=i.split("_")[0]
		if len(game2[i])==2:

			pass
		else:

			con=0

			for a in ar:

				if a[0]==game2[i][:3]:
					a[1].append(col)
					con=1
					break


			if con==0:

				ar.append([game2[i][:3],[col]])



	for i in game2:
		col=i.split("_")[0]


		if len(game2[i])==2:
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



	for i in ar:

		xx=i[0][0]
		yy=i[0][1]

		p=game1.index(i[0][2])

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





		if len(i[1])==1:

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

			


			draw_pointer(_xx,_yy,25,i[1][0])

		elif len(i[1])==2:



			if v=="b":

				_xx1=x_+yy*s+s/4
				_yy1=y_-xx*s-s/2

				_xx2=x_+yy*s+s*3/4
				_yy2=y_-xx*s-s/2
			elif v=="l":

				_xx1=x_+xx*s+s/4
				_yy1=y_+yy*s+s/2


				_xx2=x_+xx*s+s*3/4
				_yy2=y_+yy*s+s/2


			elif v=="t":

				_xx1=x_-yy*s-s/4
				_yy1=y_+xx*s+s/2

				_xx2=x_-yy*s-s*3/4
				_yy2=y_+xx*s+s/2

			elif v=="r":

				_xx1=x_-xx*s-s/4
				_yy1=y_-yy*s-s/2

				_xx2=x_-xx*s-s*3/4
				_yy2=y_-yy*s-s/2
			


			draw_pointer(_xx1,_yy1,23,i[1][0])
			draw_pointer(_xx2,_yy2,23,i[1][1])




		elif len(i[1])==3:



			if v=="b":

				_xx1=x_+yy*s+s/4
				_yy1=y_-xx*s-s/2

				_xx2=x_+yy*s+s*3/4
				_yy2=y_-xx*s-s/2

				_xx3=x_+yy*s+s/2
				_yy3=y_-xx*s-s/2


			elif v=="l":

				_xx1=x_+xx*s+s/4
				_yy1=y_+yy*s+s/2

				_xx2=x_+xx*s+s*3/4
				_yy2=y_+yy*s+s/2

				_xx3=x_+xx*s+s/2
				_yy3=y_+yy*s+s/2

			elif v=="t":

				_xx1=x_-yy*s-s/4
				_yy1=y_+xx*s+s/2

				_xx2=x_-yy*s-s*3/4
				_yy2=y_+xx*s+s/2

				_xx3=x_-yy*s-s/2
				_yy3=y_+xx*s+s/2


			elif v=="r":

				_xx1=x_-xx*s-s/4
				_yy1=y_-yy*s-s/2

				_xx2=x_-xx*s-s*3/4
				_yy2=y_-yy*s-s/2
			
				_xx3=x_-xx*s-s/2
				_yy3=y_-yy*s-s/2

			draw_pointer(_xx1,_yy1,20,i[1][0])
			draw_pointer(_xx2,_yy2,20,i[1][1])
			draw_pointer(_xx3,_yy3,20,i[1][2])



		elif len(i[1])>=4:



			if v=="b":

				_xx1=x_+yy*s+s/4
				_yy1=y_-xx*s-s*3/4

				_xx2=x_+yy*s+s*3/4
				_yy2=y_-xx*s-s*3/4



				_xx3=x_+yy*s+s/4
				_yy3=y_-xx*s-s/4

				_xx4=x_+yy*s+s*3/4
				_yy4=y_-xx*s-s/4


			elif v=="l":

				_xx1=x_+xx*s+s/4
				_yy1=y_+yy*s+s/4


				_xx2=x_+xx*s+s*3/4
				_yy2=y_+yy*s+s/4


				_xx3=x_+xx*s+s/4
				_yy3=y_+yy*s+s*3/4


				_xx4=x_+xx*s+s*3/4
				_yy4=y_+yy*s+s*3/4

			elif v=="t":

				_xx1=x_-yy*s-s/4
				_yy1=y_+xx*s+s/4

				_xx2=x_-yy*s-s*3/4
				_yy2=y_+xx*s+s/4

				_xx3=x_-yy*s-s/4
				_yy3=y_+xx*s+s*3/4

				_xx4=x_-yy*s-s*3/4
				_yy4=y_+xx*s+s*3/4


			elif v=="r":

				_xx1=x_-xx*s-s/4
				_yy1=y_-yy*s-s*3/4

				_xx2=x_-xx*s-s*3/4
				_yy2=y_-yy*s-s*3/4
			
				_xx3=x_-xx*s-s/4
				_yy3=y_-yy*s-s/4

				_xx4=x_-xx*s-s*3/4
				_yy4=y_-yy*s-s/4

			draw_pointer(_xx1,_yy1,20,i[1][0])
			draw_pointer(_xx2,_yy2,20,i[1][1])
			draw_pointer(_xx3,_yy3,20,i[1][2])
			draw_pointer(_xx4,_yy4,20,i[1][3])














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






val1_=0
val1=0
st1=1
sel_1=""
_st1=0


def can_commands(e):
	global state,game_mode,game1,game2,turn
	global wd,ht,choice,sx
	global dice_1_st,dice_2_st,dice_3_st,dice_4_st
	global dice_1,dice_2,dice_3,dice_4
	global st1,st2,st3,st4
	global st1_,st2_,st3_,st4_
	global sel_1
	global val1,val1_,m_1,m1,winners
	global ones_,twos_,threes_,fours_

	if state=="game":
		cx=wd-10-15
		cy=10+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)
		if r<=15:
			choice=""
			game1=["red","green","yellow","blue"]



			dice_1.place_forget()
			dice_2.place_forget()	
			dice_3.place_forget()
			dice_4.place_forget()




			sel_game_mode()			

		if st1==0:

			con=0


			pos=0

			d=s*2/3


			cx,cy=70+30+d+15, 70+30*9+30+d+15

			r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2)

			if r<=15:
				con=1
				pos=game1[0][0]+"1"


			cx,cy=70+30*2+d*2+15,70+30*9+30+d+15


			r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2)

			if r<=15:
				con=1
				pos=game1[0][0]+"2"

			cx,cy=70+30+d+15,70+30*9+30+d+15+d+30

			r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2)

			if r<=15:
				con=1
				pos=game1[0][0]+"3"


			cx,cy=70+30*2+d*2+15,70+30*9+30+d+15+d+30

			r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2)

			if r<=15:
				con=1
				pos=game1[0][0]+"4"




			if 70+30*6<=e.x<=70+30*9:
				if 70+30*9<=e.y<=70+30*15:
					con=1
					col=game1[0]

					x=int((e.y-(70+30*9))/30)-5

					if x<0:
						x=-x

					y=int((e.x-(70+30*6))/30)


					pos=[x,y,col]

			if 70<=e.x<=70+30*6:
				if 70+30*6<=e.y<=70+30*9:
					con=1
					col=game1[1]

					x=int((e.x-70)/30)

					y=int((e.y-(70+30*6))/30)

					pos=[x,y,col]
			if 70+30*6<=e.x<=70+30*9:
				if 70<=e.y<=70+30*6:
					con=1

					col=game1[2]

					x=int((e.y-70)/30)

					y=int((e.x-(70+30*6))/30)-2

					if y<0:
						y=-y

					pos=[x,y,col]
			if 70+30*9<=e.x<=70+30*15:
				if 70+30*6<=e.y<=70+30*9:
					con=1


					col=game1[3]

					x=int((e.x-(70+30*9))/30)-5

					y=int((e.y-(70+30*6))/30)-2

					if x<0:
						x=-x

					if y<0:
						y=-y

					pos=[x,y,col]



			def get_pwp(p):

				global game2

				ar=[]

				for i in game2:

					p2=game2[i]




					if p2[:3]==p:

						if i.split("_")[0]==game1[0]:


							ar.append(i)


				return ar


			if con==1:



				h,a=home_and_away(game1[0])

				if len(h)==4 and val1==6:

					if pos[0]==game1[0][0]:

						sel_1=get_pwp(pos)[0]
						val1=0
						val1_=0
						m1=0
						m_1=0
						st1_=0
						st1=1

				elif len(a)>0:

					if pos[0]==game1[0][0] and len(h)>0 and val1==6:

						sel_1=get_pwp(pos)[0]
						val1=0
						val1_=0
						m1=0
						m_1=0
						st1_=0
						st1=1

					else:
						a_=get_pwp(pos)

						l=len(a_)

						l-=1

						sel_1=a_[random.randint(0,l)]


						val1_=game2[sel_1][-2]


						if val1_+val1<=56:
							m1=0
							m_1=game2[sel_1][-3]
							st1_=0

							st1=1




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
					"""
				
					game2={"red_1":[6,1,"red",6,56,1],
							"red_2":[6,1,"red",6,56,1],
							"red_3":[6,1,"red",6,56,1],
							"red_4":[6,1,"red",6,56,1],

							"green_1":[6,1,"green",6,56,1],
							"green_2":[6,1,"green",6,56,1],
							"green_3":[6,1,"green",6,56,1],
							"green_4":[6,1,"green",6,56,1],		

							"yellow_1":[6,1,"yellow",6,56,1],
							"yellow_2":[6,1,"yellow",6,56,1],
							"yellow_3":[6,1,"yellow",6,56,1],
							"yellow_4":[6,1,"yellow",6,56,1],

							"blue_1":[5,1,"blue",5,55,1],
							"blue_2":[6,1,"blue",6,56,1],
							"blue_3":[6,1,"blue",6,56,1],
							"blue_4":[6,1,"blue",6,56,1],

					}

					"""

						
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
					winners=[]#"red","yellow","green"]
					#twos_=[["red_1",0]]
					dice_1_st=1
					dice_2_st=1
					dice_3_st=1
					dice_4_st=1

					st1=1
					st2=1
					st3=1
					st4=1


					st1_=1
					st2_=1
					st3_=1
					st4_=1
					

					dice_1.delete("all")
					dice_2.delete("all")
					dice_3.delete("all")
					dice_4.delete("all")

					shift(choice)
					arrows()
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
						dice_2_st=2
						dice_3_st=2
						dice_4_st=2

						turn=game1[0]
						main()



					return

			cx=195+15
			cy=510+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:
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

				winners=[]
				dice_1_st=1
				dice_2_st=1
				dice_3_st=1
				dice_4_st=1

				st1=1
				st2=1
				st3=1
				st4=1


				st1_=1
				st2_=1
				st3_=1
				st4_=1
				

				dice_1.delete("all")
				dice_2.delete("all")
				dice_3.delete("all")
				dice_4.delete("all")



				shift(choice)
				arrows()
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
					dice_2_st=2
					dice_3_st=2
					dice_4_st=2					
					turn=game1[0]
					main()
				return

			cx=395-15
			cy=510+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:


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

				winners=[]
				dice_1_st=1
				dice_2_st=1
				dice_3_st=1
				dice_4_st=1

				st1=1
				st2=1
				st3=1
				st4=1


				st1_=1
				st2_=1
				st3_=1
				st4_=1
				

				dice_1.delete("all")
				dice_2.delete("all")
				dice_3.delete("all")
				dice_4.delete("all")


				shift(choice)
				arrows()
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
					dice_2_st=2
					dice_3_st=2
					dice_4_st=2

					turn=game1[0]
					main()
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


winners=[]
crown=""

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
dice_1_st=2

dice_2=tk.Canvas(width=50,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
dice_2_st=2

dice_3=tk.Canvas(width=50,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
dice_3_st=2

dice_4=tk.Canvas(width=50,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
dice_4_st=2

#error_()


_dice_1()
_dice_2()
_dice_3()
_dice_4()


one()
move_1()

two()
move_2()


three()
move_3()



four()
move_4()

main()
sel_game_mode()

wins()

return_home_1()
return_home_2()
return_home_3()
return_home_4()
root.mainloop()