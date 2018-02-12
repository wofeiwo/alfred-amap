#!/usr/bin/python
#coding=utf-8
#author:wofeiwo@gmail.com
#last modified: 2018-02-12

from feedback import Feedback
import urllib2
import urllib
import json
import sys, os.path

AK              = '10e08aaa9afb3c590d43f5fd86eef081'
CITY            = '北京'
API_URL_BASE    = 'http://restapi.amap.com/v3/place/text'
MAP_URL_BASE    = 'https://ditu.amap.com/search?query=%s&city=%s'


def init_env():
    global CITY, AK
    if os.path.exists('city.txt'):
        CITY = file('city.txt', 'r').read().strip('\r\n \t')

    if os.path.exists('akey.txt'):
        AK = file('akey.txt', 'r').read().strip('\r\n \t')

def main(args):
    global CITY, AK, API_URL_BASE, MAP_URL_BASE
    init_env()
    
    region = urllib.quote(CITY)

    if len(args) == 2:
        query = urllib.quote(args[1])
        # query = urllib.quote('天安门')

        result = json.load(urllib2.urlopen(
            '%s?keywords=%s&city=%s&output=json&key=%s&extensions=all' % (API_URL_BASE, query, region, AK)))
        feeds = Feedback()

        if result['status'] == '1':
            if result['count'] == '0':
                if urllib.quote('到') in query or urllib.quote('去') in query:
                    map_url = MAP_URL_BASE % (query, region)
                    feeds.add_item(title=args[1], subtitle=u"搜索规划路径",
                                   valid='YES', arg=map_url, icon='icon.png')
            else:
                for i in result['pois']:
                    name    = i.get('name', u'搜索不到结果')
                    address = i.get('address', '')

                    if urllib.quote('到') in query or urllib.quote('去') in query:
                        map_url = MAP_URL_BASE % (query, region)
                    else:
                        map_url = MAP_URL_BASE % (name, region)

                    feeds.add_item(title=name, subtitle=address, valid='YES', arg=map_url, icon='icon.png')
        else:
            feeds.add_item(title=u'内容未找到', subtitle=u'输入内容有误', valid='no', arg=MAP_URL_BASE, icon='icon.png')

        print(feeds)
    return

if __name__ == '__main__':
    main(sys.argv)
