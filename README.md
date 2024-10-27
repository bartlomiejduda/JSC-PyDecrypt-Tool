# Info

**JSC-PyDecrypt-Tool** is a Python program for decrypting Cocos2d JSC files.<br>
<br>You need valid key to decrypt files. You can use **[Frida](https://frida.re/)** with my **[XXTEA Script](https://github.com/bartlomiejduda/Tools/blob/master/NEW%20Tools/Cocos2d/cocos2d_xxtea_script.js)** to get
the key from any Cocos2d android app.

Example frida command:<br>
```
frida -U -l cocos2d_xxtea_script.js -f <game_package_name>
```

# Usage

```
usage: jsc_pydecrypt_tool_v1.0.exe [-h]
                                   [-d <jsc_file_path> <encryption_key> <output_file_path>]

JSC PyDecrypt Tool v1.0

options:
  -h, --help            show this help message and exit
  -d <jsc_file_path> <encryption_key> <output_file_path>, --decrypt <jsc_file_path> <encryption_key> <output_file_path>
                        Decrypt data
```

# Building on Windows

1. Install  **[Python 3.11.0](https://www.python.org/downloads/)**
2. Install **[PyCharm 2024 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)**
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
