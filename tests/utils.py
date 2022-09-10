import sys
import string
import random
from io import StringIO


def random_alphanumeric_string(N=10):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=N))


class CaptureStdout(list):
    """
    Utility object using a context manager to capture stdout for a given block
    of Python code. Subclass of list so that you can access stdout lines like a
    list.
    """

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __enter__(self, *args, **kwargs):
        """
        The function called when we open the context, this function swaps out
        sys.stdout with a string buffer and saves the sys.stdout reference.
        """
        # Save existing stdout object so we can restore it when we're done
        self._stdout = sys.stdout
        # Swap out stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args, **kwargs):
        """
        Close the context and clean up; the *args are needed in case there is
        an exception (we don't deal with those here)
        """
        # This class extends the list class, so call self.extend to add a list
        # to the end of self. This is to add all of the new lines from the
        # StringIO object.
        self.extend(self._stringio.getvalue().splitlines())

        # Clean up (if this is missing, the garbage collector will eventually
        # take care of this...)
        del self._stringio

        # Clean up by setting sys.stdout back to what it was before we opened
        # up this context
        sys.stdout = self._stdout
