import streamlit as st
import pandas as pd
import base64
from src.scrap.scrap import get_df_url

def download_csv(df,fname,button_name):
     csv = df.to_csv(index=False)
     b64 = base64.b64encode(csv.encode()).decode() 
     href = f'<a href="data:file/csv;base64,{b64}" download="{fname}">{button_name}</a>'
     return href

st.set_page_config(
     page_title="Linkedin Finder - Generate Leads Faster",
     page_icon="crown",
     layout="wide",
     initial_sidebar_state="expanded",)

def main():
    st.title('Linkedin Finder')

    st.header('A Must-Have App for Networking: Effortlessly Generate LinkedIn URLs from Name Lists!')


    uploaded_file = st.file_uploader("Upload a spreadsheet file of First Name; Last Name ;Company")
    st.markdown(download_csv(pd.DataFrame([], columns = ['First Name', 'Last Name','Company']),'linkedin_finder.csv',"Download Template"), unsafe_allow_html=True)
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        st.write("There are " , len(df.index)," items in the file" )
        if st.button('Get leads (Free)'):
            max_leads = 150
            st.write('Working on the first '+ str(min(max_leads,len(df.index))) +' leads')
            df = get_df_url(df,max_leads)
            st.write(df)
            st.markdown(download_csv(df,'linkedin_finder.csv',"Download csv"), unsafe_allow_html=True)
        #if st.button('Get leads (Premium)'):
            #max_leads = 100
            #email = st.text_input('Email Address')
            #st.write(email)
            #df = get_df_url(df,max_leads)
            #st.write('Send email to boaz@descalo.com')'''



if __name__ == "__main__":
    main()
