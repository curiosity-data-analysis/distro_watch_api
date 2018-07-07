# imports
from bs4 import BeautifulSoup
import requests

'''
responsible function to collect the popularity data from the DistroWatch site. 
It is also responsible for generating .csv files for data analysis.
'''
def crawler_ranking():
	# requisition on the site that contains the ranking by popularity of the distributions
	page = requests.get("https://distrowatch.com/dwres.php?resource=popularity")
	# beautiful soup analyzes the generated request
	soup = BeautifulSoup(page.content, 'html.parser')
	# search for the table that contains the "NewsText" class name
	table = soup.find('td', attrs={'class':'NewsText'})
	# look for the columns inside the table
	rows = table.find_all('tr')
	# creation of .csv files for data analysis
	file_12_months = open("data/file_12_months.csv","a")
	file_6_months = open(".data/file_6_months.csv","a")
	file_3_months = open("data/file_3_months.csv","a")
	file_1_months = open("data/file_1_months.csv","a")
	# list that contains everything that was found inside the table on the site
	first_ranking = []
	# list with the ranking of 12, 6, 3 and 1 month
	total_ranking = []
	# created a list containing the rankings divided by 12, 6, 3 and 1 month
	list_12_months = []
	list_6_months = []
	list_3_months = []
	list_1_months = []
	# list with all distributions
	list_distro = []
	# add everything found in the first find
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		first_ranking.append([ele for ele in cols if ele])

	# adds in the lists of 12,6,3 and 1 month
	for x in range(3,len(first_ranking)):
		total_ranking.append(first_ranking[x])
	for x in range(0,311):
		list_12_months.append(total_ranking[x])
	for x in range(312,623):
		list_6_months.append(total_ranking[x])
	for x in range(624,935):
		list_3_months.append(total_ranking[x])
	for x in range(936,1247):
		list_1_months.append(total_ranking[x])
	
	# Adds only the distribution names in the list so that the distribution data is collected
	for x in range(0,311):
		list_distro.append(list_12_months[x][0])

	# Creating .csv files with data
	file_12_months.write("position,distribution,hit_ranking\n")
	for value,distribution in enumerate(list_12_months):
		distribution = list_12_months[value][0]
		hit_ranking = list_12_months[value][1]
		file_12_months.write(str(value+1)+","+str(distribution)+","+str(hit_ranking)+"\n")

	file_6_months.write("position,distribution,hit_ranking\n")
	for value,distribution in enumerate(list_6_months):
		distribution = list_6_months[value][0]
		hit_ranking = list_6_months[value][1]
		file_6_months.write(str(value+1)+","+str(distribution)+","+str(hit_ranking)+"\n")

	file_3_months.write("position,distribution,hit_ranking\n")
	for value,distribution in enumerate(list_3_months):
		distribution = list_3_months[value][0]
		hit_ranking = list_3_months[value][1]
		file_3_months.write(str(value+1)+","+str(distribution)+","+str(hit_ranking)+"\n")

	file_1_months.write("position,distribution,hit_ranking\n")
	for value,distribution in enumerate(list_1_months):
		distribution = list_1_months[value][0]
		hit_ranking = list_1_months[value][1]
		file_1_months.write(str(value+1)+","+str(distribution)+","+str(hit_ranking)+"\n")

	return list_distro


'''
responsible function to collect data from existing distributions on the DistroWatch site
Under development
'''
def crawler_distribution():
	list_distro = crawler_ranking()
	

if __name__ == '__main__':
	crawler_ranking()
