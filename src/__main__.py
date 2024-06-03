"""
This file allows running the parent directory directly:
python3 src [ arg1 ... ]

This also allows packaging up as a zipapp.

If you do not need this functionality:
  - Remove this file.
  - Consider moving streamlit_sandbox out of src.
"""

import streamlit_sandbox.__main__

streamlit_sandbox.__main__.main()
