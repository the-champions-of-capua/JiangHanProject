from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/StopChange', methods=['POST'])
def stop_change ():
    p_data = request.get_data(as_text=True) # 接收主控模块传来的参数
    data = json.loads(p_data) # 将JSON字符串转换为Python数据结构
    if data['command'] == 'stop':
        print('Bingo!')
    # stop_web() # 调用注意事项中提到的方法
        return 'Done'
    else:
        return 'ParameterError'

@app.route('/Start', methods=['POST'])
def start ():
    p_data = request.get_data(as_text=True) # 接收主控模块传来的参数
    data = json.loads(p_data) # 将JSON字符串转换为Python数据结构
    print(data) # 可以看到图案信息已经传递过来
        # change_web() 调用改变代理端口的方法
    return 'Done'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
