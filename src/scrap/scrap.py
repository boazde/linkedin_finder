import pandas as pd
import re
from urllib.parse import urlparse
#search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
#search (query,  tld='com', lang='en', tbs='0', safe='off', num=2, start=0, stop=2, domains=None, pause=2.0, tpe='', country='', extra_params=None, user_agent=None)
try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")


def get_google_urls(query):
    urls = search(query, tld="com", num=10, stop=10, pause=1,extra_params={'site':'linkedin.com'} )
    return urls
    

def parse_linkedin_url(urls):
    url=''
    for u in urls:    
        o = urlparse(u)    
        if '/in/' in o.path and 'linkedin' in o.netloc :
            url=u
    return url

def print_urls(urls):
    for a in urls:
        print(a)

def get_df_url(df, max_rows):
    df=df.head(max_rows)
    #df['linkedin'] =df.apply(lambda row : parse_linkedin_url(get_google_urls(row['First Name']+ row['Last Name']+row['Company']+ 'linkedin')), axis = 1)
    df['linkedin'] =df.apply(lambda row : parse_linkedin_url(get_google_urls(row[0]+row[1]+row[2] + '   linkedin')), axis = 1)
    return df


def main():
    df = pd.read_csv('data.csv')
    get_df_url(df,5)
    df.to_csv('data_out.csv')


if __name__ == "__main__":
    main()

