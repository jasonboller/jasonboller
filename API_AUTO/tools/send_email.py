import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 邮件发送的用户名和密码  常识：第三方授权码
_user = "604308925@qq.com"
_pwd = "ihlwxwvejvinbeie"

now = time.strftime('%Y-%m-%d_%H_%M_%S') # 获取时间戳
class sendEmail:
    def send_email(self, email_to, filepath):
        # email_to   收件方
        # filepath   你要发送附件的地址
        # 如名字所示Multipart就是分多个部分
        msg = MIMEMultipart()
        msg["Subject"] = now + "jason的测试报告"
        msg["From"] = _user
        msg["To"] = email_to

        # ---这是文字部分---
        part = MIMEText("这是自动化测试结果，请查收！")
        msg.attach(part)

        # ---这是附件部分---只能发一个附件
        part = MIMEApplication(open(filepath, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=filepath)
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.qq.com", timeout=25) # 连接smtp邮件服务器，端口默认是25
        s.login(_user, _pwd) # 登录服务器
        s.sendmail(_user, email_to, msg.as_string()) # 发送邮件
        s.close()

if __name__ == '__main__':
    sendEmail().send_email("1030540742@qq.com", r"D:\OrangeProject\API_AUTO\test_result\html_report\test_api.html")
