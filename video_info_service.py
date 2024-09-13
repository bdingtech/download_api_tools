from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def get_video_info(url):
    # 将 localhost 替换为 ydl_api_ng 服务的容器名称
    api_url = f"http://ydl_api_ng/extract_info?url={url}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        formats = data.get('formats', [])
        
        quality_links = {}
        for format in formats:
            format_url = format.get('url', '')
            protocol = format.get('protocol', '')
            height = format.get('height', '')
            
            if format_url and 'm3u8' not in protocol and height:
                quality_links[int(height)] = format_url
        
        # 对清晰度进行从低到高排序
        sorted_quality_links = {f"{height}p": quality_links[height] for height in sorted(quality_links.keys())}
        
        result = {
            'title': data.get('title', ''),
            'description': data.get('description', ''),
            'duration': data.get('duration', 0),
            'quality_links': sorted_quality_links
        }
        
        return result
    else:
        return {'error': '请求失败'}

@app.route('/video_info', methods=['GET'])
def video_info():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'error': '缺少URL参数'}), 400
    
    result = get_video_info(video_url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)