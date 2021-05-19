#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/13 16:45
# @Author  : Beam
# @Site    :
# @File    : demo_Monitor2.py
# @Software: PyCharm

import urllib,urllib2
import smtplib
import json
import time

URLS = ['https://app.xuehu365.com/community/list?paras=rkaStijLzJsXnpX2SumroqTrendEFob1k6j6xBwV3%2BfEAs6qGGMO1YRoQyXtJskbk7k9YHVedLj7C8DgHQhIL2hL9Lp3zVQCPqVd10lZcgcEKmypTjvIucrkERMSYJ4rMbZ007zfhCGCmWPfuwArytVZSHFpOZZNb09TJbN4tRbUhwk/ROGBLhowal0PRen12rbx9w0OzUqX/bFaVzDhDw%3D%3D&sign=CC73C40343F396E4D3356E745716F5AD823A6851&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/community/list?paras=2u%2B57x3/SsCACtm/LcEDskWRY9i%2BhCSADp%2B/tNNu0glivH5idj10KQz8/F1V%2BaQRyZHbCm7V7eV2i8vB6Cv2BhF/gQBUjnRfZkpQX4C6D1zJ873xkL4OWv75Rj/venluC25WecTueM8PfziHpobc4LHZPe3oxm%2BBSknClqX9NKu17TTh14Spkf0U2DggSUs5dW0u9bKeug4PROXCqzAkZg%3D%3D&sign=DFAAB6A157E65BF53A5DB552CA17C67E49F9BE4A&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/index?paras=8/wCjbYzsyiICUBjK5GiPJkv6LsQmpZsoEdUrE5ujt/diELwAddMnp5xzZW4L0rFsY6sYKnKr3saBQPplCZo1HzvR%2BwmjgQG0KoUJyIukAJg9bcOf/SvoNvAalyoxJavjHAGpSiQLNrXnPAT1iDt1wC%2B2MQjSZd7vqX%2B5tJb2bOuHgFEeDiVVSbaIlCV%2Bu5aPclQGH2cxQ0%3D&sign=011135B9F789E2BC26FCD20DB11807E70A671B5E&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0', 'https://app.xuehu365.com/community/chat/enter?paras=4aZDACfJnjnwhZGI1SCtD%2BWOA7NFfWjWWrQ0GTJPOI9XwjiK4wzAZh7bgR9CmhJVo%2BMidX%2BoAdtrK/EzQ5Ylo7eUhq4H0GKozQzGLMt/GbwLdhbpfMMw7xQ%2BBU6xRH8P/I1bU1UaCv0TSVuuPubTC3Zp2nC2o5xZaXYyjvfRg3NHopEu3T%2B8GkwynPQ2AFYyaJfzpg%3D%3D&sign=8419D50838B06D8D3AD671A9A90A1B446EE5791F&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/community/share/list?paras=TFszZiBmRVVF2/P6wwIjoyZ7U98CTnYgu/LhwGpNreS/%2BQaZXrJF0MGOkCPNEGS/fFY/AWK9z/hIVTzAWN9faECmyHkhjz%2Bgd1mQNprsoXUU7FU365gx5NzVkdiX6XN7u4/7P6m1qbvhUoNNI5o6J%2BlcUWPMYXX%2B5aqWi5duwoVbEPWtULDy3lZbShMkSEhlNdlGoWiZV8ZVnDLN/GSLndTNoZBlSI7C&sign=6654D59D96847848333D9F992E605B4C0C055EE0&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/room/enter?paras=qQSi%2BmWAskqEKwGH8Gpk7bC%2B4QGG/W0wxkDpo6USwiphNUYe0xIlhYwHfXn1A1MYccraez%2B2blOx%2BA6clH5/YfulCz0O87XaoQSWDDjQq5RsIcXbqJ%2BxBGcrndPr6EuP2XDVe8H7ztm8ZiZyq7mTC9R2TVjx2o3r6uL5TcOav4Jh7B0Rlkw9k0zY4871/Qr32En6Si19eKJdDdOr5SkKdy2NYh8kA17mzMYizw8x%2BjPIvZq6xV9FrA%3D%3D&sign=D700E30FB9F844C1462D378D7212FFF0585CE6FA&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/room/page?paras=ydKd2X0UQDDCM8txVfYsmqouLVlT8Hu%2BFX34HYOrjXIg8HiKtghVm0UpQpKQ1QDYDxEuCpp4sz0ilpf0BEWndlD5FnwaElkvWAsxzM29xSdJdD/UWfIaJzqw4Q74ZpCwveTAX53oKtGtwlVW/dBeVfOjyLHrOtNx/8shdFm8wDRST1OedoCT2yQzbHwKNktFvv1M/7lOM9I/0c39a2lhmsPxTQ45LL2fxoHeNA%3D%3D&sign=4A95C39F754E4EACEE908367521E265239CFB49C&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/room/question_page?paras=jSCBZ6CAi63xu1MZ3JFON7FyCKxVjl0vPDIPmme4G7nWilATVCKdyPisuF6KSWudSIWhcnyWk7hzUfeGpLIhznyJXyqMRtzcqzU5GC%2BBPZagm%2BSg3PiUj9PCL3cOcezwl%2BuxfzWySyPZql2eTQK2KcN0Mc8H6ZfLEogteK06dSBAlb7cZej0bZFMYpnIBmA8F8rAeAaRLxx1E8r3IdKolV7bACvhUuNMBhCjWg%3D%3D&sign=3A5F30DB3F4625C8CA1BE48E47FF2AB10BCACCE6&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/community/to_set?paras=M%2BG1vE4UyE5InXOMiDmofWvHZfonhU1sHqCKYvRrrsl57KqEBknrXwPR/J9R%2BWisJ92cJzVNqocV1tvKtZNpUIEoNida8keFpI%2BVfsh6EEHFdPO28VloNNzUn1MD12NmSVbWbn6MPeObuFbFrmCZCpTRg5dscuZncSLp%2BggHN4nPsYenaejnsv2Vk2m/PN2nKv1tKg%3D%3D&sign=A5FC6249FBDEB0A8B8439A548281BBEFBABBB0E0&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0', 'https://app.xuehu365.com/courses/my_order_list?paras=r1Ei9Qc/4O/86eQIWBZ2jiiiTWS6MVyDzmEsgy8anasFV9%2BdMOAP1NcUpK3vjMpbTNe7rGRuN3PVhFGUJLxOIgHxv7mwIfbjS9y9t1D2ZzQi76A6z1B5Gj5/UBudS1qBt2NkwXni09BtNW6B8UpRmcBr6uFQdxkg%2BAjsorH3CPmpYpitiN%2BnZTcyDvbYxZFRM5/cFb3d72g%3D&sign=4DABCE7EA56094BE64D473EDAC0EF5AB202B0604&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://app.xuehu365.com/client/browse/record?paras=q2KptMzEDsm%2BFopY0afA3tZZtxss02dLSm/cphBtDMt8El%2BP9JVLATFBJKxz5ty9VPjfz4h9jFayOyEbFfnqbBrIzQf9ExnCaSTorPxiIyi%2BXSIsEWCrPHfeT9eiIsw9SxvERy%2BN5yTo4BMzKZTv8uob/G60VV1gRBULriCtSk8yVRoBWJXa2khne9L/roJlLiUCNkD8Fpg%3D&sign=51623324B119D4CDB804B589D896901946CC7608&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0', 'https://app.xuehu365.com/version?paras=YWrL%2Bap3F5B0GizJl8Jc6hpHm4QMsy7cZu5KSQR81v806RwNQ6whAym6qP1SXAnZ88W3N4qZ5clF0nBonar0u2ERZ0sxzmpwo01bnJ6n%2B2ucfbZmO4m1j1/Y2OgItC9p821B5Qn0DaEszxPiosSmfkl9daRZjCGPc2OkS6OceLregSpv&sign=5AAB4326E49F2A0552D396633CDD0A3989258A04&appId=xuehu&ct=3&v=v1.0&ch=xuehu&cv=2.0.0',
        'https://api.xuehu365.com/intranet/order/order_list?searchUserName=jason', 'https://api.xuehu365.com/room/member/list?topicId=35', 'https://api.xuehu365.com/community/member/list?communityId=17', 'https://s.xuehu365.com/community/member/list?communityId=23&userId=200061&pageNo=1', 'https://s.xuehu365.com/room/tips/ranking?topicId=477&userId=200061', 'https://s.xuehu365.com/room/member/list?topicId=477&userId=200061&pageNo=1',
        'https://s.xuehu365.com/room/tips/ranking?topicId=35', 'https://s.xuehu365.com/community/info?communityId=17'
        ]

def sendmail(url,msg):
    import smtplib
    import string
    txt = url +'\n' + 'Error:' + msg.encode("utf-8")
    HOST = 'smtp.126.com'   ##定义SMTP主机
    SUBJECT = 'Interface failure!'   ##邮件主题
    TO = ['beam.l@xuehu365.com','506556658@qq.com']  ##收件地址
    FROM = 'a506556658@126.com'    ##发件地址
    BODY =string.join(("From: %s" %FROM,"To: %s" % TO, "Subject: %s" % SUBJECT,"",txt),"\r\n")     ##组装sendmail方法的邮件主题内容，每段内容以\r\n进行分隔
    try:
        server = smtplib.SMTP()   ##创建smtp()对象
        server.connect(HOST,25)   ##通过connenct方法链接smtp主机
        server.starttls()         ##启动安全传输模式
        server.login("a506556658@126.com","506556658@qq.com")    ##邮箱账号登录校验
        server.sendmail(FROM,TO,BODY)    ##邮件发送
        server.quit()    ##断开smtp链接
        return True
    except Exception,e:
        print "失败：" + str(e)
        return False


def getResult(url):
    list = []
    try:
        # ua ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81 (Edition Baidu)'   ##浏览器信息
        # request = urllib2.Request(url,headers={'User-Agent':ua})     ##伪装浏览器并连接 url
        # response = urllib2.urlopen(request)
        # html = response.read()
        # urljson = json.loads(html,encoding='utf-8')
        #if not int(urljson['result']) == 0:
        #    sendmail(url,urljson['msg'])
        data = json.load(urllib2.urlopen(url))
        #k = data['result']

        if not data['result'] == '0':
            sendmail(url,data['msg'])
        else:
            print url + ':True'
            return True

    except Exception,e:
        print "Error: " + str(e)
        sendmail(url,str(e))

def main():
    for i in URLS:
        getResult(i)
        time.sleep(2)

if __name__ == '__main__':
    main()
