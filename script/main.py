#!/usr/bin/env python
import argparse
import sys
from os.path import abspath, dirname, join

sys.path.append(abspath(join(dirname(__file__), "src")))

from get_board import main as get_board_info
from get_pin import main as get_pin_info
from get_user_boards import main as get_user_boards_info
from get_user_pins import main as get_user_pins_info

def main(argv=[]):
    parser = argparse.ArgumentParser(description="Pinterest Information Retrieval Tool")
    parser.add_argument("action", choices=["board", "pin", "user_boards", "user_pins"], help="Specify the action to perform")
    parser.add_argument("-id", "--identifier", required=True, help="Identifier of the board or pin")
    parser.add_argument("-a", "--access-token", help="Access token for Pinterest API")
    parser.add_argument("-l", "--log-level", default="2", choices=["1", "2", "3", "4", "5"], help="Set the logging level")
    args = parser.parse_args(argv)

    if args.action == "board":
        get_board_info(["-b", args.identifier, "--pins", "-a", args.access_token, "--log-level", args.log_level])
    elif args.action == "pin":
        get_pin_info(["-p", args.identifier, "-a", args.access_token, "--log-level", args.log_level])
    elif args.action == "user_boards":
        get_user_boards_info(["--page-size", "25", "--include-empty", "--no-include-archived", "-a", args.access_token, "--log-level", args.log_level])
    elif args.action == "user_pins":
        get_user_pins_info(["--page-size", "25", "-a", args.access_token, "--log-level", args.log_level])

if __name__ == "__main__":
    main(sys.argv[1:])
# import argparse
# import subprocess

# def main():
#     parser = argparse.ArgumentParser(description="Pinterest Data Retrieval")
#     subparsers = parser.add_subparsers(dest="command", help="Available commands")

#     # Subparser for get_board command
#     get_board_parser = subparsers.add_parser("get_board")
#     get_board_parser.add_argument("-b", "--board-id", required=True, help="Board identifier")
#     get_board_parser.add_argument("--pins", action="store_true", help="Get information about each pin on the board")

#     # Subparser for get_pin command
#     get_pin_parser = subparsers.add_parser("get_pin")
#     get_pin_parser.add_argument("-p", "--pin-id", required=True, help="Pin identifier")

#     # Subparser for get_user_boards command
#     get_user_boards_parser = subparsers.add_parser("get_user_boards")
#     get_user_boards_parser.add_argument("-ps", "--page-size", default=25, type=int, help="Boards per page")
#     get_user_boards_parser.add_argument("--include-empty", action="store_true", help="Include empty boards")
#     get_user_boards_parser.add_argument("--no-include-empty", action="store_true", help="Do not include empty boards")
#     get_user_boards_parser.add_argument("--include-archived", action="store_true", help="Include archived boards")
#     get_user_boards_parser.add_argument("--no-include-archived", action="store_true", help="Do not include archived boards")

#     # Subparser for get_user_pins command
#     get_user_pins_parser = subparsers.add_parser("get_user_pins")
#     get_user_pins_parser.add_argument("-ps", "--page-size", default=25, type=int, help="Pins per page")

#     args = parser.parse_args()

#     # Build the command based on the chosen subcommand
#     command = f"python script/{args.command}.py"
#     for arg, value in vars(args).items():
#         if value is True:
#             command += f" --{arg.replace('_', '-')}"
#         elif value is False:
#             command += f" --no-{arg.replace('_', '-')}"

#         elif value is not None:
#             command += f" --{arg.replace('_', '-')} {value}"

#     subprocess.run(command, shell=True)

# if __name__ == "__main__":
#     main()