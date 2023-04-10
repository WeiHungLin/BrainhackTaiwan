import useful_functions as UF
from argparse import ArgumentParser, Namespace


parser = ArgumentParser()
parser.add_argument('-m', '--message', action="store",
                        help="Path to raw data txt file, i.e. msg_file.txt.", type=str)
parser.add_argument('-k',"--key", action="store",
                        help="Please enter your key", type= str)
parser.add_argument("--mode", action="store", default="enc", type=str,
                        help="Enc or dec")
    
results: Namespace = parser.parse_args()

if __name__ == "__main__":

    if results.mode == "enc":
        results.mode = "True"
    elif results.mode == "dec":
        results.mode = "False"

   
    handle = open(results.message)
    for line in handle:
        line = line.rstrip()
        print(UF.process_message(line, results.key, results.mode))
        print(line)


