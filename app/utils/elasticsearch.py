from elasticsearch import Elasticsearch
from decouple import config


def csv_cast(value):
    return [item.strip() for item in value.split(',')]


ELASTICSEARCH_HOSTS = config('ELASTICSEARCH_HOSTS', cast=csv_cast)


def get_elasticsearch():
    return Elasticsearch(hosts=ELASTICSEARCH_HOSTS)
