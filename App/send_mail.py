from email.message import EmailMessage
import ssl
import smtplib


def send(receiver, email_receiver, check_in, check_out, cart, total):
    email = 'hoteltt11@gmail.com'
    password = "casn fvwc bvqv odcd"
    info = ""
    for c in cart.values():
        info += "{} phòng {},".format(c["quantity"], c["name"])

    info = info[0:(len(info) - 1)]
    subject = "Thông tin đơn đặt phòng"
    body = """
    Chào {},
    Bạn vừa đặt phòng thành công bên khách sạn Hotel T&T của chúng tôi. Thông tin đơn đặt phòng bao gồm:
    Ngày nhận phòng: {}
    Ngày trả phòng: {}
    Các phòng đã đặt: {}
    Tổng tiền: {}
    Cảm ơn quý khách đã chọn  Hotel T&T, chúc quý khách có một kỳ nghỉ vui vẻ.
    """.format(receiver, check_in, check_out, info, total)

    em = EmailMessage()
    em['From'] = email
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email_receiver, em.as_string())


def send2(receiver, email_receiver, check_in, check_out, details, total):
    email = 'hoteltt11@gmail.com'
    password = "casn fvwc bvqv odcd"
    info = ""
    for d in details:
        info += "Phòng {}: {} \n".format(d, details[d]["name"])

    subject = "Thông tin đơn đặt phòng"
    body = """
    Chào {},
    Bạn vừa đặt phòng thành công bên khách sạn Hotel T&T của chúng tôi. Thông tin đơn đặt phòng bao gồm:
    Ngày nhận phòng: {}
    Ngày trả phòng: {}
    Các phòng đã đặt:\n{}Tổng tiền: {}
    Cảm ơn quý khách đã chọn  Hotel T&T, chúc quý khách có một kỳ nghỉ vui vẻ.
    """.format(receiver, check_in, check_out, info, total)

    em = EmailMessage()
    em['From'] = email
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email_receiver, em.as_string())