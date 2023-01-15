import argparse

def telecloud_args():

    parser = argparse.ArgumentParser()
    # Read arguments from the command line
    parser.add_argument("--name", "-n", help = "That unique name you've set at the first", required = True)
    parser.add_argument("--username", "-u", help = "Set target username for sending file/files to her/him", required = True)
    parser.add_argument("--path", "-p", help = "Path of the file/files you want to upload", required = True)
    parser.add_argument("--mode", "-m", help="Change mode to upload or download", required=True)
    parser.add_argument("--format", default="text", dest="parse_mode", choices=["text", "markdown", "html"],
                        help="Parse mode for file caption. Choose from 'text', 'markdown', or 'html'. Default is 'text'")
    parser.add_argument("--caption", "-c", help = "for upload mode: write caption/text under file, for download mode: download file by its caption or name", default = '', required = False)
    
    args = parser.parse_args()
    return args