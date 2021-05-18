import streamlit as st
import pandas as pd
import base64
from src.scrap.scrap import get_df_url

def download_csv(df,fname,button_name):
     csv = df.to_csv(index=False)
     b64 = base64.b64encode(csv.encode()).decode() 
     href = f'<a href="data:file/csv;base64,{b64}" download="{fname}">{button_name}</a>'
     return href


def main():
    st.title('Linkedin Finder')

    st.header('Generate a list of Linkedin urls from a list of leads')


    uploaded_file = st.file_uploader("Upload a spreadsheet file of First Name; Last Name ;Company")
    st.markdown(download_csv(pd.DataFrame([], columns = ['First Name', 'Last Name','Company']),'linkedin_finder.csv',"Download Template"), unsafe_allow_html=True)
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        st.write("There are " , len(df.index)," items in the file" )
        if st.button('Get leads (Free)'):
            max_leads = 5
            st.write('Working on the first '+ str(max_leads) +' leads')
            df = get_df_url(df,max_leads)
            st.write(df)
            st.markdown(download_csv(df,'linkedin_finder.csv',"Download csv"), unsafe_allow_html=True)
        if st.button('Get leads (Premium)'):
            max_leads = 100
            email = st.text_input('Email Address')
            st.write(email)
            df = get_df_url(df,max_leads)
            st.write('Send email to boaz@descalo.com')



if __name__ == "__main__":
    main()