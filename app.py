import streamlit as st
import pandas as pd







def main():
    st.title('Linkedin Finder')

    st.header('This app get a spreadsheet with prospects and find thier Linkedin urls')


    uploaded_file = st.file_uploader("Upload a file with Name and company")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)


    st.write(len(df.index) )

if __name__ == "__main__":
    main()