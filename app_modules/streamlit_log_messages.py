import sys
import streamlit.components.v1 as components
import streamlit as st

def streamlit_log_messages(log_messages):
    if is_running_in_streamlit():
        box(log_messages)

def is_running_in_streamlit():
    # Detecting if the script is ran in streamlit
    if "main_app" in sys.argv[0]:
        return True
    else:
        return False
    
def box(log_messages):
    # Combine all messages into one string
    full_log = "<br>".join(log_messages)
    # HTML/JS component with auto-scroll

    components.html(f""" 
        <div style="margin-top: -10px;">
            <div id="log-box" 
                style="height: 100px; 
                        overflow-y: auto; 
                        background-color: #f0f0f0; 
                        padding: 6px; font-family: monospace; 
                        border-radius: 5px;">
                {full_log}
            </div>
            <script>
                var logBox = document.getElementById("log-box");
                logBox.scrollTop = logBox.scrollHeight;
            </script>
        </div>
    """, height=120)

