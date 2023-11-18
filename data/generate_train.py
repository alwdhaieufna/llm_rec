import json
id2profile = {}
fi = open("ml-1m.item", encoding="utf8")
for line in fi.readlines()[1:]:
    arr = line.strip().split("\t")
    id2profile[arr[0]] = [arr[1], arr[2], arr[3]]

all_data = []
fi = open("ctr_predict.tsv", encoding="utf8")
fo = open("rec_data_ml_1m.json", "w", encoding="utf8")
for line in fi.readlines()[:100]:
    arr = line.strip().split(" ")
    prompt = "I am an assistant working on movie recommendation, below is the watch history of an user: "
    for item in arr[:-2]:
        profile = id2profile[item]
        prompt += "< Name:" + profile[0] + ", Year:" + profile[1] + ", Genre:" + profile[2] +   " > "
    prompt += "Based on above user history information, I can make a recommendation: "
    obj = {}
    obj["instruction"] = prompt
    obj["input"] = ""
    pos_profile = id2profile[arr[-2]]
    neg_profile = id2profile[arr[-1]]
    obj["output"] = ["< Name:" + pos_profile[0] + " Year:" + pos_profile[1] + " Genre:" + pos_profile[2] +   " > ", "< Name:" + neg_profile[0] + " Year:" + neg_profile[1] + " Genre:" + neg_profile[2] +   " > "]
    all_data.append(obj)
fo.write(json.dumps(all_data))
