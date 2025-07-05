import streamlit as st
from transformers import pipeline

# Load GPT-2 text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Streamlit UI setup
st.set_page_config(page_title="Daily Motivation Generator", layout="centered")
st.title("🌟 Daily Motivation Generator")
st.write("Select your mood and get an uplifting quote!")

# Mood options
moods = [
    "Feeling anxious",
    "Need focus",
    "Low energy",
    "Looking for inspiration",
    "Feeling overwhelmed",
    "Feeling lost",
    "Want to start the day strong"
]

selected_mood = st.selectbox("How are you feeling today?", moods)

if st.button("Generate Motivation"):
    with st.spinner("Generating motivation..."):
        # Create the prompt
        prompt = f"A motivational message for someone who is {selected_mood.lower()}: "

        # Generate text
        result = generator(
            prompt,
            max_length=60,
            num_return_sequences=1,
            temperature=0.95,  # higher = more creativity
            top_k=50,          # more variety
            top_p=0.95
        )

        # Remove the prompt from the result
        full_text = result[0]['generated_text']
        message = full_text.replace(prompt, "").strip()

        # Show the result
        st.success("Here's your motivational quote:")
        st.markdown(f"> *{message}*")
