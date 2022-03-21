
# TODO -- Display error messages with colors
# TODO -- Error display format dynamic 

def showError(message: str = 'Something went wrong', errorType: str = 'Error', exitCode: int = 1, keepGoing: bool = False):

    print('\n')
    print("{}: {}".format(errorType,message))

    if not keepGoing:
        exit(exitCode)
