import streamlit as st
import pandas as pd
import base64
from src.scrap.scrap import get_df_url

def download_csv(df,fname):
     csv = df.to_csv(index=False)
     b64 = base64.b64encode(csv.encode()).decode() 
     href = f'<a href="data:file/csv;base64,{b64}" download="{fname}">Download csv</a>'
     return href


def main():
    st.title('Linkedin Finder')

    st.header('Find Linkedin urls from a list of prospects')


    uploaded_file = st.file_uploader("Upload a spreadsheet file of First Name; Last Name ;Company")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        st.write("There are " , len(df.index)," items in the file" )
        max_prospects = 5
        if st.button('Get prospects'):
            st.write('Working on the first '+ str(max_prospects) +' prospects')
            df = get_df_url(df,max_prospects)
            st.write(df)
            st.markdown(download_csv(df,'prospects.csv'), unsafe_allow_html=True)


if __name__ == "__main__":
    main()