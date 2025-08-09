import streamlit as st
import requests
st.set_page_config(page_title="SCHOLO", page_icon="💡", layout="centered")
st.title("💡 SCHOLO")
st.write("Get  research papers on your topic.")
if "history" not in st.session_state:
        st.session_state.history=[]
topic = st.text_input("Enter a topic  of your interest")
if st.button("Find Research Papers") and topic:


    st.subheader("📚 Relevant Research Papers")
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={topic}&limit=5&fields=title,url"
    response = requests.get(url)

    if response.status_code == 200:
        papers = response.json().get("data", [])
        if papers:
            for paper in papers:
                st.markdown(f"- [{paper['title']}]({paper['url']})")
        else:
            st.warning("No citations available. Try with a different topic.")
    else:
        st.error("Error  while fetching citations.")
if st.session_state.history:
    st.subheader("📜 Search History")
    for past_topic, papers in reversed(st.session_state.history):
        st.markdown(f"**Topic:** {past_topic}")
        for title, link in papers:
            st.markdown(f"- [{title}]({link})")
        st.markdown("---")
