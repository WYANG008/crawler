#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (c) 2013, Revolution Analytics
# All rights reserved.


"""
Parsing the html content according to configuration.
"""
import sys
sys.path[0:0] = [
    '/home/ec2-user/rr-crawler/src'
]
import re
import urllib2
import HTMLParser
from lxml.cssselect import CSSSelector
from lxml.html import fromstring
from lxml import etree

function_mapping = {
    "str" : str,
    "int" : int,
    "float" : float
}

def to_plain_text(tag):
    """ Transfer a <p></p> elements to plain text. 
        Replace all the html <tag> and </tag>.
    """
    pString = etree.tostring(tag)
    tagPattern = r"<[^>]*>"
    pString = re.sub(tagPattern, "", pString)
    h = HTMLParser.HTMLParser()
    return h.unescape(pString)


def parse_page(html, config):
    """
    Parse the html according to the configuration.
    html: target html string.
    config: corresponding config for this type of page.
    return: list of data in that page.
            list target link for next crawling job.
    """
    data = []
    links = []
    h = fromstring(html)
    # Get the entity for holding the target data.
    entities = []
    entity_selector = config["entity_selector"]
    if entity_selector:
        entity_selector = CSSSelector(entity_selector)
        entities = entity_selector(h)


    # parse the data in each entity
    for entity in entities:
        entity_data = {}
        for attr in config["attributes"]:
            name = attr["name"]
            type = attr["type"]
            attrname = attr["attr"]
            selector = CSSSelector(attr["selector"])
            attr_data = selector(entity)
            if len(attr_data) == 0:
                break
            if attrname != "text":
                attr_data = attr_data[0].get(attrname)
            else:
                attr_data = to_plain_text(attr_data[0])
            attr_data = attr_data.encode("ascii", "ignore")
            entity_data[name] = function_mapping[type](attr_data)
        data.append(entity_data)

    # parse the link for next crawling job.
    baseUrl = config["baseurl"]
    for link in config["links"]:
        selector = CSSSelector(link["selector"]) 
        els = selector(h)
        for el in els:
            url = baseUrl + el.get("href")
            links.append((url, link["model"]))
        pass
    return data, links


if __name__ == "__main__":
    from WebCrawler.config import config
    config = config.load_pages("../../../tests/WebCrawler/config/skyscanner.json")
    model = "skyscanner_citylist"
    page_config = None
    for webpage in config:
        for k, v in webpage.iteritems():
            if k == "model" and v == model:
                page_config = webpage
    test_page = "http://www.skyscanner.net/flights-to/cheap-flights-to-cities-all.html?letter=a"
    html = urllib2.urlopen(test_page).read()
    data, links = parse_page(html, page_config)
    print data
    print links
    pass

