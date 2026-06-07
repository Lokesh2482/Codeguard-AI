import os

# Ollama Models configuration
OLLAMA_MODEL_PRIMARY = "qwen2.5-coder:7b"
OLLAMA_MODEL_SECONDARY = "qwen2.5-coder:7b"  # Resource optimized for T4 VRAM stability

# Tavily API Configuration
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "")

# Embedding Model for Severity Analysis
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Semantic References for Severity Scoring
SEVERITY_REFERENCES = {
    "CRITICAL": [
        "Remote code execution vulnerability discovered",
        "SQL injection allowing arbitrary database read or write access",
        "Hardcoded private cryptographic keys or admin credentials found",
        "Command injection through unvalidated user inputs passed to system shell"
    ],
    "HIGH": [
        "Cross-Site Scripting vulnerability allowing session hijacking",
        "Insecure direct object reference exposing sensitive user profiles",
        "Broken authentication handling missing secure session tokens",
        "Uncontrolled memory allocation leading to crash or resource starvation"
    ],
    "MEDIUM": [
        "Use of weak or outdated hashing algorithm like MD5 or SHA1",
        "Missing rate limiting on authentication API endpoints",
        "Internal stack traces leaked via public error messages",
        "Sensitive information logged to standard system logs in cleartext"
    ],
    "LOW": [
        "Dead code blocks or completely unused imports present",
        "Code style guide violations reducing maintainability",
        "Missing explicit documentation or docstrings on public APIs",
        "Slightly inefficient loop structure optimized away by compilers"
    ]
}
