# Author:
# Data:
# Status

class CommonUtil(object):
    '''
    通用工具包
    '''

    def is_contain(self, str1, str2):
        """
        判定包含关系
        :param str1: 目标字符串
        :param str2: 被包含主体
        :return: True或false
        """
        # if isinstance(str1,unicode):           因python3中str对应的就是python2中的unicode，所以python3中没有nicode
        #     str1 = str1.encode('unicode-escape').decode('string-secape')
        flag = []
        st = str(str1).split(',')
        for i in st:
            if i in str2:
                flag.append('true')
            else:
                flag.append('false')
        if 'false' in flag:
            return False
        else:
            return True
