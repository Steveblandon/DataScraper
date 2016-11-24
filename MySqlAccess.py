import pymysql 

class MySqlAccess(object):
	def __init__(self,hostname,username,password,database):
		self.conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
	
	def query(self, que):
		self.conn.cursor().execute(que)