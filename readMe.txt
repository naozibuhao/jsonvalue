平时工作中有时候会遇到从一个json传中获取某些指定值

举例: 通过一个查询获取到一个包含用户名的json字符串,准备从这个返回接口里面提取用户名在下一步工作中使用,目前没找到合适的工具,所以写了这个
支持通用json格式数据提取
参数说明:
-h 帮助
-k json中的属性路径 例如 data.data.id  获取data下面的data下面的id的值
-f json字符串所在的文件路径 推荐使用此参数
-s json字符串 与-f同时存在时,以-s 为准,不建议使用此方式,如果数据量少的话手动查找即可,
-o 文件输出路径

举例说明:
 python .\jsonview.py -f json.txt -k data.data.id -o a.txt

