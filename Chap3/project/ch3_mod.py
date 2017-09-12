#!/usr/bin/env python3
import requests
import os
import time

def help_message():
    ''' 帮助信息

    '''
    list_message = ["输入城市名，点击「查询」，获取该城市最新天气情况；",
                    "点击「历史」，获取查询历史信息；",
                    "点击「帮助」，获取帮助信息。"]
    return list_message

        
def history_message(list_history_record):
    ''' 查询历史记录

    '''
    if list_history_record:
        return list_history_record
    else:
        return [["尚未查询过城市天气！"], ]
    
        
        
def get_city_weather(city_name):
    ''' 查询城市天气

    - 输入城市名
    - 查询成功，返回城市天气；查询失败，返回相关信息
    - 通过“心知天气API”实现（“心知天气API”文档由 https://www.seniverse.com/doc 获得。）
    '''
    weather_message = []
    my_api_thinkpage_key = os.getenv("API_THINKPAGE_KEY", default=None)
    if my_api_thinkpage_key == 'None':
        weather_message = ["获取密钥失败，请检查相关系统环境变量。"]
        exit()
    else:
        pass
    print("{0}".format(my_api_thinkpage_key))    # test #
    
    weather_params = {'key' : my_api_thinkpage_key,
                      'location' : city_name,
                      'language' : 'zh-Hans',  # 参数zh-Hans，表示简体中文
                      'unit' : 'c'}   # 当参数为c时，温度c、风速km/h、能见度km、气压mb
    try:
        r = requests.get('https://api.seniverse.com/v3/weather/now.json', params = weather_params)
    except:
        weather_message = ["遇到网络问题，请检查！"]
        
    if r.status_code == 200: 
        j = r.json()
        print(j)   # test #
        weather_state = j['results'][0]['now']
        weather_time = j['results'][0]['last_update']  # “心知天气API”返回的时间格式，类似“ 2017-08-27T21:50:00+08:00 ”
        t = time.strptime(weather_time[:19], "%Y-%m-%dT%H:%M:%S")
        weather_message = [city_name,
                           weather_state['code'],
                           weather_state['text'],
                           weather_state['temperature'] + '℃',
                           time.strftime("%Y-%m-%d %a %H:%M", t)]
    else:
       weather_message = ["城市名 {0!r} 不存在，请重新输入！ （需要帮助信息，请点击「帮助」）" .format(city_name) ]
    return weather_message


def print_message(list_one):
    for x in list_one:
        print("\t{0}".format(x))

              
if __name__ == '__main__':
    list_history_record = []
    while True:
        input_value = input("请输入指令或城市名（帮助“help”，历史信息“history”，退出“quit”）: ")
        input_value = input_value.strip(' ')
        if input_value == 'help':
            print_message( help_message() )
        elif input_value == 'history':
            print_message( history_message(list_history_record) )
        elif input_value == 'quit':
            exit(0)
        else:
            result = get_city_weather(input_value)
            print_message(result)
            if len(result) > 1:
                list_history_record.append( '\t'.join(result) )
            else:
                pass
