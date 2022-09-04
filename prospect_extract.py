import json
import tldextract
import pandas as pd
import spacy
from dns import resolver
import smtplib
from func_timeout import *
from imap_tools import *
import re
from bs4 import BeautifulSoup

filename=input("enter export file name")

jsonfile = open('prospects.json','r').read()
load_json = json.loads(jsonfile)

elements = load_json


first_names = []
last_names = []
positions = []
domains = []
companies = []
social_links = []

for ele in elements:
	try:
		first_name = ele["name"]["first"]
		last_name = ele["name"]["last"]

		position = ele["job_title"]["title"]


		domain = tldextract.extract(ele["emails"][0]["address"])
		company = domain.domain
		domain = (domain.domain+"."+domain.suffix).strip()


		social_link = ele["social_link"]
		if first_names != None and first_names != "" and first_names != " " and last_names!= None and last_names != "" and last_names != " " and domain not in ["gmail.com","gmail","yahoo.com","aol.com"] and len(first_name) > 3 :

			first_names.append(first_name)
			last_names.append(last_name)
			positions.append(position)
			domains.append(domain)
			social_links.append(social_link)
			companies.append(company)
	except:
		pass


pd_dataframe = pd.DataFrame({
 "first_name":pd.Series(first_names),
 "last_name":pd.Series(last_names),
 "company":pd.Series(companies),
 "domain":pd.Series(domains),
 "position":pd.Series(positions),
 "linkedin_profile":pd.Series(social_links)

 }) 	


pd_dataframe.to_csv(filename,index=False)

print(f"saved in file {filename}")