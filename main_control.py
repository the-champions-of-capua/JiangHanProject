from flask import Flask
import json
import requests

app = Flask(__name__)

import random
def creategraph(gspace, gtime, num):
    buff = ()
    for i in range(num):
        ret1 = random.randrange(gspace[0], gspace[1]+1)  # 空间
        ret2 = random.randrange(gtime[0], gtime[1]+1)    # 时间
        buff += ((ret1, ret2), )
    return buff


@app.route('/QueryGraph', methods=['GET'])
def query_graph (conn):
    # 查询正在使用的图案代码，查数据库即可
    cursor = conn.cursor() # 游标，用来跟数据库交互
    cursor.execute('SELECT * FROM table_name WHERE status=1')
    data = cursor.fetechone()
    return data

@app.route('/StopService', methods=['GET'])
def stop_service():
    # 向代理控制模块发送请求，停止变换
    agent_url = 'http://127.0.0.1:81/StopChange'
    data = json.dumps({"command":"stop"})
    headers = {'Content-Type':'application/json'}
    rep = requests.post(url= agent_url, data=data, headers=headers)
    return rep.text

@app.route('/StartService', methods=['GET'])
def start_service():
    # 传递图案信息给代理控制模块
    # 当然，图案存入数据库，由代理控制模块读取数据库信息也是可以的
    agent_url = 'http://127.0.0.1:81/Start'
    graph_content = creategraph([1,4],[2,5],10)
    data = json.dumps(graph_content)
    headers = {'Content-Type':'application/json'}
    rep = requests.post(url= agent_url, data=data, headers=headers)
    return rep.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
