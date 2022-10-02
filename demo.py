from newsapi import NewsApiClient
import cv2
import numpy as np
import urllib.request
import os
import random
import time
from instabot import Bot


bot = Bot()
bot.login(username = 'USERNAME',password = 'PASSWORD')


newsapi = NewsApiClient(api_key='ENTER_API_KEY_HERE')
while True:
    top_headlines =  newsapi.get_top_headlines( category='general', language='en', country='in')
    print(top_headlines['totalResults'])
#business entertainment general health science sports technology

    art = top_headlines['articles']   
    print(len(art)) 
    for i in range(len(art)):        
        img_url = art[i]['urlToImage']        
        text = (art[i]['title'])+"     "+(art[i]['source']['name'])+"      Link:-"+(art[i]['url'])
        print(text)
        try:
            data = urllib.request.urlretrieve(img_url, "local-filename.jpg")
            time.sleep(2)
        except:
            print("issue")
        img = cv2.imread("local-filename.jpg")
        s = max(img.shape[0:2])
        f = np.zeros((s,s,3),np.uint8)
        f[f==0]=255
        ax,ay = (s - img.shape[1])//2,(s - img.shape[0])//2
        f[ay:img.shape[0]+ay,ax:ax+img.shape[1]] = img
        f = cv2.resize(f,(1080,1080))
        cv2.imwrite("img2square.jpeg",f)     

        # Instagram Codes
        #comments = [add your comments here] #["comment1","comment2"] add more than 2 comments
        tags= ["#news","#trending","#technews","#sportsnews","#finnews","#latestnews","#trendingnews","#indianews","#indiatimes","#nationalnews","#englishnews","#finance","#technology","#finance","#sports"] #["#lol","startup","#fun"] add more than 10 tags
        final_tags = " ".join(random.sample(tags, 10))
        final_caption = (art[i]['title'])+"     "+(art[i]['source']['name'])+"    DO follow us             @indiantimes_official                      @indiantimes_official                            @indiantimes_official                       "+final_tags
        print(final_caption)
        bot.upload_photo("img2square.jpeg",caption = final_caption)            
        time.sleep(60*30+10)
        