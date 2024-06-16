import os
import pandas as pd
import csv
from tqdm import tqdm

black_list = ["受文者", "發文日期", "發文字號", "速別",
              "密等及解密條件或保密期限", "附件", "主旨", "說明", "正本", "副本",
              "紀　　錄", "決定", "案由"]

folder = './parsed/doc_csv'

speaker = ''
content = ''

data = []

for file in tqdm(os.listdir(folder)):
    if file.startswith('LCIDC'):
        # print(file)
        df = pd.read_csv(os.path.join(folder, file))

        start_speaking = False

        for i, paragraph in df.iterrows():
            if paragraph['style'] != '內文' or paragraph['space_before'] > 0 or paragraph['space_after'] > 0 or paragraph['cell_id'] == paragraph['cell_id']:
                start_speaking = False
                continue

            if not paragraph['text'] == paragraph['text']:
                start_speaking = False
                continue

            text = str(paragraph['text']).strip()

            if len(text) == 0:
                continue

            parts = text.split('：')

            if len(parts) == 1:
                if start_speaking:
                    if text.startswith('（') or text.endswith('）'):
                        continue
                else:
                    continue

                content += parts[0]
            else:
                if '、' in parts[0]:
                    start_speaking = False
                    continue
                if parts[0] in black_list:
                    start_speaking = False
                    continue
                start_speaking = True

                if len(content) > 0:
                    data.append([speaker, content])

                speaker = parts[0]
                content = parts[1]

if len(content) > 0:
    data.append([speaker, content])

with open('./parsed/all_speech/test.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['speaker', 'content'])
    for row in data:
        writer.writerow(row)


