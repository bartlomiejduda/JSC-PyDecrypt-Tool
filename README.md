# Info

**JSC-PyDecrypt-Tool** is a Python program for decrypting Cocos2d JSC files.

# Building on Windows

1. Install  **[Python 3.10.0](https://www.python.org/downloads/)**
2. Install **[PyCharm 2022.1 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)**
3. Create virtualenv and activate it
   - python3 -m venv \path\to\new\virtual\environment
   - .\venv\Scripts\activate.bat
4. Install all libraries from requirements.txt
   - pip3 install -r requirements.txt
5. Run the jsc_pydecrypt_tool.py file with proper command line arguments

NOTE: There is also "DECRYPT_ALL.BAT" script which can
be used for batch processing. Just set correct
encryption key, put your files inside "INPUT"
directory and run the script.
