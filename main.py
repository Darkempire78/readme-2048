from github import Github

import os


def main():
    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
    issue = repo.get_issue(number=int(os.environ["ISSUE_NUMBER"]))

    issueTitle  = issue.title
    issueAuthor = "@" + issue.user.login

    print("test")
    issue.create_comment(f"{issueAuthor} --- {issueTitle} test!")



if __name__ == "__main__":
	main()