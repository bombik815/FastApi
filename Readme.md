# Запуск аfastApi приложенеи uvicorn

> uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Запуск Celery

> celery -A app.tasks.celery:celery worker --loglevel=INFO --pool=solo

# Запуск celery flower

> celery -A app.tasks.celery:celery flower

# Запускаем локальный мэйл сервер

> python -m smtpd -c DebuggingServer -n localhost:1025

2. в tasks.py вместо STMP_SSL используем STMP без аутентификации

> with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
> server.send_message(msg_content)

## в окне, в котором запустили тестовый smtp сервер, смотрим результаты. Должно появляться тело письма, как показано на примере ниже

```
---------- MESSAGE FOLLOWS ----------
b'Subject: Booking confirmation'
b'From: test@gmail.com'
b'To: test123@gmail.com'
b'Content-Type: text/html; charset="utf-8"'
b'Content-Transfer-Encoding: 7bit'
b'MIME-Version: 1.0'
b'X-Peer: 127.0.0.1'
b''
b''
b'        <h1>Please confirm booking</h1>'
b"        You've booked hotel from 2023-07-06 till 2023-07-20"
b'        '
------------ END MESSAGE ------------
```

