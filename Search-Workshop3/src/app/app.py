"""
Creating Flask APIs
"""
__author__ = "UniCourt Inc"
__version__ = "v1.0.0"
__maintainer__ = "Search - Core & API"
__email__ = "eng-search@unicourt.com"

from flask import Flask, request
import os
import sys
import logging

sys.path.insert(0, '/src')

from views.delivery_info import GetDeliveryInfo
from views.product_stats import GetProductStats
from utils.utils_es import get_es_connection
from utils.utils_postgres import set_connection

LOGGER = logging.getLogger("search_logger")
PG_CON = set_connection(LOGGER)

app = Flask(__name__)
ES_CON = get_es_connection(os.environ['ES_HOST'], os.environ['ES_PORT'])


@app.route('/DeliveryInfo', methods=['POST'])
def get_delivery_info():
    """
    Method to return delivery info for the given product_id
    :return:
    """
    post_data = request.get_json()
    delivery_info_obj = GetDeliveryInfo(PG_CON)
    return delivery_info_obj.process(post_data)


@app.route('/ProductStats', methods=['POST'])
def get_product_stats():
    """
    Method to return products stats info for the given product_id
    :return:
    """
    post_data = request.get_json()
    product_stats_obj = GetProductStats(ES_CON)
    return product_stats_obj.process(post_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
