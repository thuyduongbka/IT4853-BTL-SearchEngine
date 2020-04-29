import pysolr
import json

solr = pysolr.Solr('http://localhost:8983/solr/BTL/')
with open('data.json', 'r') as json_file:
    json_object = json.load(json_file)
    solr.ping()
    solr.add(json_object)
    solr.commit()