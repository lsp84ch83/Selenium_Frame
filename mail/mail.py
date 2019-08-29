#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/6/8 14:16
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def senmail(user, password, now, *receive_letter):
    # 发送邮箱服务器
    mail_host = "smtp.qq.com"
    # 发送邮箱用户/密码
    mail_user = user
    mail_pass = password

    # 接收邮箱,可定义多个接收人
    receivers = []
    for mailbox in receive_letter:
        receivers.append(mailbox)
    print(receivers)
    #receivers = receive_letter 

    # 发送邮件主题
    subject = '测试报告'
    msgRoot = MIMEMultipart('related')
    # 邮件正文内容
    msgRoot.attach(MIMEText('系统邮件，请勿回复！！！', 'plain', 'utf-8'))
    msgRoot['Subject'] = Header(subject, 'utf-8')
    # 添加附件
    sendfile = open("./report/%s_result.html" % now, 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s_result.html"' % now
    msgRoot.attach(att)

    try:
        # 连接发送邮件
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, msgRoot.as_string())
        print('发送成功')
    except smtplib.SMTPException as err:
        print('发送失败')
        print(str(err))
    finally:
        smtpObj.quit()

if __name__ == '__main__':
    senmail(user, password, now, *receive_letter)
