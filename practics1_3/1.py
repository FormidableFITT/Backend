import smtplib
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'y.r.reutov@student.khai.edu'
smtp_password = '1frjrigxivgbcurfx'
from_address = 'y.r.reutov@student.khai.edu'
to_address = 'reeutov.z@gmail.com'
subject = 'Practic 1'
body = 'Practic 1 smtp '
smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
smtp_conn.starttls()
smtp_conn.login(smtp_username, smtp_password)
message = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{body}"
smtp_conn.sendmail(from_address, to_address, message)
smtp_conn.quit()
