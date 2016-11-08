from scrapy.exceptions import DropItem
import urllib
import os

class FilterWordsPipeline(object):
    base_file = os.getcwd() + '/images/' 
    def process_item(self, item, spider):
                local_file = self.base_file +  item['file_name'] 
                uf = urllib.urlopen(item['url'])
                content = uf.read()
                f = file(local_file.encode('UTF-8'), 'wb')
                f.write(content)
                print item['url'] 
                print 'write Done! : ' + local_file
                f.close()
                return item

