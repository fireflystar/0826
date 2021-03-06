# coding=utf-8
import json
from sys import argv
import os
import urllib
import urllib2

def main(member_id, page=1, index=0):
    url = 'http://worldcosplay.net/en/api/member/photos?member_id=%s&page=%s&limit=100000&rows=16&p3_photo_list=1' % (member_id, page)
    r = urllib2.urlopen(url)

    if r.code == 200:
        data = json.loads(r.read())
        if data['has_error'] != 0:
            print u'接口挫了'
            exit(1)

        photo_data_list = data['list']
        if not photo_data_list:
            print u'没东西了？第 %s 页，共下载了 %s 个图片' % (page, index - 1)
            exit(0)
        if not os.path.exists(member_id):
            os.makedirs(member_id)
        for photo_data in photo_data_list:
            url = photo_data['photo']['sq300_url']
            url = url.replace('/sq300', '')

            subject = photo_data['photo']['subject']
            subject = subject.replace('/', '_')

            filename = '%s/%s_%s.jpg' % (member_id, member_id, index)
            try:
                print(url, filename)
                urllib.urlretrieve(url=url, filename=filename)
                print u'下完了%s张' % (index + 1)
                index += 1
            except Exception, e:
                print e

        page += 1
        main(member_id, page=page, index=index)

    else:
        print u'挫了'
        exit(1)

if __name__ == '__main__':
    # if len(argv) < 2:
    #     print(u'请输入coser ID，例如：53056')
    #     exit(1)
    # member_id = argv[1]
    main('85156')

#worldcosplay.net/uploads/
#http://worldcosplay.net/en/api/member/photos?member_id=38586&page=8&limit=100000&rows=16&p3_photo_list=1