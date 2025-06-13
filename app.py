import streamlit as st
import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import time

# Load environment variables
load_dotenv()

def check_pinecone_connection():
    """Check if Pinecone API connection works"""
    try:
        # Get API key from environment
        api_key = os.getenv('PINECONE_API_KEY')
        
        if not api_key:
            return False, "API key not found in .env file"
        
        # Initialize Pinecone
        pc = Pinecone(api_key=api_key)
        
        # Try to list indexes (this will fail if API key is invalid)
        indexes = pc.list_indexes()
        
        # If we get here, connection works
        return True, f"✅ Connection successful! Found {len(indexes)} indexes."
        
    except Exception as e:
        return False, f"❌ Connection failed: {str(e)}"

# Streamlit UI
st.title("🔍 Pinecone API Checker")
st.markdown("Click the button below to test your Pinecone API connection")

# Add some spacing
st.markdown("---")

# Create columns for centered button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Test Pinecone Connection", use_container_width=True):
        with st.spinner("Checking connection..."):
            time.sleep(1)  # Small delay for better UX
            success, message = check_pinecone_connection()
        
        if success:
            st.success(message)
        else:
            st.error(message)

# Footer with instructions
st.markdown("---")
st.markdown("### 📝 Setup Instructions")
st.markdown("""
1. Make sure you have a `.env` file in your project root
2. Add your Pinecone API key: `PINECONE_API_KEY=your_key_here`
3. Run the app: `streamlit run app.py`
""")

# Show current status
with st.sidebar:
    st.markdown("### 🔐 Environment Status")
    if os.getenv('PINECONE_API_KEY'):
        st.success("✅ API key found in .env")
    else:
        st.error("❌ API key not found in .env")
