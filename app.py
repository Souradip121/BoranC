import streamlit as st  # Streamlit is used to create the user interface
import requests  # Requests is used to send API calls to GaiaNet
import json  # JSON is used to format and parse API requests and responses
from dotenv import load_dotenv  # Load environment variables from .env file
import os  # OS is used to access environment variables

# Load environment variables from the .env file
load_dotenv()

# Configure the Streamlit UI settings
st.set_page_config(
    page_title="memorAIble",  # Title of the app displayed on the browser tab
    page_icon="🧠",  # Emoji icon for the app
    layout="wide"  # Set layout to wide for better readability
)

# Application Title and Description
st.title("🧠 memorAIble")  # Displays the app title in a large font
st.write("Transform complex concepts into memorable analogies using decentralized AI!")  # Brief app description

# User Input Section
with st.container():  # Creates a container for structured layout
    st.subheader("Enter Your Complex Concept")  # Section heading
    complex_info = st.text_area(
        "What would you like to explain?",  # Input label
        height=150,  # Height of the text area
        placeholder="Enter the complex information you want to make memorable..."  # Helper text
    )

# Function to send the user's input to the GaiaNet AI network and retrieve an analogy
def generate_analogy(text):
    """
    Explain the user's input in a way that is both memorable and relatable. Make it a story. 
    """
    url = f"{os.getenv('GAIANET_NODE_URL')}/v1/chat/completions"  # API endpoint

    headers = {
        'accept': 'application/json',  # The server should return a JSON response
        'Content-Type': 'application/json'  # The request body is in JSON format
    }

    # Message format as per GaiaNet API specifications
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a creative expert at generating memorable analogies on web3 topics."
            },
            {
                "role": "user",
                "content": f"Create a memorable analogy to explain this concept: {text}"
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))  # Send the API request
        response.raise_for_status()  # Raise an error for HTTP request failures
        result = response.json()  # Convert JSON response to Python dictionary
        return result['choices'][0]['message']['content']  # Extract and return the generated analogy
    except Exception as e:
        return f"Error generating analogy: {str(e)}"  # Handle any errors and display an error message

# Process Button and Results Display
if st.button("Transform into Analogy", type="primary"):  # Button to trigger analogy generation
    if complex_info:  # Ensure that user input is provided
        with st.spinner("Generating your analogy using decentralized AI..."):  # Display a loading spinner
            analogy = generate_analogy(complex_info)  # Call the function to generate an analogy

        st.success("Your Memorable Analogy")  # Display success message
        st.markdown(f">{analogy}", unsafe_allow_html=True)  # Display the generated analogy

        # Additional Information Section
        with st.expander("How this works"):  # Create an expandable section with details
            st.markdown("""
            1. Your input is processed by our decentralized AI network
            2. Multiple AI nodes collaborate to generate the perfect analogy
            3. The best response is synthesized and delivered to you
            """)
    else:
        st.warning("Please enter some information to convert into an analogy.")  # Warning message if no input

# Footer Section
st.markdown("---")  # Adds a horizontal divider
st.markdown(
    "Built with ❤️ using GaiaNet's decentralized AI network. "
    "Contributing to a future of accessible and engaging learning."
)
