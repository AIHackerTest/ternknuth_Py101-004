#!/usr/bin/env python3

def print_help():
    ''' 打印帮助文档

    '''
    help_message = ["输入城市名，返回该城市的天气数据；",
                    "输入指令 h 或 help ，打印帮助文档；",
                    "输入指令 q 、quit 或 e 、exit ，退出程序的交互；",
                    "在退出程序之前，打印查询过的所有城市。"]
    for i in help_message:
        print("\t{0}".format(i))

        
def print_history_record(list_history_record):
    ''' 打印查询历史记录

    '''
    if list_history_record:
        print("\t------查询历史记录------")
        for i in list_history_record:
            print("\t{0[0]} {0[1]}".format(i) )
        else:
            pass
    else:
        print("\t尚未查询过城市天气！")
        
        
def get_city_weather(city_name, dict_weather_data):
    ''' 查询城市天气

    '''
    if city_name in dict_weather_data:
        return dict_weather_data[city_name]
    else:
        return False


def make_weather_data(file):
    ''' 建立城市天气数据字典

    天气数据文件中，每行数据格式如下：
    城市名,天气状况 '''
    weather_data = {}
    try:
        fh = open(file, 'r')
    except:
        print("\t未找到城市天气数据文件！")
        exit(0)
    for line in fh.readlines():
        line = line.strip('\n')
        list_value = line.split(',')
        weather_data[list_value[0]] = list_value[1]
    fh.close()
    return weather_data


def main():
    ''' 主程序

    '''
    list_command = {'h' : 'help',
                    'help' : 'help',
                    'q' : 'quit',
                    'quit' : 'quit',
                    'e' : 'quit',
                    'exit' : 'quit'}
    list_history_record = []
    file = '../resource/weather_info.txt'
    weather_data = make_weather_data(file)
    while True:
        input_value = input("请输入指令或城市名: ")
        input_value = input_value.strip(' ')
        if input_value in list_command:
            if list_command[input_value] == 'help':
                print_help()
            elif list_command[input_value] == 'quit':
                print_history_record(list_history_record)
                exit(0)
            else:
                pass
        elif input_value in weather_data:
            result = (input_value, get_city_weather(input_value, weather_data) )
            print("\t{0[0]} {0[1]}".format(result) )
            list_history_record.append(result)
        else:
            print( "\t该指令或城市名不存在，请重新输入！ （需要帮助请输入‘h’戓‘help’）" )
            continue


if __name__ == '__main__':
    main()
