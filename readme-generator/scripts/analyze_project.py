#!/usr/bin/env python3
"""
Project Analyzer

Analyzes project directory structure and files to infer project information.
Useful for auto-generating README content based on project characteristics.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
import re


class ProjectAnalyzer:
    """Analyze project structure and infer metadata"""
    
    def __init__(self, project_dir: str = '.'):
        """
        Initialize analyzer with project directory
        
        Args:
            project_dir: Path to project root directory
        """
        self.root = Path(project_dir).resolve()
        if not self.root.exists():
            raise FileNotFoundError(f"Project directory not found: {project_dir}")
        
        self.analysis = {}
    
    def analyze(self) -> Dict:
        """
        Perform complete project analysis
        
        Returns:
            Dictionary containing project metadata
        """
        self.analysis = {
            'project_name': self.detect_project_name(),
            'language': self.detect_language(),
            'project_type': self.detect_project_type(),
            'package_manager': self.detect_package_manager(),
            'has_tests': self.has_tests(),
            'ci_service': self.detect_ci(),
            'dependencies_file': self.find_dependencies_file(),
            'build_system': self.detect_build_system(),
            'framework': self.detect_framework(),
            'description': self.extract_description(),
            'version': self.extract_version(),
            'license': self.detect_license(),
            'has_docs': self.has_documentation(),
            'git_repo': self.is_git_repo()
        }
        
        return self.analysis
    
    def detect_project_name(self) -> Optional[str]:
        """Detect project name from various sources"""
        # Try package.json
        pkg_json = self.root / 'package.json'
        if pkg_json.exists():
            try:
                data = json.loads(pkg_json.read_text())
                return data.get('name')
            except:
                pass
        
        # Try setup.py
        setup_py = self.root / 'setup.py'
        if setup_py.exists():
            content = setup_py.read_text()
            match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
        
        # Try Cargo.toml
        cargo_toml = self.root / 'Cargo.toml'
        if cargo_toml.exists():
            content = cargo_toml.read_text()
            match = re.search(r'name\s*=\s*"([^"]+)"', content)
            if match:
                return match.group(1)
        
        # Try pyproject.toml
        pyproject = self.root / 'pyproject.toml'
        if pyproject.exists():
            content = pyproject.read_text()
            match = re.search(r'name\s*=\s*"([^"]+)"', content)
            if match:
                return match.group(1)
        
        # Fall back to directory name
        return self.root.name
    
    def detect_language(self) -> Optional[str]:
        """Detect primary programming language"""
        # Count files by extension
        extensions = {}
        
        for file in self.root.rglob('*'):
            if file.is_file() and not any(part.startswith('.') for part in file.parts):
                ext = file.suffix.lower()
                if ext:
                    extensions[ext] = extensions.get(ext, 0) + 1
        
        # Map extensions to languages
        lang_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.rs': 'Rust',
            '.go': 'Go',
            '.java': 'Java',
            '.rb': 'Ruby',
            '.php': 'PHP',
            '.cpp': 'C++',
            '.c': 'C',
            '.cs': 'C#',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.scala': 'Scala',
            '.r': 'R',
        }
        
        # Find most common language file
        if extensions:
            most_common_ext = max(extensions, key=extensions.get)
            return lang_map.get(most_common_ext, most_common_ext[1:].upper())
        
        return None
    
    def detect_project_type(self) -> str:
        """Detect project type (library, webapp, cli-tool, etc.)"""
        # Check for web framework indicators
        web_indicators = [
            'app.py', 'server.js', 'index.html', 'views/', 'templates/',
            'public/', 'static/', 'routes/', 'controllers/'
        ]
        
        for indicator in web_indicators:
            if (self.root / indicator).exists():
                return 'webapp'
        
        # Check for CLI indicators
        cli_indicators = ['main.rs', 'cli.py', 'cmd/', 'bin/']
        for indicator in cli_indicators:
            if (self.root / indicator).exists():
                # Check if it's a library with CLI
                if (self.root / 'src' / 'lib.rs').exists() or (self.root / 'lib').exists():
                    return 'library'
                return 'cli-tool'
        
        # Check package files
        if (self.root / 'setup.py').exists() or (self.root / 'Cargo.toml').exists():
            return 'library'
        
        if (self.root / 'package.json').exists():
            try:
                pkg = json.loads((self.root / 'package.json').read_text())
                if pkg.get('bin'):
                    return 'cli-tool'
                return 'library'
            except:
                pass
        
        return 'application'
    
    def detect_package_manager(self) -> Optional[str]:
        """Detect package manager"""
        managers = {
            'package.json': 'npm',
            'yarn.lock': 'yarn',
            'pnpm-lock.yaml': 'pnpm',
            'setup.py': 'pip',
            'requirements.txt': 'pip',
            'Pipfile': 'pipenv',
            'poetry.lock': 'poetry',
            'Cargo.toml': 'cargo',
            'go.mod': 'go',
            'Gemfile': 'bundler',
            'composer.json': 'composer',
            'pom.xml': 'maven',
            'build.gradle': 'gradle',
        }
        
        for file, manager in managers.items():
            if (self.root / file).exists():
                return manager
        
        return None
    
    def has_tests(self) -> bool:
        """Check if project has tests"""
        test_indicators = [
            'test/', 'tests/', 'spec/', '__tests__/',
            'test_*.py', '*_test.py', '*.test.js', '*.spec.js'
        ]
        
        for indicator in test_indicators:
            if '*' in indicator:
                # Pattern matching
                if list(self.root.rglob(indicator)):
                    return True
            else:
                # Directory/file check
                if (self.root / indicator).exists():
                    return True
        
        return False
    
    def detect_ci(self) -> Optional[str]:
        """Detect CI/CD service"""
        ci_files = {
            '.github/workflows': 'github-actions',
            '.travis.yml': 'travis',
            '.circleci': 'circleci',
            '.gitlab-ci.yml': 'gitlab-ci',
            'Jenkinsfile': 'jenkins',
            '.drone.yml': 'drone',
            'azure-pipelines.yml': 'azure-pipelines',
        }
        
        for file, service in ci_files.items():
            if (self.root / file).exists():
                return service
        
        return None
    
    def find_dependencies_file(self) -> Optional[str]:
        """Find dependencies file"""
        dep_files = [
            'requirements.txt', 'Pipfile', 'package.json',
            'Cargo.toml', 'go.mod', 'Gemfile', 'pom.xml'
        ]
        
        for file in dep_files:
            if (self.root / file).exists():
                return file
        
        return None
    
    def detect_build_system(self) -> Optional[str]:
        """Detect build system"""
        build_systems = {
            'Makefile': 'make',
            'CMakeLists.txt': 'cmake',
            'build.gradle': 'gradle',
            'pom.xml': 'maven',
            'webpack.config.js': 'webpack',
            'rollup.config.js': 'rollup',
            'vite.config.js': 'vite',
        }
        
        for file, system in build_systems.items():
            if (self.root / file).exists():
                return system
        
        return None
    
    def detect_framework(self) -> Optional[str]:
        """Detect web framework"""
        # Check package.json
        pkg_json = self.root / 'package.json'
        if pkg_json.exists():
            try:
                data = json.loads(pkg_json.read_text())
                deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                
                frameworks = ['react', 'vue', 'angular', 'svelte', 'next', 'nuxt', 'express']
                for fw in frameworks:
                    if fw in deps:
                        return fw
            except:
                pass
        
        # Check Python frameworks
        if (self.root / 'manage.py').exists():
            return 'django'
        
        if (self.root / 'app.py').exists() or (self.root / 'main.py').exists():
            try:
                for py_file in self.root.glob('*.py'):
                    content = py_file.read_text()
                    if 'from flask import' in content or 'import flask' in content:
                        return 'flask'
                    if 'from fastapi import' in content or 'import fastapi' in content:
                        return 'fastapi'
            except:
                pass
        
        return None
    
    def extract_description(self) -> Optional[str]:
        """Extract project description"""
        # Try package.json
        pkg_json = self.root / 'package.json'
        if pkg_json.exists():
            try:
                data = json.loads(pkg_json.read_text())
                if 'description' in data:
                    return data['description']
            except:
                pass
        
        # Try Cargo.toml
        cargo_toml = self.root / 'Cargo.toml'
        if cargo_toml.exists():
            content = cargo_toml.read_text()
            match = re.search(r'description\s*=\s*"([^"]+)"', content)
            if match:
                return match.group(1)
        
        # Try README
        for readme in ['README.md', 'README.rst', 'README.txt']:
            readme_path = self.root / readme
            if readme_path.exists():
                try:
                    lines = readme_path.read_text().split('\n')
                    # Find first substantial line after title
                    for line in lines[1:10]:
                        line = line.strip()
                        if line and not line.startswith('#') and not line.startswith('[') and len(line) > 20:
                            return line.strip('> ').strip()
                except:
                    pass
        
        return None
    
    def extract_version(self) -> Optional[str]:
        """Extract project version"""
        # Try package.json
        pkg_json = self.root / 'package.json'
        if pkg_json.exists():
            try:
                data = json.loads(pkg_json.read_text())
                return data.get('version')
            except:
                pass
        
        # Try Cargo.toml
        cargo_toml = self.root / 'Cargo.toml'
        if cargo_toml.exists():
            content = cargo_toml.read_text()
            match = re.search(r'version\s*=\s*"([^"]+)"', content)
            if match:
                return match.group(1)
        
        # Try setup.py
        setup_py = self.root / 'setup.py'
        if setup_py.exists():
            content = setup_py.read_text()
            match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
            if match:
                return match.group(1)
        
        return None
    
    def detect_license(self) -> Optional[str]:
        """Detect license type"""
        license_files = ['LICENSE', 'LICENSE.txt', 'LICENSE.md', 'COPYING']
        
        for license_file in license_files:
            path = self.root / license_file
            if path.exists():
                try:
                    content = path.read_text()
                    # Simple license detection
                    if 'MIT License' in content:
                        return 'MIT'
                    elif 'Apache License' in content and '2.0' in content:
                        return 'Apache-2.0'
                    elif 'GNU GENERAL PUBLIC LICENSE' in content and 'Version 3' in content:
                        return 'GPL-3.0'
                    elif 'BSD' in content:
                        return 'BSD'
                except:
                    pass
        
        # Check package.json
        pkg_json = self.root / 'package.json'
        if pkg_json.exists():
            try:
                data = json.loads(pkg_json.read_text())
                return data.get('license')
            except:
                pass
        
        return None
    
    def has_documentation(self) -> bool:
        """Check if project has documentation"""
        doc_indicators = ['docs/', 'doc/', 'documentation/', 'README.md']
        
        for indicator in doc_indicators:
            if (self.root / indicator).exists():
                return True
        
        return False
    
    def is_git_repo(self) -> bool:
        """Check if project is a git repository"""
        return (self.root / '.git').exists()
    
    def print_analysis(self):
        """Print analysis results in a readable format"""
        print("\n" + "="*60)
        print("Project Analysis Results")
        print("="*60 + "\n")
        
        for key, value in self.analysis.items():
            if value is not None:
                key_display = key.replace('_', ' ').title()
                print(f"{key_display:.<30} {value}")
        
        print("\n" + "="*60 + "\n")


def main():
    """Main entry point for command-line usage"""
    project_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    try:
        analyzer = ProjectAnalyzer(project_dir)
        results = analyzer.analyze()
        
        # Print results
        analyzer.print_analysis()
        
        # Also output as JSON
        print("JSON Output:")
        print(json.dumps(results, indent=2))
    
    except Exception as e:
        print(f"Error analyzing project: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
