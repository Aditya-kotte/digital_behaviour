import csv
import random as rd
from datetime import datetime,timedelta

NO_of_Days = 30
rd.seed()

start_date = datetime.now() - timedelta(days = NO_of_Days)

rows = []
for i in range(NO_of_Days):
    rows.append(['current_date','insta_min','yt_mins','whatsapp_mins','reels_watched','linkedin_mins','vedios_watched','msg_sent','posts_liked','study_,min'])
    
