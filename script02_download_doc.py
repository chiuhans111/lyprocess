import pandas as pd
from download import download
import re

term = 11
year = 113
period = 1
keyword = '立法院職權行使法'

df = pd.read_csv('./download/csv/院會紀錄_{term:02d}{period:02d}.csv')
for value in df[df['subject'].str.contains(keyword)]['docUrl']:
    for url in re.findall(r'https://.*?\.doc', value):
        download(url, './download/doc/'+url.split('/')[-1])

df = pd.read_csv('./download/csv/議事錄原始檔案.csv')
for url in df[df['term'] == term]['docUrl']:
    download(url, './download/doc/'+url.split('/')[-1])

df = pd.read_csv('./download/csv/黨團協商.csv')
for value in df[df['comYear'] == year]['docUrl']:
    for url in re.findall(r'https://.*?\.doc', value):
        download(url, './download/doc/'+url.split('/')[-1])


df = pd.read_csv('./download/csv/委員會紀錄_{term:02d}{period:02d}.csv')
for value in df[df['subject'].str.contains(keyword)]['docUrl']:
    for url in re.findall(r'https://.*?\.doc', value):
        download(url, './download/doc/'+url.split('/')[-1])

df = pd.read_csv('./download/csv/議案提案_{term:02d}{period:02d}.csv')
print(df['billName'].str.contains(keyword))
for url in df[df['billName'].str.contains(keyword) == True]['docUrl']:
    # for url in re.findall(r'https://.*?\.doc', value):
    download(url, './download/doc/'+url.split('/')[-1])
