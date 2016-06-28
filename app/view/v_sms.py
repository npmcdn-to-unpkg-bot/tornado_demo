# coding=utf-8
import datetime
from base import BaseRight
from models import SMS
from sqlalchemy import text
from common import base_config



class SMSList(BaseRight):
    def get(self):
        start_date = (datetime.datetime.now() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
        end_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.render('sms/list.html', start_date=start_date, end_date=end_date, user=self.get_current_user())


class SMSData(BaseRight):
    def post(self):
        parameters = self.get_args(['start_time', 'end_time', 'phone_number'], None)
        start_time = self.get_argument('start_time', None, True)
        end_time = self.get_argument('end_time', None, True)

        query = self.db.query(SMS)
        if parameters['phone_number']:
            query = query.filter(SMS.phone_number == parameters['phone_number'])
        if start_time:
            query = query.filter(SMS.create_at >= '%s 00:00:00' % start_time)
        if end_time:
            query = query.filter(SMS.create_at <= '%s 23:59:59' % end_time)
        query = query.order_by(SMS.id.desc())

        di_all_data = self.get_query(query)
        self.write(di_all_data)

