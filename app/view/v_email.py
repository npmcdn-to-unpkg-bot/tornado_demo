# coding=utf-8
from base import BaseRight
from models import Email


class EmailList(BaseRight):
    def get(self):
        self.render('email/list.html', user=self.get_current_user())


class EmailData(BaseRight):
    def post(self):
        parameters = self.get_args(['address'], None)
        print '--', parameters
        query = self.db.query(Email)
        if parameters['address']:
            query = query.filter_by(address=parameters['address'])

        query = query.order_by(Email.id.desc())

        di_all_data = self.get_query(query)

        self.write(di_all_data)
