import selenium
from selenium import webdriver
import urllib.request
import time

browser = webdriver.Firefox()

browser.get("https://www.google.com/search?q=kalem&tbm=isch&ved=2ahUKEwiXzLXIo6n7AhWhif0HHSHhAx8Q2-cCegQIABAA&oq=kalem&gs_lcp=CgNpbWcQAzIHCAAQsQMQQzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMgUIABCABDILCAAQgAQQsQMQgwEyCAgAEIAEELEDMgQIABBDUNMNWPgRYLkXaABwAHgAgAGxAYgBjAaSAQMwLjaYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=pOZvY5fqBaGT9u8PocKP-AE&bih=629&biw=1366")
"""
browser.get('https://www.youtube.com/playlist?list=PL33a8qXOY4kdTEoffAN8d2qBA23gmKqC0')
"""

for i in range(1,51):

    css = "ytd-playlist-video-renderer.style-scope:nth-child({}) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(2)".format(i)
    
    picture = browser.find_element("css selector", css)

    kaynak = picture.get_attribute("href")

    print(kaynak)
    yol = "./deneme/{}.jpg".format(i)

    urllib.request.urlretrieve(kaynak, yol)
    time.sleep(1)

    




