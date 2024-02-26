import streamlit as st
import os

def main():
    st.set_page_config(
        page_title = "Pandas Apps",
        page_icon = "🎛️",   # :bar_chart:
        layout = "wide",
        initial_sidebar_state="expanded"
    )

    with st.sidebar:
        # st.info("Select a page above.")
        st.write(
            "<small>**About.**  \n</small>",
            "<small>*blueholelabs*, Feb. 2024  \n</small>",
            unsafe_allow_html=True,
        )
    
    # main page
    st.title("Welcome to the Pandas Dashboard Apps")
    st.divider()

    st.markdown("""
    <style>
    .custom-font {
        font-size:20px !important;
        font-weight: bold;
        
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="custom-font">App1. Adidas Interactive Sales Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-font">App2. SuperStore Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-font">App3. US Population Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-font">App4. Sales Dashboard</p>', unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()