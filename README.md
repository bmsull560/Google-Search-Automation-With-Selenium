# Google Search Automation with Selenium

This project demonstrates how to use **Selenium**, a powerful browser automation tool, to perform automated Google searches and extract search results. The script interacts with the Google homepage, performs a search based on a user-defined query, and retrieves the titles and URLs of the top search results, saving them to a text file.

## Key Features
- **Automated Search**: Inputs a search query into Google's search bar and executes the search.
- **Result Extraction**: Extracts the titles and URLs of the top search results.
- **File Output**: Saves the extracted data in a structured format to a text file.
- **User-Friendly**: Minimal setup with straightforward configuration (e.g., path to the ChromeDriver).

## Technologies Used
- **Python**: The core programming language for automation and data handling.
- **Selenium WebDriver**: For browser automation and DOM interaction.
- **ChromeDriver**: To enable Selenium to interface with Google Chrome.

## Prerequisites
1. **Python**: Install Python (version 3.6 or higher).
2. **Selenium**: Install Selenium using `pip install selenium`.
3. **ChromeDriver**: Download the ChromeDriver compatible with your version of Chrome and update the path in the script.

## How to Run
1. Clone or download this repository.
2. Ensure you have the required dependencies installed.
3. Update the `chromedriver.exe` path in the script if necessary.
4. Run the script:
   ```bash
   python script_name.py
   ```
5. The top search results will be saved to a file named `google_search_results.txt`.

## File Structure
- `script.py`: The main script for automating the search and extracting results.
- `google_search_results.txt`: Output file containing the titles and URLs of the top search results.

## Use Cases
- Quickly gather information or data from Google for research.
- Automate repetitive search tasks.
- Develop further insights or tools that rely on search data (e.g., keyword analysis, web scraping projects).

## Notes
- Ensure the version of ChromeDriver matches the version of Chrome installed on your system.
- Adjust the script's sleep time (`time.sleep(2)`) if the results take longer to load on your network.

## License
This project is licensed under the MIT License. Feel free to use and modify it for personal or commercial purposes.
