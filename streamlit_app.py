import streamlit as st
from agent_recommender import get_movie_recommendations

st.set_page_config(page_title="Movie Recommender Agent", layout="centered")

st.title("MOVIE RECOMMENDER AGENT")
st.write("Enter your current mood or genre preference to receive movie recommendations.")

user_input = st.text_input("your mood or genre preference", "")

if st.button("RECOMMEND MOVIES") and user_input:
    with st.spinner("Finding the best matches for your mood..."):
        response = get_movie_recommendations(user_input)
        st.subheader("RECOMMENDATIONS")
        st.markdown(f"Here are three {user_input.lower()} movies that I recommend:")

        # Parse and show each line as a box
        for line in response['output'].split("\n"):
            if line.strip():
                st.markdown(
                    f"""
                    <div style="background-color:#f0f2f6;padding:12px 15px;border-radius:8px;margin:8px 0;">
                        <p style="margin:0;font-size:15px;">{line}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )