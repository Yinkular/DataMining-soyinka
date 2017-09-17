# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:18:02 2017

@author: soyinka
"""

import sys
import requests
import bs4
from bs4 import BeautifulSoup
import time
import random
import json

restaurantList= []

for i in range (0,110,10):
    pageStart =str(i) # variable indicating start of page
    
    #full URL including page start
    url = "https://www.yelp.com/search?find_loc=Wichita+Falls,+TX&start=" 
    url = url +pageStart+"&cflt=restaurants"
    
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    
    restaurants = soup.find_all('li',{'class':'regular-search-result'})
    
    for restaurant in restaurants:
        # get name of restaurant
        nameContainer = restaurant.findNext('a',{'class':'biz-name'})
        name =  nameContainer.findNext('span').text
                        
        # get number of reviews
        reviewsContainer  = restaurant.findNext('div',{'class':'biz-rating'})
        reviewsTag = reviewsContainer.findNext('span', {'class': 'review-count'})
        reviews = reviewsTag.text
        
        # get the price range
        priceContainer  = restaurant.findNext('div',{'class':'price-category'})
        price = priceContainer.findNext('span', {'class': 'price-range'}).text
            
        # get the phonenumber
        phoneContainer = restaurant.findNext('div',{'class':'secondary-attributes'})
        phone = phoneContainer.findNext('span', {'class': 'biz-phone'}).text
        
          
        # store data in JSON format
        restaurantDict = {}
        restaurantDict['name']= name.strip()
        restaurantDict['reviews'] = reviews.strip()
        restaurantDict['priceRange'] = price.strip()
        restaurantDict['phone'] = phone.strip()
        
        # append to list
        restaurantList.append(restaurantDict)
        
     
        
        # pause before new request is made
        time.sleep(random.randint(0,3))
        
        
    #print list
   # for restaurant in restaurantList:
    with open('data.json', 'w+') as outfile:
            jsonData = json.dumps(restaurantList,indent=True)
            outfile.write(jsonData)
    
    
    
