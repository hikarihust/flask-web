import os
from typing import List
from requests import Response, post
import gettext


class MailGunException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Mailgun:
    FROM_TITLE = 'Pricing Service'
    
    @classmethod
    def send_email(
        cls, email: List[str], subject: str, text: str, html: str
    ) -> Response:
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        domain = os.environ.get('MAILGUN_DOMAIN', None)
        from_email = f'do-not-reply@{domain}'

        if api_key is None:
            raise MailGunException(gettext('mailgun_failed_load_api_key'))

        if domain is None:
            raise MailGunException(gettext('mailgun_failed_load_domain'))

        response = post(
            f'https://api.mailgun.net/v3/{domain}/messages',
            auth=('api', api_key),
            data={
                'from': f'{cls.FROM_TITLE} <{from_email}>',
                'to': email,
                'subject': subject,
                'text': text,
                'html': html,
            },
        )
        if response.status_code != 200:
            # print(response.status_code)
            # print(response.json())
            raise MailGunException('An error occurred while sending e-mail.')
        return response
