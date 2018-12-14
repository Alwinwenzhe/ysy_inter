# Author:
# Data:
# Status

import smtplib
from email.mime.text import MIMEText
from util.operate_yaml import OperateYaml


class SendEmail(object):

    def __init__(self):
        self.yaml_data = OperateYaml()

    def send_email(self, user_list, sub, content):
        """
        发送邮件
        :param user_list: 接收人
        :param sub: 邮件主题
        :param content: 内容
        :return:
        """
        email_host = 'smtp.163.com'
        send_user = '15828022852@163.com'
        password = '225410weyd'
        user = "Alwin" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')  # 邮件内容及编码
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)  # 接收人通过“；”拼接
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        try:
            server.sendmail(user, user_list, message.as_string())
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')
        server.close()

    def send_main(self, pass_list, fail_list):
        '''
        发送邮件
        :param pass_list: 通过的用例集合
        :param fail_list: 失败的用例集合
        :return:
        '''
        p_count = float(len(pass_list))
        f_count = float(len(fail_list))
        sum_count = p_count + f_count
        p_percent = "%.2f%%" % (p_count / sum_count * 100)  # %.2f 表示2位小数，%%代表百分号
        f_percent = "%.2f%%" % (f_count / sum_count * 100)
        userlist = self.yaml_data.read_yaml()['email']['user_list']
        sub = self.yaml_data.read_yaml()['email']['sub']
        content = self.yaml_data.read_yaml()['email']['content'].format(s1=sum_count, s2=p_count, s3=f_count,
                                                                        s4=p_percent, s5=pass_list, s6=fail_list)
        self.send_email(userlist, sub, content)


if __name__ == '__main__':
    pass
