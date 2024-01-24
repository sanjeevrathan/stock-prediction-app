import sys
from streamlit.web import cli as stcli
if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "main.py", "5000"]
    sys.exit(stcli.main())
