import streamlit as st
import pytz
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="⏰ Clockwise AI",
    page_icon="🕐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .clock-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 2px solid #e1e8ed;
    }
    
    .digital-clock {
        font-family: 'Courier New', monospace;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        background: linear-gradient(45deg, #3498db, #2ecc71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 1rem 0;
    }
    
    .timezone-label {
        font-size: 1.2rem;
        font-weight: 600;
        color: #34495e;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .date-display {
        font-size: 1rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    
    .feature-card {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 4px solid #3498db;
    }
</style>
""", unsafe_allow_html=True)

# Timezone data with country/capital format
TIMEZONE_DATA = {
    "Pakistan/Islamabad": "Asia/Karachi",
    "United States/New York": "America/New_York",
    "United States/Los Angeles": "America/Los_Angeles",
    "United Kingdom/London": "Europe/London",
    "Germany/Berlin": "Europe/Berlin",
    "France/Paris": "Europe/Paris",
    "Japan/Tokyo": "Asia/Tokyo",
    "China/Beijing": "Asia/Shanghai",
    "India/New Delhi": "Asia/Kolkata",
    "Australia/Sydney": "Australia/Sydney",
    "Canada/Toronto": "America/Toronto",
    "Brazil/Brasília": "America/Sao_Paulo",
    "Russia/Moscow": "Europe/Moscow",
    "South Africa/Cape Town": "Africa/Johannesburg",
    "Egypt/Cairo": "Africa/Cairo",
    "UAE/Dubai": "Asia/Dubai",
    "Singapore/Singapore": "Asia/Singapore",
    "South Korea/Seoul": "Asia/Seoul",
    "Turkey/Istanbul": "Europe/Istanbul",
    "Italy/Rome": "Europe/Rome",
    "Spain/Madrid": "Europe/Madrid",
    "Netherlands/Amsterdam": "Europe/Amsterdam",
    "Sweden/Stockholm": "Europe/Stockholm",
    "Norway/Oslo": "Europe/Oslo",
    "Mexico/Mexico City": "America/Mexico_City",
    "Argentina/Buenos Aires": "America/Argentina/Buenos_Aires",
    "Chile/Santiago": "America/Santiago",
    "Thailand/Bangkok": "Asia/Bangkok",
    "Vietnam/Ho Chi Minh City": "Asia/Ho_Chi_Minh",
    "Philippines/Manila": "Asia/Manila",
    "Indonesia/Jakarta": "Asia/Jakarta",
    "Malaysia/Kuala Lumpur": "Asia/Kuala_Lumpur",
    "Bangladesh/Dhaka": "Asia/Dhaka",
    "Sri Lanka/Colombo": "Asia/Colombo",
    "Nepal/Kathmandu": "Asia/Kathmandu",
    "Iran/Tehran": "Asia/Tehran",
    "Israel/Jerusalem": "Asia/Jerusalem",
    "Saudi Arabia/Riyadh": "Asia/Riyadh",
    "Kenya/Nairobi": "Africa/Nairobi",
    "Nigeria/Lagos": "Africa/Lagos",
    "Ghana/Accra": "Africa/Accra",
    "Morocco/Casablanca": "Africa/Casablanca",
    "New Zealand/Auckland": "Pacific/Auckland",
    "Fiji/Suva": "Pacific/Fiji",
}

def display_digital_clock(timezone_name, timezone_str):
    """Display digital clock"""
    try:
        tz = pytz.timezone(timezone_str)
        current_time = datetime.now(tz)
        
        # Format time in 12-hour format
        time_str = current_time.strftime("%I:%M:%S %p")
        date_str = current_time.strftime("%A, %B %d, %Y")
        
        return time_str, date_str
        
    except Exception as e:
        st.error(f"Error getting time for {timezone_name}: {str(e)}")
        return "Error", "Error"

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>⏰ Clockwise AI</h1>
        <p>Multi-Timezone Clock Application</p>
        <p>Track time across different countries and capitals around the world</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🌍 Clock Configuration")
        
        # Clock display mode (Digital only)
        display_mode = "Digital"
        
        # Manual refresh button
        if st.button("🔄 Refresh Clocks", use_container_width=True):
            st.rerun()
        
        st.markdown("---")
        
        # Timezone management
        st.markdown("### 🕐 Manage Clocks")
        
        # Initialize session state for selected timezones
        if 'selected_timezones' not in st.session_state:
            st.session_state.selected_timezones = ["Pakistan/Islamabad"]
        
        # Display current clocks
        if st.session_state.selected_timezones:
            st.markdown("**Current Clocks:**")
            for i, timezone in enumerate(st.session_state.selected_timezones):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.text(f"{i+1}. {timezone}")
                with col2:
                    if st.button("❌", key=f"remove_{i}", help="Remove this clock"):
                        st.session_state.selected_timezones.pop(i)
                        st.rerun()
        
        # Add new clock section
        if len(st.session_state.selected_timezones) < 6:
            st.markdown("**Add New Clock:**")
            new_timezone = st.selectbox(
                "Select Country/City",
                ["Select a timezone..."] + [tz for tz in TIMEZONE_DATA.keys() if tz not in st.session_state.selected_timezones],
                key="new_timezone_selector",
                help="Search by typing country or city name"
            )
            
            if st.button("➕ Add Clock", use_container_width=True):
                if new_timezone != "Select a timezone...":
                    st.session_state.selected_timezones.append(new_timezone)
                    st.rerun()
                else:
                    st.warning("Please select a timezone first!")
        else:
            st.info("Maximum 6 clocks reached. Remove a clock to add a new one.")
        
        selected_timezones = st.session_state.selected_timezones
        
        st.markdown("---")
    
    # Main content
    if not selected_timezones:
        st.info("👆 Please add at least one timezone from the sidebar to display clocks.")
        return
    
    # Display clocks (Digital only)
    st.markdown("### 🕐 Your Clocks")
    
    # Digital clocks in grid layout
    cols = st.columns(min(len(selected_timezones), 3))
    
    for i, timezone_name in enumerate(selected_timezones):
        timezone_str = TIMEZONE_DATA[timezone_name]
        
        with cols[i % 3]:
            time_str, date_str = display_digital_clock(timezone_name, timezone_str)
            
            st.markdown(f"""
            <div class="clock-container">
                <div class="timezone-label">{timezone_name}</div>
                <div class="date-display">{date_str}</div>
                <div class="digital-clock">{time_str}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; margin-top: 2rem;">
        <p>🤖 Powered by Clockwise AI | Built with Streamlit & Python</p>
        <p>Track time across the globe with precision and style</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
