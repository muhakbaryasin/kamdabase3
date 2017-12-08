from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import func

from ..models.mymodel import TblPatient
from collections import OrderedDict

import logging
log = logging.getLogger(__name__)

@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
	try:
		group_of_age = ['1-17','18-44','45-64','65-84','85-95']
		result = OrderedDict([])
		race = ('white', 'black', 'hispanic', 'asian pacific islander', 'native american', 'other', 'missing')
		
		for each_group in group_of_age:
			result[each_group] = OrderedDict([])
			split_ = each_group.split('-')
			min_ = int(split_[0])
			max_ = int(split_[1])
			
			query_result = request.dbsession.query(TblPatient.patient_race, func.count(TblPatient.patient_race)).group_by(TblPatient.patient_race).filter(TblPatient.patient_age >= min_, TblPatient.patient_age <= max_).all()
			tpg = 0
			
			for row in query_result:
				tpg += row[1]
				result[each_group][row[0]] = row[1]
			
			result[each_group]['total'] = tpg
		
	except Exception as e:
		log.exception(str(e))
		return {'code': 'error', 'message': str(e), 'content' : ''}
	return {'code': 'ok', 'message': '', 'content' : result, 'race' : race}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_kamdabase3_db" script
	to initialize your database tables.  Check your virtual
	environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
	database server referred to by the "sqlalchemy.url" setting in
	your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
