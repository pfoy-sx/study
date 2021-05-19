#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeBackupsRequest
from aliyunsdkrds.request.v20140815 import DescribeBinlogFilesRequest
import json
import urllib
import datetime



# 获得时间需要备份的时间范围
def getdate():
        today_time = datetime.datetime.now()
        date1 = datetime.datetime.strftime(today_time, '%Y-%m-%d')  # +'T00:00:00Z'
        yes_time = today_time + datetime.timedelta(days=-2)
        date2 = datetime.datetime.strftime(yes_time,'%Y-%m-%d')  #  +'T00:00:00Z'

        global start_date
        global end_date
        start_date = date2
        end_date = date1

        return 0


# 拉取指定db_instanceid的备份文件
def downfullbackupfile(db_instanceid):
        startdate = start_date+'T00:00Z'
        enddate = end_date+'T00:00Z'
        clt = client.AcsClient('0ozYjkWe123456','kSVNVc89123456SY5tkFpUFXwPH','cn-hangzhou')
        request = DescribeBackupsRequest.DescribeBackupsRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeBackups')
        request.set_DBInstanceId(db_instanceid)
        request.set_StartTime(startdate)
        request.set_EndTime(enddate)
        result = clt.do_action(request)
        s=json.loads(result)
        list = s['Items']['Backup']
        for i in list:
                DBInstanceId = i['DBInstanceId']
                url = i['BackupDownloadURL']
                idx = url.index('tar.gz')
                filename = url[7:idx+6].replace('/','_')
                filename = "/backup/databackup/%s_%s" % (DBInstanceId,filename)
                urllib.urlretrieve(url,filename)



# 拉取指定db_instanceid的备份文件
def downbinlogfile(db_instanceid):
        startdate = start_date+'T00:00:00Z'
        enddate = end_date+'T00:00:00Z'
        clt = client.AcsClient('0ozYjkWeiHULnOjK','kSVNVc89zdFIMw4VPSY5tkFpUFXwPH','cn-hangzhou')
        request = DescribeBinlogFilesRequest.DescribeBinlogFilesRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeBinlogFiles')
        request.set_DBInstanceId(db_instanceid)
        request.set_StartTime(startdate)
        request.set_EndTime(enddate)
        result = clt.do_action(request)
        s=json.loads(result)
        list = s['Items']['BinLogFile']
        for i in list:
                DBInstanceId = db_instanceid
                url = i['DownloadLink']
                idx = url.index('.tar?OSSAccessKeyId')
                filename = url[7:idx+4].replace('/','_')
                filename = "/backup/binlogbackup/%s_%s" % (DBInstanceId,filename)
                urllib.urlretrieve(url,filename)


#需要备份的db_instanceid
def dblist():
        dblist = ['rm-bp1tg9vcgd0z775jj11pfi','rdss5r8cmjgisdf52zkx290']
        for db in dblist:
                downfullbackupfile(db)
                downbinlogfile(db)

try:
        if __name__ == "__main__":
                getdate()
                dblist()
except Exception as e:
        print(e)