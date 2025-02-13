import streamlit as st
import requests
import json

# Streamlit App Title and Description
st.title("🎨 Boring-to-Analogies Converter")
st.write("Turn boring information into fun, memorable analogies!")

# User Input for Boring Information
boring_info = st.text_area("Enter the boring information:", "In 2008, an individual or group under the pseudonym Satoshi Nakamoto applied the Proof of Work mechanism in the creation of Bitcoin.")

# Button to Convert
if st.button("Make it Memorable!"):
    # Qwen-2-0.5B API Endpoint (Updated)
    url = "https://0x71d5c98a36b6fcefbd867f2838d657d16d01abd6.gaia.domains/v1/chat/completions"
    
    # Headers and Data for API Request
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Explain this using a fun analogy: {boring_info}"}
        ]
    }
    
    # API Call
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        
        # Get the Analogy from API Response
        result = response.json()
        analogy = result['choices'][0]['message']['content']
        
        # Display the Analogy
        st.success("Here’s a fun analogy:")
        st.write(analogy)
    except requests.exceptions.HTTPError as errh:
        st.error("HTTP Error:")
        st.write(errh)
    except requests.exceptions.ConnectionError as errc:
        st.error("Error Connecting:")
        st.write(errc)
    except requests.exceptions.Timeout as errt:
        st.error("Timeout Error:")
        st.write(errt)
    except requests.exceptions.RequestException as err:
        st.error("Something went wrong:")
        st.write(err)
