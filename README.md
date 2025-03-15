# Calculator Project

## Overview

This project is a simple Python-based calculator that lets you perform basic arithmetic and statistical operations through an interactive command-line interface. It features a calculation history that persists between sessions, the ability to edit previous entries, and support for plugins to extend its functionality.

## Features

- **Arithmetic Operations:** Easily perform addition, subtraction, multiplication, and division.
- **Statistical Operations:** Easily perform mean, median, mode and variance.
- **Calculation History:** Every calculation is recorded with a timestamp. You can view, clear, or edit your history.
- **Plugin Support:** Extend the calculator’s capabilities by adding custom plugins.
- **Persistence:** Your calculation history is saved automatically when you exit and loaded when you start again.
- **User-Friendly REPL:** A clear command-line interface that shows available commands and usage instructions.

## Demo Video Link
- This the link to my demo video link - [Demo Video](https://drive.google.com/file/d/1FsWkvNlHg8uYU5c4BsHBsaO7kfeKYeWb/view?usp=drive_link)
## Create and Activate a Virtual Environment
- **On Linux/Mac:**
- `python3 -m venv venv`
- `source venv/bin/activate`

- **On Windows:**
- `python -m venv venv`
- `venv\Scripts\activate`

## Usage
- To start the calculator, run:
- `python main.py`
- When the calculator starts, you'll see a welcome message with a list of commands. - Here are a few examples:
**Basic Operations**
- 1. `add 5 7` - Adds 5 and 7.
- 2. `subtract 99 76` - Subtracts 76 from 99.
- 3. `multiply 84 364` - Multiplies 84 by 364.
- 4. `divide 875 35` - Divides 875 by 35 (also shows an error if division by zero is attempted).
- 5. `sqrt 49` - Gives the square root of 49.
- 6. `mean 978 348 479 987` - Gives average of these numbers.
- 7. `square 6` - Gives the square of 6. 
### History Management:
- `history` – Displays all past calculations.
- `clear_history` – Clears the calculation history.
- `edit_history <record_index> <command> <arg1> <arg2>` – Edits a specific history record.

### Plugin Commands:
- `plugins` – Lists any available plugin commands.

### Help and Exit:
- `help` – Displays the help message.
- `exit` – Saves the history and exits the calculator.

### Testing
- To run the test suite (including linting and coverage reports), execute:
- `pytest --pylint --cov`
- This command will run all tests and display the coverage percentage.

### Continuous Integration
- The project includes a GitHub Actions workflow that automatically runs tests on each push and pull request. The CI configuration is located in `.github/workflows/python-app.yml`.
