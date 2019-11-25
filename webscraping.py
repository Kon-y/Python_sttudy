#!/usr/bin/python3
# Hack the problem collection of koiwa club.

import requests
import json

r = requests.get('https://nikkei225jp.com/chart/')
text = r.text
date     = text.split('<div class=wtimeT>')[1].split('</div>')[0]
week     = text.split('<div class=wtimeW>')[1].split('</div>')[0]
nik_cal  = text.split('<span class=if_col>')[1].split('</span>')[0]
nikkei   = text.split('<div class=if_cur>')[1].split('</div>')[0].replace(',','')
dau      = text.split('<div class=if_cur>')[2].split('</div>')[0].replace(',','')
kawase   = text.split('<div class=if_cur>')[3].split('</div>')[0].replace(',','')

print('今日は',date + '(' + week + ')','です')
print (nik_cal+'は' ,nikkei, '円です')
print ('ダウ平均株価は', dau, '円です')
print ('為替ドルは', kawase,'円です')

#
a=open('shares.csv','w')
a.write('日時,日経平均株価,ダウ平均株価,為替ドル\n')
a.write(date+','+nikkei+','+dau+','+kawase+'\n')
a.close()