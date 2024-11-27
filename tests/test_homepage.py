from selenium import webdriver

def test_homepage():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Or provide the path to ChromeDriver: webdriver.Chrome(executable_path="/path/to/chromedriver")
    
    # Open the application in the browser
    driver.get("http://localhost:5002")  # Ensure your Flask app is running
    
    # Check if the page contains expected content
    assert "Data Analysis Results" in driver.page_source  # Change "Data Analysis Results" to match your actual page content

    # Close the browser
    driver.quit()

