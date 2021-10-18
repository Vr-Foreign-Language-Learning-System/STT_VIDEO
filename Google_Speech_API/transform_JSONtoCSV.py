import json
import csv

# test.json 파일을 읽어서 test.csv 파일에 저장
with open('test.json', 'r', encoding = 'utf-8') as input_file, open('test.csv', 'w', newline = '') as output_file :
    data = json.load(input_file)

    f = csv.writer(output_file)

    # csv 파일에 header 추가
    f.writerow(["word", "start_time", "end_time"])

    # write each row of a json file
    for key in data["sentence"]:
        f.writerow([key["word"], key["start_time"], key["end_time"]])

    '''
    for datum in data:
    # exclude instrument versions
        if any(x for x in datum["alternatives"]["words"]):
          continue
        f.writerow([datum["startTime"], datum["endTime"], datum["word"]])
    '''