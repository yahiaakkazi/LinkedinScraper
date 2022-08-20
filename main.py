from linkedin_api import Linkedin
from utils.utils import get_search_results,get_data,write_data_file
from getpass import getpass
import time

def main():
    mail = str(input("Please ur mail: "))
    password = getpass("Please ur pw: ")
    api = Linkedin(mail, password)
    keyword = str(input("What keyword to make data from: "))
    processed = get_search_results(api,keyword)
    data = get_data(api,processed)
    write_data_file(data)

if __name__ == '__main__':
    main()