from github import Github

from random import randint
import os
import json


def main():
    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
    issue = repo.get_issue(number=int(os.environ["ISSUE_NUMBER"]))

    issueTitle  = issue.title
    issueAuthor = "@" + issue.user.login

    issueArguments = issueTitle.split("|")
    issueType = issueArguments[1]

    if issueType == "newgame":
        newGame()

class createNewCurrentFile:
    def __init__(self, grid, score, bestScore, lastMoves):
        self.grid = grid,
        self.score = score,
        self.bestScore = bestScore,
        self.lastMoves = lastMoves

def newGame():
    """Create a new 2048 game"""

    grid = [
            [None, None, None], 
            [None, None, None], 
            [None, None, None]
        ]
    
    # Add random number
    gridLine = randint(0, 2)
    gridCase = randint(0, 2)
    grid[gridLine][gridCase] = 2

    # Write the current file
    bestScore = 0
    with open("Data/bestScore.txt", "r") as _bestScore:
        bestScore = int(_bestScore)

    currentFile = createNewCurrentFile(grid, 0, bestScore, [])

    with open("Data/Games/current.json", "w") as _current:
        currentFile = json.dumps(currentFile.__dict__, indent=4, ensure_ascii=False) # Convert the object to json
        _current.write(currentFile)

    

    # issue.create_comment(f"{issueAuthor} --- {issueTitle} test!")



if __name__ == "__main__":
	main() 