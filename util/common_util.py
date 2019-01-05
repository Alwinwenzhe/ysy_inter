# Author:
# Data:
# Status
import datetime, time


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

    def not_contain(self,str1,str2):
        """
        判定st2不被包含
        :param str1: 目标字符串
        :param str2: 被包含主体
        :return:
        """
        flag = []
        st = str(str1).split(',')
        for i in st:
            if i in str2:
                flag.append('false')
            else:
                flag.append('true')
        if 'false' in flag:
            return False
        else:
            return True

    def get_tomorrow(self):
        """
        获取明天这个时间点
        :return: str格式的字符串
        """
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)  # 获取明天日期
        h_m = time.strftime(" %H:%M")
        return str(tomorrow) + str(h_m)

if __name__ == '__main__':
    cu = CommonUtil()
    now_time= cu.get_tomorrow()
    print(now_time)