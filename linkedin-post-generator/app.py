import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📝", layout="centered")

# Custom UI styles
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #0077b5;
        color: white;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #005582;
        border-color: #0077b5;
    }
    .stSelectbox, .stTextArea {
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

st.title("📝 AI LinkedIn Post Generator")
st.markdown("Generate high-quality, professional LinkedIn posts using Google's Gemini 2.5 Flash model.")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "Gemini API Key", 
        type="password", 
        help="Enter your Gemini API key here. It remains secure in your browser session."
    )
    if not api_key:
        st.warning("⚠️ Please enter your Gemini API key to generate posts.")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app uses your Gemini API key to draft viral-worthy professional posts tailored precisely for LinkedIn.")

# Form Layout
with st.form("post_generator_form"):
    topic = st.text_area(
        "What's your post about?", 
        placeholder="E.g., Overcoming a major bug in production and what my team learned...", 
        height=100
    )
    
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Tone", ["Professional", "Inspirational", "Educational", "Storytelling", "Controversial"])
    with col2:
        length = st.selectbox("Length", ["Short (under 100 words)", "Medium (100-200 words)", "Long (above 200 words)"])
    
    col3, col4 = st.columns(2)
    with col3:
        include_hashtags = st.checkbox("Include Hashtags", value=True)
    with col4:
        call_to_action = st.checkbox("Include Call to Action", value=True)
    
    submit_button = st.form_submit_button(label="Generate Post ✨")

# Generation Logic
if submit_button:
    if not api_key:
        st.error("Please provide a Gemini API key in the sidebar.")
    elif not topic.strip():
        st.error("Please enter a topic.")
    else:
        with st.spinner("Generating magic with Gemini..."):
            try:
                # Configure Gemini API
                genai.configure(api_key=api_key)
                
                # Prompt Engineering
                prompt = f"""
                You are a top-tier Social Media Manager and expert LinkedIn copywriter. Your goal is to write a highly engaging, viral-worthy LinkedIn post based on the following specifics.
                
                Topic: {topic}
                Tone: {tone}
                Target Length: {length}
                
                Guidelines:
                - Use a strong hook in the first line to catch attention.
                - Use spacing to make it skimmable (the classic LinkedIn formatting without huge dense paragraphs).
                - Use emojis appropriately for the context (don't overdo it).
                - Provide only the text of the post itself, with no intro or outro comments.
                """
                
                # Add specific conditionals
                if include_hashtags:
                    prompt += "\n- Add 3-5 relevant, highly searched hashtags at the bottom."
                if call_to_action:
                    prompt += "\n- End the post with an engaging question to drive comments."
                
                # Initialize Model
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # API Call
                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                    )
                )
                
                result = response.text
                
                st.success("Post Generated Successfully!")
                
                st.markdown("### Your LinkedIn Post")
                st.info(result)
                
                st.markdown("📍 **Quick Copy:**")
                st.code(result, language="text")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
