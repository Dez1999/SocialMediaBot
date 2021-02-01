#Python GUI for Social Media Automation Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys		#Allows us to interact with the keys and elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from PIL import ImageTk
import time
import tkinter as GUI
import tkinter as tk  #GUI interface

#Closes the application
def close_app():
	window.destroy()

def reset_Buttons():
	label["text"] = "Posted to: " + "... (Buttons Reset)"
	button_twitter.config(state=GUI.NORMAL, borderwidth=0)
	button_Discord.config(state=GUI.NORMAL, borderwidth=0)
	button_All.config(state=GUI.NORMAL, borderwidth=2)


def tweet_Bot():
	print('Its tweeting')
	label["text"] = "Posted to: " + "Twitter"
	button_twitter.config(state=GUI.DISABLED, borderwidth=4)
	button_All.config(state=GUI.DISABLED, borderwidth=4)

	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH)   #Always start with this and choose the browser you want to use
	driver.get("https://twitter.com/login")   #Choose a specific website to open up

	#Message to tweet ******THIS NEEDS TO CHANGED CONSTANTLY/RANDOMLY
	tweet = "We LIVING! #goingLive "

	####Interact with the webpage
	print(driver.title)  #Prints the title of the website

	time.sleep(2)
	usr_box = driver.find_element_by_name("session[username_or_email]")
	usr_box.send_keys("userName")     


	pwd_box = driver.find_element_by_name("session[password]")
	pwd_box.send_keys("password")

	time.sleep(2)
	pwd_box.send_keys(Keys.RETURN)

	time.sleep(2)

	#Click Home-Page Tweet Button
	home_tweetButton_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'

	button_tweet1 = driver.find_element_by_xpath(home_tweetButton_xpath)
	button_tweet1.click()


	#NOTE: To get CSS selector code you inspect the input box and then inspect it again -> then copy selector code
	tweet_box = driver.find_element_by_css_selector("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-rsyp9y.r-1pjcn9w.r-htvplk.r-1udh08x.r-1potc6q > div > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(1) > div > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > div.css-901oao.r-18jsvk2.r-6koalj.r-16y2uox.r-1qd0xha.r-1b6yd1w.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
	#Home Page of Twitter
	#tweet_box = driver.find_element_by_name("")
	tweet_box.send_keys(tweet)



	time.sleep(3)

	tweet_button_Xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span'

	tweet_button = driver.find_element_by_xpath(tweet_button_Xpath)  #Got this by searching for button in inspect and then getting selector code/xpath
	tweet_button.click()

	print("Done")
	driver.quit()
	

#Function to post for Discord Bot
def discord_Bot():
	print('Posted to Discord')
	label["text"] = "Posted to: " + "Discord"
	button_Discord.config(state=GUI.DISABLED, borderwidth=4)
	button_All.config(state=GUI.DISABLED, borderwidth=4)

#Function to post on all platforms
def Allplatforms_Bot():
	print('Posted to All Platforms')
	tweet_Bot()
	discord_Bot()
	label["text"] = "Posted to: " + "All Platforms"



#Everything must be inside the window variables
window = tk.Tk()

window.title("Going Live Bot")
window.geometry("400x300")
window.resizable("false", "false")

#Frames on GUI
frame_header = tk.Frame(master = window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)

#Grid placement of frames
frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

#Header frame style
header = tk.Label(frame_header, text = "Going Live Bot", bg='red', fg='black', height ='3', width= '30', 
	font = ("Helvetica 16 bold"))
header.grid(row=0,column=0)

#Twitter Image
#img_twitterLogo = tk.PhotoImage(file = "C:\\Users\\Blake\\Desktop\\Python_files\\images\\Twitter_logo.jpg")
image = Image.open("C:\\Users\\Twitter_logo.jpg")
image = image.resize((170, 170))
img_twitterLogo = ImageTk.PhotoImage(image)

#Discord Image
image2 = Image.open("C:\\Users\\Discord_logo.jpg")
image2 = image2.resize((170, 200))
img_discordLogo = ImageTk.PhotoImage(image2)

#Twitter Button
button_twitter = tk.Button(center_frame, image = img_twitterLogo, command=tweet_Bot, bg ='blue', fg='white', relief='raised', height = 95, width=100, borderwidth=0, font=('Helvetica 12 bold'))
button_twitter.grid(column=0, row=0, sticky='w', padx=10, pady=2)

#Discord Button
button_Discord = tk.Button(center_frame, image = img_discordLogo, command=discord_Bot, bg ='light blue', fg='black', relief='raised', height = 95, width=100, borderwidth=0, font=('Helvetica 12 bold'))
button_Discord.grid(column=2, row=0, sticky='w', padx=10, pady=2)

#All Platforms(Buttons)
button_All = tk.Button(center_frame, text ="All Platforms", command=Allplatforms_Bot, bg ='lime', fg='black', relief='raised', height = 5, width=10, font=('Helvetica 12 bold'))
button_All.grid(column=1, row=0, sticky='w', padx=10, pady=2)

#Reset Button
button_Reset = tk.Button(bottom_frame, text ="Reset", command=reset_Buttons, bg ='red', fg='black', relief='raised', height = 1, width=5, font=('Helvetica 12 bold'))
button_Reset.grid(column=0, row=0, sticky='w', padx=10, pady=2)

#Exit Button
#button_close = tk.Button(bottom_frame, text= "Exit", command=close_app, bg='dark red', fg ='white', relief='raised', width=10, font=('Helvetica 12 bold'))
#button_close .grid(column=0, row=0, sticky='e', padx=100, pady=2)

#Label
label = tk.Label(bottom_frame, text ='Posted to: ...', font=("Courier bold", 15))
label.grid(row=0, column=1, sticky ='w', pady=10)

window.mainloop()

