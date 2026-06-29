import streamlit as st

st.title("🎤 Voice-Based Concept Understanding Analyzer")

st.write("Enter spoken text (or simulate voice output)")

text = st.text_input("User Response:")

if st.button("Analyze Understanding"):
    if text:
        text = text.lower()

        if "machine learning" in text:
            st.success("Score: 90/100 - Strong Understanding 👍")
            st.balloons()
        elif "ai" in text or "artificial intelligence" in text:
            st.info("Score: 70/100 - Moderate Understanding 🙂")
        else:
            st.warning("Score: 40/100 - Needs Improvement ⚠️")
    else:
        st.error("Please enter text first")