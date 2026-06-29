import streamlit as st

st.title("🎤 Voice-Based Concept Understanding Analyzer")

st.write("Enter spoken text (or simulate voice output)")

text = st.text_input("User Response:")

if st.button("Analyze Understanding"):

    if text:
        text_low = text.lower()

        if "machine learning" in text_low:
            result = "90/100 - Strong Understanding 👍"
            st.success(result)

        elif "ai" in text_low or "artificial intelligence" in text_low:
            result = "70/100 - Moderate Understanding 🙂"
            st.info(result)

        else:
            result = "40/100 - Needs Improvement ⚠️"
            st.warning(result)

        pdf_file = create_pdf(text, result)

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_file,
            file_name="report.pdf",
            mime="application/pdf"
        )

    else:
        st.error("Please enter text first")