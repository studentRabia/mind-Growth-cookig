import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset for Chefs & Restaurants", page_icon="🍽️")

# Title & Introduction
st.title("🍽️ Growth Mindset Challenge: Culinary Success 🚀")
st.header("Welcome to Your Culinary Growth Journey! 👨‍🍳👩‍🍳")
st.write("Cooking is an art, and every challenge in the kitchen is a chance to learn. Whether you're a chef, restaurant owner, or food lover, embrace challenges and grow! 🎯")

# Daily Motivation Quote
st.header("💡 Today's Growth Mindset Quote")
st.write(
    '"A recipe has no soul. You, as the cook, must bring soul to the recipe." - Thomas Keller'
)

# Challenge Section
st.header("🔧 What’s Your Culinary Challenge Today?")
cooking_challenge = st.text_input("Describe a cooking or restaurant challenge you're facing:")

if cooking_challenge:
    st.success(f"You're facing: {cooking_challenge}. Keep experimenting and refining your skills! 🍳🔥")
else:
    st.warning("Tell us about your culinary challenge to get started!")

# Reflection Section
st.header("🔍 Reflect on Your Culinary Learning")
reflection = st.text_area("Write about a lesson learned from a recent challenge:")

if reflection:
    st.success(f"✨ Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your learning moments.")

# Achievements Section
st.header("🏆 Celebrate Your Culinary Wins! 🥇")
achievement = st.text_input("Share a dish you perfected or a milestone in your restaurant:")

if achievement:
    st.success(f"🎉 Amazing! Your achievement: {achievement} 👏")
else:
    st.info("Every small win matters! Share your culinary success story! 🍽️")

# Footer
st.write("- - -")
st.write("🌟 Keep believing in yourself. Growth is a journey, not a destination! ✨")
st.write("© Created by Rabia 👑")
