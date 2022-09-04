import gzip
from typing import Optional
import xxtea
import sys
import argparse

from reversebox.io_files.check_file import check_file

from logger import get_logger


# Ver    Date        Author               Comment
# v0.1   03.09.2022  Bartlomiej Duda      -


logger = get_logger(__name__)

VERSION_NUM = "v0.1"
EXE_FILE_NAME = f"jsc_pydecrypt_tool_{VERSION_NUM}.exe"
PROGRAM_NAME = f"JSC PyDecrypt Tool {VERSION_NUM}"


def export_data(
        jsc_file_path: str, encryption_key_str: str, output_file_path: str
                ) -> Optional[tuple]:
    """
    Function for decrypting JSC files
    """
    logger.info("Starting export_data...")

    code, status = check_file(jsc_file_path, ".JSC", True)
    if code != "OK":
        return code, status

    jsc_file_data = open(jsc_file_path, "rb").read()

    output_data = xxtea.decrypt(jsc_file_data, encryption_key_str)
    if len(output_data) == 0:
        return "WRONG_KEY", "Invalid encryption key!"

    #output_data = zlib.decompress(output_data, 16 + zlib.MAX_WBITS)
    output_data = gzip.decompress(output_data)

    #output_data = json.dumps(output_data, indent=4)

    js_file = open(output_file_path, "wb")
    js_file.write(output_data)

    js_file.close()
    logger.info(f"File exported: {output_file_path}")
    return "OK", ""


def main():
    """
    Main function of this program.
    """
    parser = argparse.ArgumentParser(prog=EXE_FILE_NAME, description=PROGRAM_NAME)
    # fmt: off
    parser.add_argument("-d", "--decrypt", metavar=("<jsc_file_path>", "<encryption_key>", "<output_file_path>"),
                        type=str, nargs=3, required=False, help="Decrypt data")

    # parser.add_argument("-e", "--encrypt", metavar=("<xml_file_path>", "<encryption_key>", "<eco_file_path>"),
    #                     type=str, nargs=3, required=False, help="Encrypt data")
    # fmt: on

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.decrypt is not None:
        code, status = export_data(args.decrypt[0], args.decrypt[1], args.decrypt[2])
        if code != "OK":
            logger.error(f"{code}: {status}")
            sys.exit(-1)
    # elif args.encrypt is not None:
    #     code, status = import_data(args.encrypt[0], args.encrypt[1], args.encrypt[2])
    #     if code != "OK":
    #         logger.error(f"{code}: {status}")
    #         sys.exit(-2)

    logger.info("End of main... Program has been executed successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()
