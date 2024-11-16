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

1. Download and install  **[Python 3.11.6](https://www.python.org/downloads/release/python-3116/)**. Remember to add Python to PATH during installation
2. Download and install **[Microsoft C++ Build Tools](https://visualstudio.microsoft.com/pl/visual-cpp-build-tools/)**
3. Download project's source code and save it in "JSC-PyDecrypt-Tool-main" directory
4. Go to the directory containing source code
   - ```cd JSC-PyDecrypt-Tool-main```
5. Create virtualenv and activate it
   - ```python -m venv my_env```
   - ```.\my_env\Scripts\activate.bat```
6. Install all libraries from requirements.txt file
   - ```pip install -r requirements.txt```
7. Add project's directory to PYTHONPATH environment variable
   - ```set PYTHONPATH=C:\Users\user\Desktop\JSC-PyDecrypt-Tool-main```
8. Run the jsc_pydecrypt_tool.py file with proper command line arguments
   - ```python jsc_pydecrypt_tool.py -d project.jsc "secret" project.js```
