# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:14:20 2019
    作者：kexinl
    项目：天气预测AQI
    版本：3.0
"""
import requests
def get_html_text(url):
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text
def main():
    city_pinyin = input('请输入城市拼音:')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    print(url_text)
    
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 3
    aqi_val = url_text[begin_index: end_index]
    print('空气质量为：{}'.format(aqi_val))
    
if __name__ == '__main__':
    main()
