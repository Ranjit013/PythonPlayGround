import argparse


def createCommandForProcessing(args):
    arguments = args.arguments
    fileName = args.fileName

    if (len(arguments) > 0):
        finalString = ' '.join([str(item) for item in arguments])

    print(finalString)
    return "less" + fileName + "| python -m json.tool | jq '.[] |" + finalString + "'"


def formatFile(args):
    fileName = args.fileName
    argments = args.arguments
    cmd = createCommandForProcessing(args)
    print(cmd)
    # subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='fileName', action='store', help='To format the file Name', required=True)
    parser.add_argument('-a', dest='arguments', action='store', help='To format the file Name', required=True)
    parser.add_argument('-l', dest='arguments', nargs="*", help='To format the file Name')
    parse = parser.parse_args()
    formatFile(parse)
