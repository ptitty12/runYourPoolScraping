from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

try:
    print("Loading brackets from CSV...")
    brackets = pd.read_csv(r"C:\Users\Patrick Taylor\Downloads\Bracket_Standings_Report (1).csv")
    entries = tuple(zip(brackets.ID, brackets.Entry))
    print(f"Found {len(entries)} brackets to process")
    
    # setup chrome options
    print("Setting up Chrome...")
    options = Options()
    options.add_argument("--headless")  # run in headless mode
    
    # initialize the driver
    driver = webdriver.Chrome(options=options)
    print("Chrome initialized successfully")
    
    # load cookies
    print("Loading cookies...")
    driver.get("https://www.runyourpool.com")
    for name, value in cookies.items():
        try:
            driver.add_cookie({"name": name, "value": value})
        except Exception as e:
            print(f"Warning: Could not add cookie {name}: {e}")
    print("Cookies loaded")
    
    # navigate to bracket page
    processed = 0
    failed = 0
    print("Beginning to process brackets...")
    
    for (k, v) in entries:
        try:
            print(f"Processing bracket {processed+failed+1}/{len(entries)}: ID={k}, Entry={v}")
            driver.get(f"https://www.runyourpool.com/MarchMadness/ncaa_bracket/bracket/view_bracket.cfm?t={k}&s={v}")
            
            # wait for javascript to load content
            print(f"  Waiting for page to load...")
            time.sleep(5)
            
            # get fully rendered html
            html = driver.page_source
            
            # save to file
            print(f"  Saving HTML to file...")
            with open(f"bracket_{k}_selenium_{v}.html", "w", encoding="utf-8") as f:
                f.write(html)
            
            print(f"  Successfully saved bracket for {v}")
            processed += 1
        except Exception as e:
            print(f"  ERROR processing bracket {k} - {v}: {str(e)}")
            failed += 1
    
    print(f"Finished processing brackets. Successful: {processed}, Failed: {failed}")
except Exception as e:
    print(f"Fatal error: {str(e)}")
finally:
    try:
        driver.quit()
        print("Chrome driver closed")
    except:
        print("Note: Could not close Chrome driver (might not have been initialized)")
