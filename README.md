# Web Scraping 

This Python script performs web scraping on the TenderTiger website to extract tender information and stores it in a Google Sheets document. The script uses the Selenium library to automate browsing and data extraction.

## Prerequisites

Before running the script, make sure you have the following:

1. Python (version 3.6 or later) installed.
2. Chrome WebDriver installed and its executable path configured in the script.
3. Google API credentials (`auth.json`) for accessing Google Sheets.

## Installation

1. Clone the repository:   
<button onclick="copyToClipboard('git-clone')"></button>
``` shell
git clone https://github.com/notTanveer/WebScraping.git
```

2.  Run the following command to install the required Python packages:
<button onclick="copyToClipboard('pip-install')"></button>

```shell
pip install -r requirements.txt 
```

## Usage

1. Replace `path_to_webdriver` with the actual path to your Chrome WebDriver executable in the `main.py` script.
2. Replace `auth.json` with your Google API credentials file in the project directory.
3. Run the script:


The script will perform the following steps:

1. Open a Chrome browser and navigate to the TenderTiger website.
2. Click the "Load More" button ten times to load more tender information.
3. Extract tender information for each item and store it in a Google Sheets document named "Data."

Note: The script includes a rate limit compliance mechanism. After 299 API requests, the script will pause for 45 seconds to comply with API rate limits.

## Configuration

You can adjust the number of times the "Load More" button is clicked and the data extraction details by modifying the `main.py` script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## Usage

1. Replace `path_to_webdriver` with the actual path to your Chrome WebDriver executable in the `main.py` script.
2. Replace `auth.json` with your Google API credentials file in the project directory.
3. Run the script:


The script will perform the following steps:

1. Open a Chrome browser and navigate to the TenderTiger website.
2. Click the "Load More" button ten times to load more tender information.
3. Extract tender information for each item and store it in a Google Sheets document named "Data."

Note: The script includes a rate limit compliance mechanism. After 299 API requests, the script will pause for 45 seconds to comply with API rate limits.

## Configuration

You can adjust the number of times the "Load More" button is clicked and the data extraction details by modifying the `main.py` script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Usage

1. Replace `path_to_webdriver` with the actual path to your Chrome WebDriver executable in the `main.py` script.
2. Replace `auth.json` with your Google API credentials file in the project directory.
3. Run the script:


The script will perform the following steps:

1. Open a Chrome browser and navigate to the TenderTiger website.
2. Click the "Load More" button ten times to load more tender information.
3. Extract tender information for each item and store it in a Google Sheets document named "Data."

Note: The script includes a rate limit compliance mechanism. After 299 API requests, the script will pause for 45 seconds to comply with API rate limits.

## Configuration

You can adjust the number of times the "Load More" button is clicked and the data extraction details by modifying the `main.py` script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
