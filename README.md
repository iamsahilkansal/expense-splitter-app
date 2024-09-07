# expense-splitter-app

This project is a web application that helps split group expenses efficiently by minimizing the number of transactions required. The app takes into account the amounts spent by each person and settles the debts in the minimum possible transactions using Graph Theory and Dynamic Programming.

## Features

- **Efficient Transaction Reduction:** Reduces the number of transactions required to settle expenses within a group, often far fewer than the traditional method.
- **Dynamic Programming & Graph Algorithm:** Utilizes advanced algorithms to minimize intermediary transactions, directly calculating the optimal settlement path.
- **User-Friendly Interface:** Simple interface for users to input expenses and instantly view the results.
- **Multi-person Group Support:** Handles expenses for any number of people in a group.

## Tech Stack

- **Frontend:** Streamlit (Python-based web framework)
- **Backend Logic:** Python, Graphs, Dynamic Programming
- **Deployment:** Python

## How It Works

1. Input the number of people and the amount each person has spent.
2. The app processes the expenses using dynamic programming and graphs to minimize transactions.
3. The minimum number of transactions required to settle the debts will be displayed.

## Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- **Streamlit** library for building the web interface.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/iamsahilkansal/expense-splitter-app.git
   ```
2. Navigate to the project directory:

   ```bash
   cd expense-splitter-app
   ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

### Usage

- After running the app, you will see a web interface in your browser.
- Input the number of people and their respective expenses.
- The app will calculate and display the minimum number of transactions to settle the expenses.

## Example

For example, consider the following group with 5 people and their respective expenses:

- A spent ₹500
- B spent ₹1000
- C spent ₹700
- D spent ₹300
- E spent ₹600

Instead of each person paying others directly, the app will calculate the fewest possible transactions, optimizing settlement paths.

In a typical case, this could reduce the number of transactions from 20 to 4 by eliminating unnecessary intermediary transfers (e.g., A -> B -> C is directly reduced to A -> C).

## Project Structure

expense-splitter-app
├── app.py # Main Streamlit app an Core logic for minimizing transactions
├── README.md # Project documentation
├── requirements.txt # Project dependencies
└── assets/ # Any static assets (images, etc.)

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. Any improvements in algorithm efficiency, features, or UI are highly appreciated!

## Contact

If you have any questions or feedback, feel free to reach out:

- **Email:** kansalsahil51@gmail.com
- **GitHub:** [iamsahilkansal](https://github.com/iamsahilkansal)
