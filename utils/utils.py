from tqdm import tqdm
import time

def get_search_results(api=None,keywords = "rh",current_company = None):
    search_results = api.search_people(keywords=keywords, connection_of=None, network_depths=None, current_company=current_company, past_companies=None,
    nonprofit_interests=None, profile_languages=None, regions=None, industries=None, schools=None, contact_interests=None, 
    service_categories=None, include_private_profiles=False, keyword_first_name=None, keyword_last_name=None, keyword_title=None, 
    keyword_company=None, keyword_school=None, network_depth=None, title=None)
    processed = [(i.get("urn_id",""),i.get("public_id","")) for i in search_results]
    return processed[0:50]

def get_data(api= None,processed=None):
    data = []
    for i in tqdm(processed):
        try:
            d = {}
            l = api.get_profile(public_id=i[1], urn_id=i[0])
            d["fname"]=l.get("firstName","").lower()
            d["lname"]=l.get("lastName","").lower()
            d["company"]= l.get("experience","")[0].get("companyName","").lower()
            data.append(d)
        except:
            continue
    return data

def write_data_file(data):
    tim = time.time()//5
    with open('data-{}.txt'.format(str(tim)),"w+") as text_file:  
        for iter in tqdm(data):
            fname, company, mail = iter["fname"], iter["company"], "{}.{}@{}.com".format(iter["fname"],iter["lname"],iter["company"])
            text_file.write("{} {} {}".format(fname,company,mail)+'\n')
    print('data-{}.txt'.format(str(tim))+ " has all data")