
import pandas as pd
def read_html_as_text(file_path):
    """
    Reads an HTML file and returns its content as a string.

    Args:
        file_path (str): The path to the HTML file.

    Returns:
        str: The content of the HTML file as a string, or None if an error occurs.
    """
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            html_content = file.read()
            return html_content
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = r"C:\Users\Patrick Taylor\Downloads\bracket_6821140_selenium_2.html"  
html_text = read_html_as_text(file_path)

def mine_brackets(html_text):
    d = {}
    teams = ['Auburn','Alabama St.','Louisville','Creighton','Michigan','UC San Diego','Tex. A&amp;M','Yale','Ole Miss','UNC','Iowa St.','Lipscomb','Marquette','New Mex.','Mich. St.','Bryant','Florida','Norfolk St.','UConn','Oklahoma','Memphis','Colo. St.','Maryland','Gr. Canyon','Missouri','Drake','Texas Tech','UNCW','Kansas','Arkansas','St. Johns','Omaha','Duke','Mt. St. Marys','Miss. St.','Baylor','Oregon','Liberty','Arizona','Akron','BYU','VCU','Wisconsin','Montana','St. Marys','Vandy','Alabama','Rob. Morris','Houston','SIU Edwardsville','Gonzaga','Georgia','Clemson','McNeese St.','Purdue','High Point','Illinois','Xavier','Kentucky','Troy','UCLA','Utah St.','Tennessee','Wofford']

    for team in teams:
        idx = teams.index(team) + 1
        d[idx] = int(html_text.count(f'>{team}<')/2 -1)
    return d


import os
import re

directory_path = r"C:\Users\Patrick Taylor\Downloads\marchMadness\brackets"
all_brackets = {}
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):  # Process only files, excluding subdirectories
        filename_pattern = r'bracket_(\d+)_selenium_(\d+)\.html'
        match = re.search(filename_pattern, filename)
        if match:
            bracket_id = match.group(1)
            iteration = match.group(2)
            entry = bracket_id + '_' + iteration
            r_txt = read_html_as_text(file_path)
            all_brackets[entry] = mine_brackets(r_txt)


# Define the current Sweet 16 matchups
sweet_16_matchups = {
    "South1": (1, 5), #auburn michigan///1v5
    "South2": (9, 14), #ole miss, iowa state vs netmexio micogan state///9,11vs14,15
    "East1": (33, 37),   # duke vs oregon,arizona /// 33vs37,39
    "East2": (41, 45),   # BYU vs Saint marys, Alabama /// 41vs45,47
    "Midwest1": (49, 55), #Houston vs Purdue /// 49vs55
    "Midwest2": (59, 63), #Kentucky vs Tennese /// 59vs63
    "West1": (17, 22), # Florida vs Colorado St, Maryland  /// 17vs22,23
    "West2": (27, 30) #texas tech vs arkansa ///27vs30
}


def generate_all_outcomes():
    """Generate all possible tournament outcomes from Sweet 16 onward"""
    all_outcomes = []
    
    # For each Sweet 16 matchup, decide who wins and who loses
    for south1_winner in [sweet_16_matchups["South1"][0], sweet_16_matchups["South1"][1]]:
        south1_loser = sweet_16_matchups["South1"][1] if south1_winner == sweet_16_matchups["South1"][0] else sweet_16_matchups["South1"][0]
        
        for south2_winner in [sweet_16_matchups["South2"][0], sweet_16_matchups["South2"][1]]:
            south2_loser = sweet_16_matchups["South2"][1] if south2_winner == sweet_16_matchups["South2"][0] else sweet_16_matchups["South2"][0]
            
            for east1_winner in [sweet_16_matchups["East1"][0], sweet_16_matchups["East1"][1]]:
                east1_loser = sweet_16_matchups["East1"][1] if east1_winner == sweet_16_matchups["East1"][0] else sweet_16_matchups["East1"][0]
                
                for east2_winner in [sweet_16_matchups["East2"][0], sweet_16_matchups["East2"][1]]:
                    east2_loser = sweet_16_matchups["East2"][1] if east2_winner == sweet_16_matchups["East2"][0] else sweet_16_matchups["East2"][0]
                    
                    for midwest1_winner in [sweet_16_matchups["Midwest1"][0], sweet_16_matchups["Midwest1"][1]]:
                        midwest1_loser = sweet_16_matchups["Midwest1"][1] if midwest1_winner == sweet_16_matchups["Midwest1"][0] else sweet_16_matchups["Midwest1"][0]
                        
                        for midwest2_winner in [sweet_16_matchups["Midwest2"][0], sweet_16_matchups["Midwest2"][1]]:
                            midwest2_loser = sweet_16_matchups["Midwest2"][1] if midwest2_winner == sweet_16_matchups["Midwest2"][0] else sweet_16_matchups["Midwest2"][0]
                            
                            for west1_winner in [sweet_16_matchups["West1"][0], sweet_16_matchups["West1"][1]]:
                                west1_loser = sweet_16_matchups["West1"][1] if west1_winner == sweet_16_matchups["West1"][0] else sweet_16_matchups["West1"][0]
                                
                                for west2_winner in [sweet_16_matchups["West2"][0], sweet_16_matchups["West2"][1]]:
                                    west2_loser = sweet_16_matchups["West2"][1] if west2_winner == sweet_16_matchups["West2"][0] else sweet_16_matchups["West2"][0]
                                    
                                    # Elite 8 matchups
                                    for south_winner in [south1_winner, south2_winner]:
                                        south_loser = south2_winner if south_winner == south1_winner else south1_winner
                                        
                                        for east_winner in [east1_winner, east2_winner]:
                                            east_loser = east2_winner if east_winner == east1_winner else east1_winner
                                            
                                            for midwest_winner in [midwest1_winner, midwest2_winner]:
                                                midwest_loser = midwest2_winner if midwest_winner == midwest1_winner else midwest1_winner
                                                
                                                for west_winner in [west1_winner, west2_winner]:
                                                    west_loser = west2_winner if west_winner == west1_winner else west1_winner
                                                    
                                                    # Final Four: South vs East, Midwest vs West
                                                    for ff1_winner in [south_winner, east_winner]:
                                                        ff1_loser = east_winner if ff1_winner == south_winner else south_winner
                                                        
                                                        for ff2_winner in [midwest_winner, west_winner]:
                                                            ff2_loser = west_winner if ff2_winner == midwest_winner else midwest_winner
                                                            
                                                            # Championship
                                                            for champion in [ff1_winner, ff2_winner]:
                                                                runner_up = ff2_winner if champion == ff1_winner else ff1_winner
                                                                
                                                                # Create the outcome with all teams
                                                                outcome = {
                                                                    # Start with all teams at 2 wins (instead of 3)
                                                                    south1_loser: 2, south2_loser: 2,
                                                                    east1_loser: 2, east2_loser: 2,
                                                                    midwest1_loser: 2, midwest2_loser: 2,
                                                                    west1_loser: 2, west2_loser: 2,
                                                                    
                                                                    # Teams that made it to Elite 8 but lost: 3 wins (instead of 4)
                                                                    south_loser: 3, east_loser: 3,
                                                                    midwest_loser: 3, west_loser: 3,
                                                                    
                                                                    # Teams that made Final Four but lost: 4 wins (instead of 5)
                                                                    ff1_loser: 4, ff2_loser: 4,
                                                                    
                                                                    # Runner-up: 5 wins (instead of 6)
                                                                    runner_up: 5,
                                                                    
                                                                    # Champion: 6 wins (instead of 7)
                                                                    champion: 6
                                                                }
                                                                
                                                                all_outcomes.append(outcome)
    
    return all_outcomes
