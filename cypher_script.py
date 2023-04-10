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
        x = "True"
        name = results.message.replace(".txt", "_encrypted.txt")
    elif results.mode == "dec":
        x = "False"
        name = results.message.replace(".txt", "_decrypted.txt")

    with open(name, 'w') as fp:
        list =[]
        handle = open(results.message)
        for line in handle:
            line = line.rstrip()
            ans = UF.process_message(line, results.key, x)
            print(ans)
            fp.write("%s\n" % ans)