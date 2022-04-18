from tkinter import *
import random
import os
from random import randint
from PIL import ImageTk, Image
from selenium import webdriver
from io import BytesIO
from termcolor import colored
# import requests
import cfscrape
# Set environment variable
TK_SILENCE_DEPRECATION = 1

# generate a string of 2 random letters
letters = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=2))

# generate 4 random numbers & convert them to string
numbers = "".join([str(randint(0, 9)) for n in range(4)])

# url + urlcode
url = "https://prnt.sc/"+(letters+numbers)

# webscrape driver


class By:
    ID = "id"


print(colored("[!] Loading Driver...", 'cyan'))
os.environ['MOZ_HEADLESS'] = '1'
driver = webdriver.Firefox()
print(colored("[SUCCESS] Loaded Driver.", 'green'))
print(colored("[!] Loading URL... This may take a while depending on internet connection speeds.", 'cyan'))
driver.get(url)
print(colored("[SUCCESS] URL Loaded.", 'green'))
# element = (driver.find_element_by_id('screenshot-image').get_attribute("src"))
print(colored("[!] Injecting into element...", 'cyan'))
element = (driver.find_element(By.ID, 'screenshot-image').get_attribute("src"))
img_url = element
print(colored("[SUCCESS] Injected into element.", 'green'))
print(colored("[!] Scarping image...", 'cyan'))
scraper = cfscrape.create_scraper()
img_data = scraper.get(img_url).content
print(colored("[SUCCESS] Image Scraped: ", 'green'))
print(img_url)
# quit after loading
# driver.quit()

print(colored("[!] Loading GUI Window...", 'cyan'))
# -----GUI Window----800x600-----
window = Tk()
# add widgets here
my_img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
my_label = Label(image=my_img)
my_label.pack()

# Generate new image button
btn = Button(window, text="Find New Image", fg='blue')
btn.place(x=80, y=500)

# Save image button
btn = Button(window, text="Save Image", fg='blue')
btn.place(x=600, y=500)

# Show URL label
lbl = Label(window, text=url, fg='red', font=("Helvetica", 16))
lbl.place(x=330, y=503)

# -----Window configuration-----
window.title('Screenshot Finder')
window.geometry("1920x1080+10+20")
window.mainloop()
print(colored("[SUCCESS] GUI Window Loaded.", 'green'))
# quit Firefox driver running in the background
print(colored("[!] Stopping driver to save memory...", 'cyan'))
driver.quit()
print(colored("[SUCCESS] Driver stopped.", 'green'))
