import datetime
from github import Github, GithubException, Auth
from .state import CodeGuardState

class GitHubIntegration:
    def __init__(self, token: str, repo_url: str):
        self.token = token
        self.repo_name = repo_url.replace("https://github.com/", "").strip("/")
        auth = Auth.Token(self.token)
        self.g = Github(auth=auth)
        
    def create_pull_request(self, state: CodeGuardState) -> str:
        if not self.token or self.token == "YOUR_GITHUB_TOKEN_HERE":
            return "Error: Invalid GitHub Token."
            
        try:
            repo = self.g.get_repo(self.repo_name)
            main_branch = repo.get_branch(repo.default_branch)
            
            branch_name = f"codeguard/auto-fix-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
            repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=main_branch.commit.sha)
            
            for fix in state.get('critic_approved_fixes', []):
                file_path = fix.get('issue_ref', {}).get('file')
                if not file_path: continue
                
                try:
                    contents = repo.get_contents(file_path, ref=branch_name)
                    decoded_content = contents.decoded_content.decode("utf-8")
                    new_content = decoded_content.replace(fix.get('original_code', ''), fix.get('fixed_code', ''))
                    
                    if new_content != decoded_content:
                        repo.update_file(
                            contents.path, 
                            f"Fix {fix.get('issue_ref', {}).get('issue_type')} via CodeGuard",
                            new_content, 
                            contents.sha, 
                            branch=branch_name
                        )
                except Exception as e:
                    print(f"Failed to update file {file_path}: {e}")
                    
            if state.get('changelog_entry'):
                try:
                    repo.create_file("CHANGELOG_UPDATE.md", "Add CodeGuard Changelog", state['changelog_entry'], branch=branch_name)
                except: pass
                
            pr = repo.create_pull(
                title=state.get('pr_title', f"CodeGuard Automated Fixes - {datetime.datetime.now().strftime('%Y-%m-%d')}"),
                body=state.get('pr_description', "Automated security and bug fixes."),
                head=branch_name,
                base=repo.default_branch
            )
            return pr.html_url
            
        except GithubException as e:
            return f"GitHub API Error: {e.data.get('message', str(e))}"
        except Exception as e:
            return f"Failed to create PR: {str(e)}"
