from typing import TypedDict, List, Dict, Any

class CodeGuardState(TypedDict):
    # Core Data Ingestion & Tracking
    repo_url: str
    cloned_path: str
    parsed_files: List[str]
    blame_map: Dict[str, Any]
    commit_history: List[Dict[str, Any]]
    
    # Analysis & Graph Logic
    detected_issues: List[Dict[str, Any]]
    scored_issues: List[Dict[str, Any]]
    blast_radius_map: Dict[int, int]
    user_approved_issues: List[int]
    guardrail_flags: List[str]
    tavily_context_map: Dict[int, str]
    consensus_log: List[str]
    
    # Mitigation & Verification Phase
    generated_fixes: List[Dict[str, Any]]
    critic_approved_fixes: List[Dict[str, Any]]
    critic_rejections: List[Dict[str, Any]]
    verification_results: List[Dict[str, Any]]
    generated_tests: List[Dict[str, Any]]
    
    # PR & Final Documentation Strategy
    pr_title: str
    pr_description: str
    changelog_entry: str
    reflection_summary: Dict[str, Any]
    final_status: str
    error_log: List[str]
