# This code is used to extract followers from a specific profile in Instagram. It can be used on more profile at the same time.

import re
import csv
from time import sleep
import os
import sys
import pathlib
from timeit import default_timer as timer
import datetime

import time
start_time = time.time()
pausa2 = start_time

import urllib3
import instaloader

# Get instance
L = instaloader.Instaloader()

# Login or load session

# Change the username and password with the one you're going to use
L.login('username', 'password')        # (login)
#L.interactive_login(USER)      # (ask password on terminal)
# L.load_session_from_file('dslr.lover.nepal') # (load session created w/

pathlib.Path('downloads/').mkdir(parents=True, exist_ok=True)

http = urllib3.PoolManager()


start = timer()
curr = str(datetime.datetime.now())    

def wait_for_internet_connection():
    while True:
        try:
        
            response = http.request('GET', 'http://ku.edu.np')
            return
        except:
            print('No internet connection.\nTrying after 5 seconds.\n')
            sleep(5)

# wait_for_internet_connection()

f = open('input_instabot.txt','r')
accounts = f.read()
p = accounts.split('\n')
cont = 0

with open('last.txt','r') as f:
    last =  f.read()
    last=last.strip()
print('Last account scraped was:',last)

for profile in p:
    if last in profile and len(last)>2:
        print(last,profile)
        p.remove(profile)


# input()
print('Resuming from:',p[0])
PROFILE = p[:]
print(PROFILE)
print('Total accounts:',len(PROFILE))

for ind in range(len(PROFILE)):
    pro = PROFILE[ind]
    try:
#         wait_for_internet_connection()
        print('\n\nGetting followers from',pro)
        filename = 'downloads/'+pro+'.csv'
        with open(filename,'a',newline='',encoding="utf-8") as csvf:

            csv_writer = csv.writer(csvf)
            csv_writer.writerow(['username','follower_count'])
            

    
        profile = instaloader.Profile.from_username(L.context, pro)
        main_followers = profile.followers
        count = 0
        total=0
        # Print list of followees
        
        for person in profile.get_followers():
            try:
#                 wait_for_internet_connection()
                total+=1
                
                username = person.username
                follower_count = person.followers



                print('Username:',username)
                with open(filename,'a',newline='') as csvf:

                    csv_writer = csv.writer(csvf)
                    csv_writer.writerow([username, follower_count])
                # os.system('clear')
                # os.system('cls' if os.name == 'nt' else 'clear')
                pausa = time.time()-pausa2
                cont = cont + 1
                if pausa > 300:
                    print('------- Followers extracted: %s' % cont)
                    print('----------------------------------- PAUSE ------------------------------------')
                    sleep(320)
                    pausa2 = time.time()
            
            except Exception as e:
                print(e)
            

        #saving the last account for resume
        f=open('last.txt','w+')
        f.write(pro)
        f.close()
        #log of completed account
        f=open('completed.txt','a+')
        f.write(pro+'\n')
        f.close()
        # (likewise with profile.get_followers())
    except:
        print('Skipping',pro)

end_time = time.time() - start_time
print('------- Followers extracted: %s' % cont)
print("--- Extraction time: %s seconds ---" % end_time)
