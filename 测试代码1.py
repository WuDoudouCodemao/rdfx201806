import json
import datetime
time = str(datetime.datetime.now())
lyb = [["李心言","同学们好😊",time[:-10]]]
print(lyb)
with open("lyb_json.json","w") as f:
    json.dump(lyb,f)
    