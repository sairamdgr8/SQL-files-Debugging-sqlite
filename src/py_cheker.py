from github import Github
g=Github("sairamdgr8","XXXXXXXXX")

for repo in g.get_user().get_repos():
    print(repo.name)
	
repo=g.get_repo("sairamdgr8/SQL-files-Debugging-sqlite")