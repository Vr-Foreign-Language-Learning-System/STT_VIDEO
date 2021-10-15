import json
import csv

# music.json 파일을 읽어서 music.csv 파일에 저장
with open('sample.json', 'r', encoding = 'utf-8') as input_file, open('sample.csv', 'w', newline = '') as output_file :
    data = json.load(input_file)

    f = csv.writer(output_file)

    # csv 파일에 header 추가
    f.writerow(["startTime", "endTime", "word"])

    # write each row of a json file
    for key in data["alternatives"]:
        for x in key['words']:
            f.writerow([x["startTime"], x["endTime"], x["word"]])

    '''
    for datum in data:
    # exclude instrument versions
        if any(x for x in datum["alternatives"]["words"]):
          continue
        f.writerow([datum["startTime"], datum["endTime"], datum["word"]])
    '''