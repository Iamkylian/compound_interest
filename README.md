# Compound Interest Calculator

## Sommaire
- [Compound Interest Calculator](#compound-interest-calculator)
  - [Sommaire](#sommaire)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Error Handling](#error-handling)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

---

## Introduction

This project is a simple desktop application for calculating compound interest, developed using Python and PyQt5. The application allows users to input initial investment details and calculates the final amount based on the specified interest rate, duration, and compounding frequency. Additionally, the results can be saved to an Excel file.

---

## Features

- **Initial Amount Input**: Enter the starting amount in euros.
- **Interest Rate Selection**: Choose an interest rate from 1% to 10%.
- **Duration Selection**: Select a duration from 1 to 20 years.
- **Compounding Frequency**: Options for weekly, bi-monthly, or monthly compounding.
- **Calculate Final Amount**: Compute the final amount using the compound interest formula.
- **Save Results to Excel**: Save yearly results to an Excel file for further analysis.

---

## Requirements

- Python 3.x
- PyQt5
- pandas
- openpyxl (for Excel file handling)

---

## Installation

1. Clone this repository to your local machine.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

3. Run the application using the following command:

```bash
python process_compound_interest.py
```

---

## Usage

1. Launch the application.
2. Enter the initial amount in euros.
3. Select the desired interest rate from the dropdown menu.
4. Choose the duration in years.
5. Select the compounding frequency (weekly, bi-monthly, or monthly).
6. Click "Calculate" to see the final amount after the specified duration.
7. To save results, click "Save to Excel", which will generate a `compound_interest_results.xlsx` file with yearly breakdowns.

---

## Error Handling

The application includes basic error handling for invalid input values and missing parameters, providing user feedback through message boxes.

---

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

This project utilizes PyQt5 for GUI development and pandas for data management and Excel file creation.
