import pandas as pd
import jieba
import csv
from tqdm import tqdm
pd = pd.read_csv('./parsed/all_speech/test.csv')

records = {}

for i, row in tqdm(pd.iterrows()):
    speaker = row['speaker']

    if speaker not in records:
        records[speaker] = {}
    record = records[speaker]

    for word in jieba.cut(row['content']):
        if word not in record:
            record[word] = 0
        record[word] += 1


for speaker, record in records.items():
    records[speaker] = list(record.items())
    records[speaker].sort(key=lambda x: -x[1])

rows = []
for speaker, record in records.items():
    rows.append([speaker, sum([len(r[0])*r[1] for r in record]), *[f"{r[0]}:{r[1]}" for r in record[:100]]])
rows.sort(key=lambda x:-x[1])

with open('./parsed/all_speech/analyzed.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)