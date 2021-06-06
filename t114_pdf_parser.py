import pdfplumber
import json

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
    print(text)

    return info


if __name__ == "__main__":
    main()