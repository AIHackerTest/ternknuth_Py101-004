#!/usr/bin/env python3
import requests
import os
import time

def print_help():
    ''' 打印帮助信息

    '''
    help_message = ["输入城市名，返回该城市最新的天气数据；",
                    "输入指令 h 或 help ，获取帮助信息；",
                    "输入指令 hist 戓 history ，获取历史查询信息；",
                    "输入指令 q 、quit 或 e 、exit ，退出程序的交互。"]
    for i in help_message:
        print("\t{0}".format(i))

        
def print_history_record(list_history_record):
    ''' 打印查询历史记录

    '''
    if list_history_record:
        print("\t------查询历史记录------")
        for i in list_history_record:
            print("\t", end='')
            for j in i:
                print("{0}\t".format(j), end='')
            else:
                print("")
        else:
            pass
    else:
        print("\t尚未查询过城市天气！")
        
        
def get_city_weather(city_name):
    ''' 查询城市天气

    通过“心知天气API”实现。
    详情查询相关文档（https://www.seniverse.com/doc） '''
    my_api_thinkpage_key = os.getenv("API_THINKPAGE_KEY", default=None)
    if my_api_thinkpage_key == 'None':
        print("获取密钥失败，请检查相关系统环境变量。")
        exit()
    else:
        pass

    weather_params = {'key' : my_api_thinkpage_key,
                      'location' : city_name,
                      'language' : 'zh-Hans',  # 参数zh-Hans，表示简体中文
                      'unit' : 'c'}   # 当参数为c时，温度c、风速km/h、能见度km、气压mb
    r = requests.get('https://api.seniverse.com/v3/weather/now.json', params = weather_params)
    j = r.json()
    weather_state = j['results'][0]['now']
    # print(weather_state['text'], weather_state['temperature'])
    weather_time = j['results'][0]['last_update']
    # print(weather_time)            # 输出类似 2017-08-27T21:50:00+08:00
    t = time.strptime(weather_time[:19], "%Y-%m-%dT%H:%M:%S")
    return (city_name, weather_state['text'], weather_state['temperature'] + '℃', time.strftime("%Y-%m-%d %a %H:%M", t))



def app():
    ''' 主程序

    '''
    list_history_record = []
    while True:
        input_value = input("请输入指令或城市名: ")
        input_value = input_value.strip(' ')
        if input_value in ['h', 'help']:
            print_help()
        elif input_value in ['hist', 'history']:
            print_history_record(list_history_record)
        elif input_value in ['q', 'quit', 'e', 'exit']:
            exit(0)
        else:
            try:
                result = get_city_weather(input_value)
            except:
                print( "\t该指令或城市名不存在，请重新输入！ （需要帮助请输入‘h’戓‘help’）" )
                continue
            for x in result:
                print("\t{0}" .format(x))
            list_history_record.append(result)


if __name__ == '__main__':
    app()
