from elasticsearch import Elasticsearch
import json
es = Elasticsearch()


def create_index():
    for j in range(500):
        name = str(j)+".json"
        f = open(name, )
        data = json.load(f)
        res = es.index(index="music", doc_type='song', id=j, body=data)
        print(res['result'])

if __name__ == "__main__":
    create_index()