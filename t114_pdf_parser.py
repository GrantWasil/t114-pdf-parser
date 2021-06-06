import pdfplumber
import json
import sys
import glob
import traceback

def main():
    """ Main function
    """
    if len(sys.argv) != 2:
        print("Invalid arguments")
        print("python parse_info_pdf.py <directory>")
        exit(0)

    directory = sys.argv[1]
    files = glob.glob(directory + "/*.pdf")

    print("Running...")

    for i, f in enumerate(files):
        print("[{}/{}] Running on file {}".format(i+1, len(files), f))
        try:
            final = parse_pdf(f)
            j = json.dumps(final)
            with open(f+".json", "w") as output:
                output.write(j)
        except Exception as e:
            print("\t~Exception Occurred: {}".format(e))
            print(traceback.format_exc())

    print("\nDone!")

def get_until_str(text, match_text):
    """ Get line data as string until string match is hit
    """
    data, remaining = get_until(text, match_text)
    return "".join(data), remaining

def get_until(text, match_text):
    """ Get line data until string match is hit
    """
    data = []
    remaining = text
    for i, line in enumerate(text):
        if match_text in line:
            i += 1
            remaining = text[i:]
            break
        data.append(line)

    if len(data) < 1:
        print("No data pulled from get_until with match_text {}. Input text {}".format(match_text, text))

    return data, remaining


def parse_pdf(filename):
    """ Parse formatted PDF
    """
    info = {}
    pdf = pdfplumber.open(filename)

    # Get raw text
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    pdf.close()

    # Add your own parsing here
    # Parse the 'text' string and pull out the info you want put it into the 'info' dictonary
    text = get_until(text, "Position Name Person ID Address BL DOB M/F Phone")
    print(text)


    return info


if __name__ == "__main__":
    main()