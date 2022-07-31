import os
import sys
import argparse
from glob import glob
from datetime import datetime
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError
import asyncio  # See https://bugs.python.org/issue37373 :(

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Parse command line options
parser = argparse.ArgumentParser(description="Automate running of Jupyter notebooks.")
parser.add_argument(
    "notebook_list",
    nargs="*",
    default=glob("*.ipynb"),
    help="List of Jupyter notebooks (*.ipynb) to be run (default=all notebooks in path).",
)
parser.add_argument(
    "-t",
    "--timeout",
    type=int,
    default=1000,
    help="Seconds until a cell in the notebook timesout, which raises a Timeouterror exception (default is 1000).",
)
parser.add_argument(
    "-s",
    "--sequence",
    action="store_true",
    help="Sequence implicit in notebook lists. If error occurs somewhere, stop entire pipeline.",
)
parser.add_argument(
    "-o",
    "--output",
    action="store_true",
    help='Creates a separate notebook with "-out"-suffix (e.g. *-out.ipynb) instead of overwriting existing file.',
)
parser.add_argument(
    "-v",
    "--version",
    type=int,
    help="Version of notebook to return (Default=No conversion). Notebook will be converted if necessary.",
)
parser.add_argument(
    "-q",
    "--stfu",
    default=False,
    action="store_true",
    help="Minimal printing of messages. Caution: Errors may not be printed.",
)

args = parser.parse_args()


def print_or_stfu(string, stfu=args.stfu):
    if not stfu:
        print(string)
    return None


print_or_stfu(f"Args:{args}")
start_time = datetime.now()
print_or_stfu(f"\nStart time: (hh:mm:ss) {start_time}")

# Run notebooks
size_work = len(args.notebook_list)
seq_err_msg = f"Error in sequence of notebooks, exiting entire pipeline..."

print_or_stfu("~~~~~~~~~~~~~~~~~~~~~~~~~")
for ix, filename in enumerate(args.notebook_list):
    if not os.path.isfile(filename):
        filename = "".join([filename, ".ipynb"])

    with open(filename) as f:
        if not args.version:
            nb = nbformat.read(f, nbformat.NO_CONVERT)
        else:
            nb = nbformat.read(f, as_version=args.version)

        ep = ExecutePreprocessor(timeout=args.timeout, kernel_name="python3")
        print_or_stfu(f"Running notebook {ix+1}/{size_work}: {filename}")

        try:
            ep.preprocess(nb)
            print_or_stfu(f"Done {filename}.\n")
        except CellExecutionError:
            print(f"Error executing {ix+1}/{size_work}: {filename}.\n")
            if args.sequence:
                sys.exit(seq_err_msg)
        except TimeoutError:
            print(f"Cell timeout error with {filename}.\n")
            if args.sequence:
                sys.exit(seq_err_msg)
        finally:
            if args.output:
                filename = filename.split(".")[0]
                filename = "".join([filename, "-out.ipynb"])

                with open(filename, mode="wt") as f:
                    nbformat.write(nb, f)

print_or_stfu(f"End time: (hh:mm:ss) {datetime.now()}")
elapsed_time = datetime.now() - start_time
print_or_stfu(f"Elaped time: (hh:mm:ss) {elapsed_time}")
