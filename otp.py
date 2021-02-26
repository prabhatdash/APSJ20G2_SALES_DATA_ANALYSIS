import random
import smtplib
def otpgeneration(email):
    otp = str(random.randint(100000, 999999))
    print("#"*50)
    print("PLEASE WAIT WE ARE SENDING AN OTP TO YOUR MAIL ID...")
    SUBJECT = 'OTP FOR LOGIN'
    TEXT = 'YOUR OTP TO LOGIN IS:' + otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('group2@apsjorhat.org','apsj#12345678')
    message = 'Subject:{} \n\n{}'.format(SUBJECT,TEXT)
    s.sendmail('group2@apsjorhat.org',email, message)
    s.quit()
    print('OTP SENT SUCCESSFULLY!')
    print('Enter the OTP which has been sent to your email address')
    check = input()
    print("#"*50)
    if check == otp:
        count = 1
        return count
    else:
        count = 0
        return count