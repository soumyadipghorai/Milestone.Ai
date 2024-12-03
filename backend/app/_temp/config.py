from models.db_models import *

PDF_UPLOAD_DIR = "dump/pdf"
MD_STORE_DIR = "dump/markdown"
LANGUAGE_TO_EXTENSION = {
    'Python': '.py', 'JavaScript': '.js', 'TypeScript': '.ts', 'HTML': '.html', 
    'CSS': '.css', 'Java': '.java', 'Ruby': '.rb', 'PHP': '.php', 'C++': '.cpp', 
    'C': '.c', 'C#': '.cs', 'Go': '.go', 'Rust': '.rs', 'Swift': '.swift', 'Kotlin': '.kt', 
    'Objective-C': '.m', 'R': '.r', 'Jupyter Notebook': '.ipynb', 'Scala': '.scala', 
    'Shell Script': '.sh', 'Batch File': '.bat', 'Perl': '.pl', 'Lua': '.lua', 
    'JSON': '.json', 'XML': '.xml', 'YAML': '.yaml', 'SQL': '.sql', 'Markdown': '.md', 
    'Plain Text': '.txt', 'INI Config File': '.ini', 'TOML Config File': '.toml', 
    'Configuration File': '.cfg', 'Log File': '.log', 'Dockerfile': '.dockerfile', 
    'Makefile': '.makefile', 'Terraform': '.tf', 'PowerShell Script': '.ps1', 
    'Assembly': '.asm', 'C Header': '.h', 'TypeScript React': '.tsx', 
    'JavaScript React': '.jsx', 'Visual Basic': '.vb', 'Erlang': '.erl', 
    'Elixir': '.ex', 'Elixir Script': '.exs', 'Dart': '.dart', 'Groovy': '.groovy', 
    'Verilog': '.v', 'SystemVerilog': '.sv', 'Julia': '.jl', 'ASP': '.asp', 
    'JavaServer Pages': '.jsp', 'Sass': '.scss', 'LESS': '.less', 'CoffeeScript': '.coffee'
}

EXTENTION_TO_LANGUAGE = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript", 
    ".html": "HTML", ".css": "CSS", ".java": "Java", ".rb": "Ruby", 
    ".php": "PHP", ".cpp": "C++", ".c": "C", ".cs": "C#", ".go": "Go", 
    ".rs": "Rust", ".swift": "Swift", ".kt": "Kotlin", ".m": "Objective-C", 
    ".r": "R", ".ipynb": "Jupyter Notebook", ".scala": "Scala", 
    ".sh": "Shell Script", ".bat": "Batch File", ".pl": "Perl", 
    ".lua": "Lua", ".json": "JSON", ".xml": "XML", 
    ".yml": "YAML", ".yaml": "YAML", ".sql": "SQL", 
    ".md": "Markdown", ".txt": "Plain Text", ".ini": "INI Config File", 
    ".toml": "TOML Config File", ".cfg": "Configuration File", 
    ".log": "Log File", ".dockerfile": "Dockerfile", ".makefile": "Makefile", 
    ".tf": "Terraform", ".ps1": "PowerShell Script", ".asm": "Assembly", 
    ".h": "C Header", ".tsx": "TypeScript React", ".jsx": "JavaScript React", 
    ".vb": "Visual Basic", ".erl": "Erlang", ".ex": "Elixir", 
    ".exs": "Elixir Script", ".dart": "Dart", ".groovy": "Groovy", 
    ".v": "Verilog", ".sv": "SystemVerilog", ".jl": "Julia", ".php": "PHP", 
    ".asp": "ASP", ".jsp": "JavaServer Pages", ".scss": "Sass", 
    ".less": "LESS", ".coffee": "CoffeeScript"
}


SECRET_KEY = "adg7!W@1yqdb!@*&^wdWQSX*()*s783eyxgq"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

ROLE_MAPPING = {
    "student" : Student, "admin" : Admin, "instructor" : Instructor, 
    "support" : SupportTeam
}