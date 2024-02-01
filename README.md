# pcheck - Pinterest Checker

## Overview

pcheck is a user-friendly command-line tool designed to retrieve information about pins and boards from a Pinterest user's profile. The application aims to simplify the process of tracking changes, monitoring activities, and obtaining relevant data from specific boards and pins on Pinterest. It provides users with a quick and convenient way to access the information they are interested in.

## Features

- **Information Retrieval:** Obtain detailed data about pins and boards associated with a Pinterest user account.

- **Sync Changes:** Keep track of updates and changes in the specified boards and pins.

- **User-Friendly Interface:** pcheck is designed for ease of use, allowing users to quickly gather the information they need.

## Getting Started

### Prerequisites

Before using pcheck, make sure you have the following installed:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/pcheck.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pcheck
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

<!-- ### Usage

#### Main Script (main.py)

The `main.py` script serves as the entry point for interacting with the Pinterest API through various specialized scripts.

##### Retrieving User Boards

To retrieve information about user boards, use the following command:

```bash
python main.py --user-boards [--page-size PAGE_SIZE] [--include-empty | --no-include-empty] [--include-archived | --no-include-archived]
```

- `--page-size`: Specify the number of boards per page (default is 25).
- `--include-empty` or `--no-include-empty`: Include or exclude empty boards.
- `--include-archived` or `--no-include-archived`: Include or exclude archived boards.

##### Retrieving User Pins

To retrieve information about user pins, use the following command:

```bash
python main.py --user-pins [--page-size PAGE_SIZE]
```

- `--page-size`: Specify the number of pins per page (default is 25).

##### Retrieving Board Information

To retrieve information about a specific board, use the following command:

```bash
python main.py --board-id BOARD_ID [--pins]
```

- `--pins`: Include this flag to also retrieve information about each pin on the board.

##### Retrieving Pin Information

To retrieve information about a specific pin, use the following command:

```bash
python main.py --pin-id PIN_ID
```

#### Examples

- Retrieve information about user boards:

  ```bash
  python main.py --user-boards --page-size 50 --include-archived
  ```

- Retrieve information about a specific board and its pins:

  ```bash
  python main.py --board-id <BOARD_ID> --pins
  ```

- Retrieve information about user pins:

  ```bash
  python main.py --user-pins --page-size 50
  ```

- Retrieve information about a specific pin:

  ```bash
  python main.py --pin-id <PIN_ID>
  ```

### Note

Replace `<BOARD_ID>` and `<PIN_ID>` with the actual board and pin identifiers. -->

### Usage

```bash
python main.py <action> -id <identifier> [-a <access-token>] [-l <log-level>]
```

#### Arguments

- `<action>`: Specify the action to perform. Available options:
  - `board`: Retrieve information about a specific board.
  - `pin`: Retrieve information about a specific pin.
  - `user_boards`: Retrieve information about boards associated with a user.
  - `user_pins`: Retrieve information about pins associated with a user.

- `-id, --identifier <identifier>`: Identifier of the board or pin. Required for all actions.

- `-a, --access-token <access-token>`: Access token for Pinterest API. Optional.

- `-l, --log-level <log-level>`: Set the logging level. Options: "1" (DEBUG), "2" (INFO), "3" (WARNING), "4" (ERROR), "5" (CRITICAL). Default: "2" (INFO).

#### Examples

1. Retrieve information about a specific board with identifier "12345":

   ```bash
   python main.py board -id 12345 -a <your-access-token>
   ```

2. Retrieve information about a specific pin with identifier "67890":

   ```bash
   python main.py pin -id 67890 -a <your-access-token>
   ```

3. Retrieve information about boards associated with a user:

   ```bash
   python main.py user_boards -id <user-identifier> -a <your-access-token> --log-level 3
   ```

4. Retrieve information about pins associated with a user:

   ```bash
   python main.py user_pins -id <user-identifier> -a <your-access-token>
   ```

Ensure to replace `<your-access-token>` and `<user-identifier>` with your actual Pinterest API access token and user identifier. Adjust other parameters as needed for your specific use case.
## Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.