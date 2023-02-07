import streamlit as st
from rembg import remove
import io

def main():
    st.title("Remove Background Tool")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png"])
    if uploaded_file is not None:
        input_path = io.BytesIO(uploaded_file.getvalue())
        output_path = 'output.png'

        with input_path as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)

        st.image(output_path, caption="Image with removed background")

if __name__ == "__main__":
    main()
