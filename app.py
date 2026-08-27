import datetime
import time
import streamlit as st
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Happy Birthday Archana! ✨",
    page_icon="🌸",
    layout="centered"
)

# --- CUSTOM THEME STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1, h2, h3, h4 {
        color: #D1477F !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.3);
    }
    .stButton>button:hover {
        background-color: #FF1493;
        color: white;
        box-shadow: 0px 6px 15px rgba(255, 20, 147, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- TITLE AREA ---
st.title("✨ Something Special For You, Archana ✨")
st.write("A digital surprise crafted with love and code.")

# --- HARD TARGET DATE (SEPTEMBER 3, 2026 12:01 AM IST) ---
target_date = datetime.datetime(2026, 9, 3, 0, 1, 0)

# Fetch exact Live Current IST time
now_utc = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)

# STRICT LOCK CONDITION
# Ippudu absolute logic condition verify chestundi. True unte matrame surprise open avthundi.
is_birthday = now_ist >= target_date

# --- DISPLAY LOGIC ---
if not is_birthday:
    st.subheader("Counting down the days until September 3rd...")
    
    # Live updating countdown container
    countdown_placeholder = st.empty()
    
    # Refresh loops current clock data directly inside structural parameters
    loop_utc = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
    loop_ist = loop_utc + datetime.timedelta(hours=5, minutes=30)
    live_difference = target_date - loop_ist
    
    # Calculate exact live segments
    days = live_difference.days
    hours = live_difference.seconds // 3600
    minutes = (live_difference.seconds % 3600) // 60
    seconds = (live_difference.seconds % 60)
    
    with countdown_placeholder.container():
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Days Left", days)
        col2.metric("Hours Left", hours)
        col3.metric("Minutes Left", minutes)
        col4.metric("Seconds Left", seconds)
        
    st.info("The surprise unlocks automatically on your special day! Stay tuned. 😉")
    
    # Trigger refresh cycle
    time.sleep(1)
    st.rerun()

else:
    # Ee content pure ga kevalam September 3rd target daataka matrame unlock avuthundi
    if 'balloons_played' not in st.session_state:
        st.balloons()
        st.session_state['balloons_played'] = True
        
    st.success("🎉 HAPPY BIRTHDAY, ARCHANA! 🎉")

    # 1. Main Photo Section
    st.subheader("📸 A Special Moment")
    try:
        st.image("archana.png", caption="Keep shining bright!", width=300) 
    except Exception:
        st.error("Could not find 'archana.png'. Please make sure it is in your repository directory!")

    # 2. Interactive Note Generator
    st.subheader("💡 Click Below For A Secret Note...")
    if st.button("Click Here 👑"):
        compliments = [
            "Wishing you a year filled with achievements and boundless joy!",
            "May your smile always stay this bright and beautiful!",
            "Here's to a fantastic year ahead full of success!",
            "Hope this special day brings you endless reasons to be happy!"
        ]
        st.write(f"### 💌 *\"{random.choice(compliments)}\"*")

    # 3. Personalized Letter Section
    st.subheader("✉️ A Note For You")
    with st.expander("Click to open the message from Sai Charan"):
        st.write("""
        Hey Archana, 
        
        Naku konchem unique ga wishes chepdham anipinchindhi. 
        Thvaralo manam college lo kuda matladukuntam ani anukuntunna. ❤️✨
        
        Have the most beautiful birthday ever!
        
        Best wishes,  
        **Sai Charan**
        """)
