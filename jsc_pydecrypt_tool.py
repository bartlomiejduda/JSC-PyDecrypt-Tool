import argparse
import gzip
import io
import sys
from typing import Optional
from zipfile import BadZipFile, ZipFile

import xxtea
from reversebox.common.logger import get_logger
from reversebox.io_files.check_file import check_file

# Ver    Date        Author               Comment
# v0.1   03.09.2022  Bartlomiej Duda      -
# v0.2   04.09.2022  Bartlomiej Duda      -
# v1.0   27.10.2024  Bartlomiej Duda      Update packages
# v1.1   16.11.2024  Bartlomiej Duda      Update packages


logger = get_logger(__name__)

VERSION_NUM = "v1.1"
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

    jsc_file = open(jsc_file_path, "rb")
    jsc_file_data = jsc_file.read()
    jsc_file.close()

    logger.info(f"Decrypting with key = {encryption_key_str}")
    output_data = xxtea.decrypt(jsc_file_data, encryption_key_str)
    if len(output_data) == 0:
        return "WRONG_KEY", "Invalid encryption key!"

    is_gzip_file = True
    try:
        output_data = gzip.decompress(output_data)
        logger.info("IT IS a GZIP archive.")
    except gzip.BadGzipFile as error:
        logger.info("It's NOT a GZIP archive.")
        is_gzip_file = False

    if not is_gzip_file:
        try:
            zip_file = io.BytesIO(output_data)
            ZipFile(zip_file)
            output_file_path += ".zip"
            logger.info("IT IS a ZIP archive.")
        except BadZipFile as error:
            logger.info("It is NOT a ZIP archive.")

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

    logger.info("End of main... Program has been executed successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()
