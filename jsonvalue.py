#coding=utf-8
'''
@Author: your name
@Date: 2020-06-17 19:09:02
@LastEditTime: 2020-06-17 23:51:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode\jsonview.py
'''

import json
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def jsonvalue(str,key):
    result = []
    saa = str
    path = key
    paths = path.split('.')
    s = json.loads(saa)
    for i in range(len(paths)-1):
        s = s[paths[i]]
        if isinstance(s,list): # 如果发现是list 那么退出
            break
        
    key =  paths[len(paths)-1]
    if isinstance(s,list):
        for item in s:
            result.append(item[key])
            print item[key]
    if isinstance(s,dict):
        result.append(json.dumps(s[key], encoding="UTF-8", ensure_ascii=False))
        #print json.dumps(s[key], encoding="UTF-8", ensure_ascii=False)
    return result
def readfile(filepath):
    f = open(filepath,'r')
    str = ''
    for lines in f:
        str = str +lines.replace('\n','')
    return str

    
def wf(filepath,msg):
    f = open(filepath,'a+')
    f.write(msg+"\n")
    f.close() 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--jsonstr', help=u"json字符串")
    parser.add_argument('-f', '--filepath', help=u"文件路径")
    parser.add_argument('-k', '--keypath', help=u"需要获取属性的路径,需要已.分开 例如 data.data.id",)
    parser.add_argument('-o', '--output', help=u"导出到文件",)
    args = parser.parse_args()

    filepath = args.filepath
    jsonstr = args.jsonstr
    key = args.keypath
    output= args.output
    ss = ''
    if filepath !=None :
       ss = readfile(filepath) 
       ss = ss.replace(' ','')
       ss = unicode(ss, "utf-8")
    if key is None:
        print u"输入python jsonview.py -h 查看帮助"
        quit()
    if jsonstr is not None:
        ss = jsonstr
    

    result = jsonvalue(ss,key)
    if output is not None:
        for s in result:
            wf(output,s)
