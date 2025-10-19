#!/usr/bin/env python3
"""
Badge Generator for README files

Generates markdown badges based on project information.
Supports various badge types from shields.io and other services.
"""

import json
import sys
from typing import Dict, List, Optional
from urllib.parse import quote


class BadgeGenerator:
    """Generate badges for README files"""
    
    def __init__(self, project_info: Dict):
        """
        Initialize badge generator with project information
        
        Args:
            project_info: Dictionary containing project metadata
                - project_name: Name of the project
                - username: GitHub username/organization
                - language: Programming language
                - package_manager: npm, pip, cargo, etc.
                - license: License type (MIT, Apache-2.0, etc.)
                - ci_service: CI service (github-actions, travis, circle, etc.)
        """
        self.info = project_info
        self.shields_base = "https://img.shields.io"
    
    def generate_all(self) -> str:
        """Generate all applicable badges"""
        badges = []
        
        # Build status
        if self.info.get('ci_service'):
            badges.append(self.build_badge())
        
        # Version badge
        if self.info.get('package_manager'):
            badges.append(self.version_badge())
        
        # Downloads
        if self.info.get('package_manager') in ['npm', 'pypi']:
            badges.append(self.downloads_badge())
        
        # License
        if self.info.get('license'):
            badges.append(self.license_badge())
        
        # Language/Platform
        if self.info.get('language'):
            badges.append(self.language_badge())
        
        return '\n'.join(filter(None, badges))
    
    def build_badge(self) -> Optional[str]:
        """Generate CI/build status badge"""
        ci = self.info.get('ci_service', '').lower()
        username = self.info.get('username')
        project = self.info.get('project_name')
        
        if not all([username, project]):
            return None
        
        if ci == 'github-actions':
            workflow = self.info.get('workflow_name', 'CI')
            url = f"https://github.com/{username}/{project}/workflows/{workflow}/badge.svg"
            link = f"https://github.com/{username}/{project}/actions"
            return f"[![Build Status]({url})]({link})"
        
        elif ci == 'travis':
            branch = self.info.get('branch', 'main')
            url = f"https://travis-ci.org/{username}/{project}.svg?branch={branch}"
            link = f"https://travis-ci.org/{username}/{project}"
            return f"[![Build Status]({url})]({link})"
        
        elif ci == 'circleci':
            url = f"https://circleci.com/gh/{username}/{project}.svg?style=svg"
            link = f"https://circleci.com/gh/{username}/{project}"
            return f"[![CircleCI]({url})]({link})"
        
        return None
    
    def version_badge(self) -> Optional[str]:
        """Generate version badge"""
        pkg_manager = self.info.get('package_manager', '').lower()
        project = self.info.get('project_name')
        
        if not project:
            return None
        
        if pkg_manager == 'npm':
            url = f"{self.shields_base}/npm/v/{project}.svg"
            link = f"https://www.npmjs.com/package/{project}"
            return f"[![npm version]({url})]({link})"
        
        elif pkg_manager == 'pypi':
            url = f"{self.shields_base}/pypi/v/{project}.svg"
            link = f"https://pypi.org/project/{project}/"
            return f"[![PyPI version]({url})]({link})"
        
        elif pkg_manager == 'cargo':
            url = f"{self.shields_base}/crates/v/{project}.svg"
            link = f"https://crates.io/crates/{project}"
            return f"[![Crates.io]({url})]({link})"
        
        elif pkg_manager == 'gem':
            url = f"{self.shields_base}/gem/v/{project}.svg"
            link = f"https://rubygems.org/gems/{project}"
            return f"[![Gem Version]({url})]({link})"
        
        elif pkg_manager == 'nuget':
            url = f"{self.shields_base}/nuget/v/{project}.svg"
            link = f"https://www.nuget.org/packages/{project}/"
            return f"[![NuGet]({url})]({link})"
        
        return None
    
    def downloads_badge(self) -> Optional[str]:
        """Generate downloads badge"""
        pkg_manager = self.info.get('package_manager', '').lower()
        project = self.info.get('project_name')
        
        if not project:
            return None
        
        if pkg_manager == 'npm':
            url = f"{self.shields_base}/npm/dm/{project}.svg"
            link = f"https://www.npmjs.com/package/{project}"
            return f"[![npm downloads]({url})]({link})"
        
        elif pkg_manager == 'pypi':
            url = f"{self.shields_base}/pypi/dm/{project}.svg"
            link = f"https://pypi.org/project/{project}/"
            return f"[![PyPI downloads]({url})]({link})"
        
        return None
    
    def license_badge(self) -> Optional[str]:
        """Generate license badge"""
        license_type = self.info.get('license', '').upper()
        
        if not license_type:
            return None
        
        # Map common license formats
        license_map = {
            'MIT': ('MIT', 'yellow'),
            'APACHE-2.0': ('Apache_2.0', 'blue'),
            'APACHE': ('Apache_2.0', 'blue'),
            'GPL-3.0': ('GPLv3', 'blue'),
            'GPL': ('GPLv3', 'blue'),
            'BSD-3': ('BSD_3--Clause', 'blue'),
            'BSD': ('BSD_3--Clause', 'blue'),
        }
        
        license_info = license_map.get(license_type, (license_type, 'blue'))
        license_name, color = license_info
        
        url = f"{self.shields_base}/badge/License-{license_name}-{color}.svg"
        
        # Link to common license URLs
        license_links = {
            'MIT': 'https://opensource.org/licenses/MIT',
            'Apache_2.0': 'https://opensource.org/licenses/Apache-2.0',
            'GPLv3': 'https://www.gnu.org/licenses/gpl-3.0',
            'BSD_3--Clause': 'https://opensource.org/licenses/BSD-3-Clause',
        }
        
        link = license_links.get(license_name, 'LICENSE')
        
        return f"[![License]({url})]({link})"
    
    def language_badge(self) -> Optional[str]:
        """Generate programming language badge"""
        language = self.info.get('language', '')
        
        if not language:
            return None
        
        # Common language colors (from GitHub)
        language_colors = {
            'python': 'blue',
            'javascript': 'yellow',
            'typescript': 'blue',
            'rust': 'orange',
            'go': 'cyan',
            'java': 'red',
            'ruby': 'red',
            'php': 'purple',
            'c++': 'pink',
            'c': 'gray',
            'swift': 'orange',
            'kotlin': 'purple',
        }
        
        color = language_colors.get(language.lower(), 'blue')
        lang_display = language.capitalize()
        
        url = f"{self.shields_base}/badge/Language-{quote(lang_display)}-{color}.svg"
        
        return f"![Language: {lang_display}]({url})"
    
    def coverage_badge(self, coverage_service: str = 'codecov') -> Optional[str]:
        """Generate code coverage badge"""
        username = self.info.get('username')
        project = self.info.get('project_name')
        branch = self.info.get('branch', 'main')
        
        if not all([username, project]):
            return None
        
        if coverage_service == 'codecov':
            url = f"https://codecov.io/gh/{username}/{project}/branch/{branch}/graph/badge.svg"
            link = f"https://codecov.io/gh/{username}/{project}"
            return f"[![Coverage]({url})]({link})"
        
        elif coverage_service == 'coveralls':
            url = f"https://coveralls.io/repos/github/{username}/{project}/badge.svg?branch={branch}"
            link = f"https://coveralls.io/github/{username}/{project}?branch={branch}"
            return f"[![Coverage Status]({url})]({link})"
        
        return None
    
    def custom_badge(self, label: str, message: str, color: str = 'blue') -> str:
        """Generate a custom badge"""
        url = f"{self.shields_base}/badge/{quote(label)}-{quote(message)}-{color}"
        return f"![{label}]({url})"


def main():
    """Main entry point for command-line usage"""
    if len(sys.argv) < 2:
        print("Usage: generate_badges.py <project_info.json>")
        print("\nExample project_info.json:")
        print(json.dumps({
            "project_name": "my-awesome-lib",
            "username": "github-user",
            "language": "python",
            "package_manager": "pypi",
            "license": "MIT",
            "ci_service": "github-actions",
            "branch": "main"
        }, indent=2))
        sys.exit(1)
    
    # Read project info from JSON file
    with open(sys.argv[1], 'r') as f:
        project_info = json.load(f)
    
    # Generate badges
    generator = BadgeGenerator(project_info)
    badges = generator.generate_all()
    
    # Output
    print(badges)


if __name__ == '__main__':
    main()
