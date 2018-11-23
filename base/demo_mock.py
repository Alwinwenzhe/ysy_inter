#Author:
#Data:
#Status
import mock

def mock_test(mock_method,method,url,request_data,response_data):
    mock_method = mock.Mock(response_data)          #通过mock得到返回值赋值给被模拟方法
    res = mock_method(method,url,request_data)      #被模拟方法传入其参数
    return res