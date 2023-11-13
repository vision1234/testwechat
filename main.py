from flask import Flask, request, abort
import hashlib

app = Flask(__name__)

# 替换成你在公众平台设置的Token
token = 'your_token'

@app.route('/wechat/callback', methods=['GET', 'POST'])
def wechat_callback():
    if request.method == 'GET':
        # 微信服务器验证
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')

        if check_signature(signature, timestamp, nonce):
            return echostr
        else:
            abort(401)

    elif request.method == 'POST':
        # 处理微信服务器发送的消息
        data = request.data
        if data:
            # 在这里处理接收到的消息，解析XML等操作
            # 具体处理逻辑根据业务需求而定
            print(data)
        return ''

def check_signature(signature, timestamp, nonce):
    # 验证微信服务器发送的消息签名
    tmp_list = [token, timestamp, nonce]
    tmp_list.sort()
    tmp_str = ''.join(tmp_list)
    tmp_str = hashlib.sha1(tmp_str.encode('utf-8')).hexdigest()

    return tmp_str == signature

if __name__ == '__main__':
    # 运行服务器
    app.run(host='127.0.0.1', port=5003)
