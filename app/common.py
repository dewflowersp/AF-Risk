import streamlit as st

BACKGROUND_COLOR = 'white'
COLOR = 'black'

def set_page_container_style(
        max_width: int = 1100, max_width_100_percent: bool = True,
        padding_top: int = 1, padding_right: int = 3, padding_left: int = 3, padding_bottom: int = 1,
        color: str = COLOR, background_color: str = BACKGROUND_COLOR,
    ):
        if max_width_100_percent:
            max_width_str = f'max-width: 100%;'
        else:
            max_width_str = f'max-width: {max_width}px;'
        st.markdown(
            f'''
            <style>
                .appview-container .css-1lcbmhc .css-1outpf7 {{
                    padding-top: 35px;
                }}
                .appview-container .main .block-container {{
                    {max_width_str}
                    padding: {padding_top}rem {padding_right}rem {padding_bottom}rem {padding_left}rem;
                }}
                .appview-container .main {{
                    color: {color};
                    background-color: {background_color};
                }}
            </style>
            ''',
            unsafe_allow_html=True,
        )