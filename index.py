"""Michael Wright """
import sys

option = sys.argv[1].lower()

urName = "My user's name is Michael Wright.\nHe is currently a senior."
qWhy = "You want to know why he chose CS?\nHe was a gamer growing up and he wanted to give back to the Gaming Industry by helping create games for future generations."
qWhat = "Upon graduation, he plans to take on Programmer/Software Engineering jobs and interships to gain experience in the industry.\nWith luck, he ultimately hopes to obtain enough experience to work in the Gaming Industry, or programming Artificial Intelligence."
funFact = "You really want a fun fact about him?\nAre you sure that's what you want?\nWell, he was voted most likely to become a hoarder back during his senior year of high school.\nI, like many who knows him, still believe that he should have been voted most likely to start a revelution."
additionHomework = "Michael managed to install the desktop version of GitHub on his laptop as a temporary fix to the command prompt problem.\nSure, he may still have to override the dubious ownership bs,\nbut he believes that it might be due to the file path leading to a removeable drive that is shared between his laptop and desktop."
whoAmI = "I am Maxim.\nThe rest is unimportant for now."
elseStatement = 'You have entered an incorrect option. The only correct options are "/name", "/why", "/what", "/fact" "/additional_homework", and "/who_r_u".\nI know the remaining two are outside of the parameters of the assignment,\nbut my user believed them necessary.'

if option == "/name":
	print(urName)
elif option == "/why":
	print(qWhy)
elif option == "/what":
	print(qWhat)
elif option == "/fact":
	print(funFact)
elif option == "/additional_homework":
	print(additionHomework)
elif option == "/who_r_u" :
	print(whoAmI)
else :
	print(elseStatement)