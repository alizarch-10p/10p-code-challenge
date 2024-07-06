from elasticsearch import Elasticsearch


def get_elasticsearch():
    return Elasticsearch(hosts=["http://elasticsearch:9200"])
