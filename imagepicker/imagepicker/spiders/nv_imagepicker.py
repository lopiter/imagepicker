from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from imagepicker.items import Website

import HTMLParser
import json

from pprint import pprint

class ImgSpider(Spider):
    name = "nv_imagepicker"
    allowed_domains = ["naver.com"]
    i = 1
    current_item_idx = 1 
    base_url = "https://s.search.naver.com/p/instant/search.naver?_callback=window.__jindo2_callback._imageenlarge1234_0&where=image&section=image&rev=31&res_fr=1&res_to=153599&face=1&color=0&ccl=0&aq=0&spq=1&query={!s}&nx_search_query={!s}&nx_and_query=&nx_sub_query=&nx_search_hlquery=&nx_search_fasquery=&ac=0&json_type=6&ie=utf8&datetype=0&startdate=0&enddate=0&ssl=1&display=48&start={!s}"

    def __init__(self, SearchWord = None, iteration = 0 , *args, **kwargs):
        super(Spider, self).__init__(*args, **kwargs)
        self.search_word = SearchWord
        self.start_urls = [self.base_url.format(SearchWord, SearchWord , 0)] 
        self.iteration=iteration
    
    def parse(self, response):
        global last_id
        items = []
	print('response ok')
	text = response.text.encode('utf8')
	item_idx = text.find("item:")
	jsonresponse = json.loads('{"item":' + text.strip()[item_idx+3:-3])
	sel = Selector(response)
	for item in jsonresponse['item']:
            downloadItem = Website()
            img_url = item['sThumb'].encode('utf8') 
	    downloadItem['url'] = img_url
            downloadItem['file_name'] = img_url[img_url.rfind('/') + 1:]
            yield downloadItem 
        item_count = len(jsonresponse['item'])
        self.current_item_idx = self.current_item_idx + item_count
        print(self.i)
        print(self.iteration)
        if int(self.i) <  int(self.iteration) :
            self.i += 1
            print 'go to %d page' % self.current_item_idx
            yield Request(self.base_url.format(self.search_word, self.search_word,self.current_item_idx), callback=self.parse)
