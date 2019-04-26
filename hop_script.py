import time

def ha_control(ip, port):
    """
    该函数用来修改HAProxy的配置
    :return:
    """
    print(ip, port)
    pass

def change_control(graph_content, position, rate=None):
    """
    :param graph_content:[[],[],[],[],[],[]]
    :param position:int,<len(graph_content)
    :param rate: None or int
    :return:
    """
    if position < len(graph_content):
        for i in graph_content[position:]:
            print(i)
            start_time = time.time()
            end_time = start_time + i[1]
            flag = 0
            while  start_time < end_time:
                if flag == 0:
                    ha_control('127.0.0.1', 8000)
                    flag = 1
                time.sleep(1)
                start_time = time.time()
                print(start_time)
    else:
        pass

change_control([[1,2],[2,4],[4,4],[3,2],[2,4],[1,5]], 3)