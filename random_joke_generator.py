import streamlit as st
import requests  # api calling and data fetch from the api


def random_joke_generator():
    """This function generates a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:  # api correctly running
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch joke. Please try again later."
    except:
        return "Oops! Your logic went on a coffee break and never came back."


def main():
    """This function is the main function of the application"""
    st.title("Random Joke Generator")
    st.write("Click the butto below to generate joke")
    if st.button("Tell me a joke!", icon="😂"):
        joke = random_joke_generator()
        st.success(joke)
    st.divider()

    st.markdown(
        """
      <div style=" text-align: center;">
      <h4>🤣</h4>
      <p>Hi I am Front End Developer. Watch my Project on my github profile link below:</p>
      <div style=" display: flex; justify-content: center; align-items: center; gap: 16px;">
      
      <img src="https://github.com/sadafshahab12.png"  style="border-radius: 50%; width : 40px"/>
      <p style = "margin: 0px "><a href="https://www.github.com/sadafshahab12"> Sadaf Shahab </p> 
      </div>
      </div>
      
      """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
