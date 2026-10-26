import pyfiglet
from colorama import Style,Fore

print("")
print("")
print(pyfiglet.figlet_format(text="reconjs",font="smblock"),end="")
print("JavaScript bundle security auditing, source map checks, unpacking, Retire.js scanning, secret detection, endpoint extraction.")
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="wordlist path") 
args = parser.parse_args()
