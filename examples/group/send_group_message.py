import requests
import configparser
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

if __name__ == '__main__':
    # [INPUT_GROUP_ID] 에 그룹 아이디를 넣어주세요
    # ex) G4V20181005122748TESTTESTTESTTES
    data = {
        'messages': [
            {
                'to': '01025570489',
                'from': '01053110489',
                'text': '안녕하세요'
            },
            {
                'to': '01028440489',
                'from': '01053110489',
                'text': '안녕하세요'
            }
        ]
    }
    res = requests.post(config.getUrl('/messages/v4/groups/[INPUT_GROUP_ID]/send'),
                        headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
