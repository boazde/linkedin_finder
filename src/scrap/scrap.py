import pandas as pd
from urllib.parse import urlparse
try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")


def get_linkedin_url(query):
    urls = search(query, tld="com", num=10, stop=10, pause=2)
    for url in urls:
        o = urlparse(url)
        if '/in/' in o.path and 'linkedin' in o.netloc:
            return url
    return ''

def get_google_urls(query):
    urls = search(query, tld="com", num=10, stop=10, pause=2)
    for url in urls:
        print(url)

def get_df_url(df, max_rows):
    df = df.head(max_rows)
    df['linkedin'] = df.apply(lambda row: get_linkedin_url(f"{row['First Name'] if pd.notna(row['First Name']) else ''} {row['Last Name'] if pd.notna(row['Last Name']) else ''} {row['Company'] if pd.notna(row['Company']) else ''} linkedin"), axis=1)
    return df

def main():
    get_google_urls('James Child NyC Linkedin')

if __name__ == "__main__":
    main()
