import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser


class DataScraper (HTMLParser):
	"""this class scrapes the given webpage for table data, which can be stored into a textfile as a tab-spaced table"""
	
	def start(self, tableClass, url):
		"""initialize scraper given class name of table to look for and url"""
		self.read = False
		self.startFetch = False
		self.data = []		#use this to get scraped data
		self.tableClass = tableClass;	#scraper will look for the table with this class
		#once opened, urlHandle acts as a file for reading
		urlHandle = urllib.request.urlopen(url)
		self.feed(str(urlHandle.read()))
		self.data = tuple(self.data)
		
	
	def handle_starttag(self, tag, attrs):
		"""data to be scraped is contained in a table belonging to a particular class"""
		if tag == "table":
			#attrs is a list of tuples, here for ease of access its converted to a dict type
			attrs = self.handle_attrs(attrs)
			if "class" in attrs:
				if attrs["class"] == self.tableClass:
					self.startFetch = True
		elif tag == "tr":
			self.data.append([])
		elif (tag == "td" or tag == "th") and self.startFetch == True:
			self.read = True
	
	
	def handle_data(self, data):
		if self.read == True:
			self.data[-1].append(data)
	
	
	def handle_endtag(self, tag):
		if tag == "td" or tag == "th":
			self.read = False
		if tag == "table":
			self.startFetch = False

			
	def handle_attrs(self, attrs):
		attrDict = {}
		for attr in attrs:
			attrDict[attr[0]] = attr[1]
		return attrDict


	def saveData(self):
		"""this dumps the data into a text file separating columns by tabs"""
		with open('ds_data.txt','w') as f:
			for line in self.data:
				if len(line) == 0:
					continue
				for i in line:
					f.write(i.strip() + '\t')
				f.write('\n')




