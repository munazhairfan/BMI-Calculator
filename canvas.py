import streamlit as st
from streamlit_drawable_canvas import st_canvas


st.set_page_config(page_title="Canvas",page_icon="🖌")
st.markdown("""
    <style>
        button[title="Send to Streamlit"],
        div[data-testid="stDownloadButton"] {
            display: none !important;
            visibility: hidden !important;
        }
    </style>
""", unsafe_allow_html=True)



st.sidebar.title("🎨 Toolbar")

bg_color = st.sidebar.color_picker("Pick a background color:","#FFFFFF")

brush_color = st.sidebar.color_picker("Pick a brush color:","#000000")

brush_size = st.sidebar.slider("Pick a brush size:",1,20,5)
brush_style = st.sidebar.selectbox(
    "Select Brush Style", 
    ["Normal", "Marker", "Highlighter", "Spray Paint"]
)

if brush_style == "Marker":
    brush_size = brush_size + 5  
elif brush_style == "Highlighter":
    brush_size = brush_size + 10
    brush_color = brush_color + "80" 
elif brush_style == "Spray Paint":
    brush_size = brush_size + 40
    brush_color = brush_color + "33"  

drawing_tool = st.sidebar.selectbox("Pick a tool:",["freedraw","line","rect","circle","polygon"])

eraser = st.sidebar.checkbox("Eraser🧽")
if eraser:
    brush_color = bg_color
    drawing_tool = "freedraw"
st.header("Sketchpad")
st_canvas(background_color=bg_color,
          height=800,width=800,
          drawing_mode=drawing_tool,
          stroke_width=brush_size,
          stroke_color=brush_color,
          key="canvas")
