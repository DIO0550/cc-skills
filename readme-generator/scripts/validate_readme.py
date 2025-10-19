#!/usr/bin/env python3
"""
README Validator

Validates README.md files for completeness, structure, and quality.
Checks for required sections, proper formatting, and common issues.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict


class READMEValidator:
    """Validate README files for quality and completeness"""
    
    def __init__(self, readme_path: str):
        """
        Initialize validator with README file path
        
        Args:
            readme_path: Path to README.md file
        """
        self.path = Path(readme_path)
        if not self.path.exists():
            raise FileNotFoundError(f"README not found: {readme_path}")
        
        self.content = self.path.read_text(encoding='utf-8')
        self.lines = self.content.split('\n')
        self.issues = []
        self.warnings = []
        self.suggestions = []
    
    def validate_all(self) -> Tuple[bool, Dict]:
        """
        Run all validation checks
        
        Returns:
            Tuple of (is_valid, results_dict)
        """
        self.check_title()
        self.check_description()
        self.check_required_sections()
        self.check_code_blocks()
        self.check_links()
        self.check_length()
        self.check_formatting()
        
        results = {
            'valid': len(self.issues) == 0,
            'issues': self.issues,
            'warnings': self.warnings,
            'suggestions': self.suggestions,
            'score': self.calculate_score()
        }
        
        return results['valid'], results
    
    def check_title(self):
        """Check if README has a proper title (H1)"""
        h1_pattern = r'^# .+'
        
        # Find first H1
        h1_line = None
        for i, line in enumerate(self.lines[:10]):  # Check first 10 lines
            if re.match(h1_pattern, line):
                h1_line = i
                break
        
        if h1_line is None:
            self.issues.append("❌ Missing H1 title (# Project Name)")
        else:
            title = self.lines[h1_line].lstrip('# ').strip()
            if len(title) < 2:
                self.issues.append("❌ Title is too short")
            elif len(title) > 80:
                self.warnings.append("⚠️  Title is very long (>80 characters)")
    
    def check_description(self):
        """Check if README has a description"""
        # Look for description in first 20 lines
        has_description = False
        
        for line in self.lines[:20]:
            # Skip empty lines, titles, and badges
            if (line.strip() and 
                not line.startswith('#') and
                not line.startswith('[![') and
                not line.startswith('![') and
                len(line.strip()) > 20):
                has_description = True
                break
        
        if not has_description:
            self.issues.append("❌ Missing project description (add 1-2 sentences after title)")
    
    def check_required_sections(self):
        """Check for required README sections"""
        required_sections = {
            'installation': r'##\s+(Installation|Getting Started|Setup)',
            'usage': r'##\s+(Usage|Quick Start|Examples)',
            'license': r'##\s+License',
        }
        
        recommended_sections = {
            'contributing': r'##\s+(Contributing|Contribution)',
            'features': r'##\s+Features',
        }
        
        content_lower = self.content.lower()
        
        # Check required sections
        for name, pattern in required_sections.items():
            if not re.search(pattern, self.content, re.IGNORECASE):
                self.issues.append(f"❌ Missing required section: {name.capitalize()}")
        
        # Check recommended sections
        for name, pattern in recommended_sections.items():
            if not re.search(pattern, self.content, re.IGNORECASE):
                self.warnings.append(f"⚠️  Missing recommended section: {name.capitalize()}")
    
    def check_code_blocks(self):
        """Check code blocks are properly formatted"""
        # Find code blocks
        code_block_pattern = r'```(\w*)\n'
        code_blocks = re.finditer(code_block_pattern, self.content)
        
        unclosed_blocks = 0
        blocks_without_language = 0
        
        for match in code_blocks:
            language = match.group(1)
            if not language:
                blocks_without_language += 1
        
        # Check for unclosed code blocks
        opening_blocks = len(re.findall(r'```', self.content))
        if opening_blocks % 2 != 0:
            self.issues.append("❌ Unclosed code block (missing closing ```)")
        
        if blocks_without_language > 0:
            self.suggestions.append(
                f"💡 {blocks_without_language} code block(s) without language specification"
            )
    
    def check_links(self):
        """Check for broken or empty links"""
        # Find markdown links
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.finditer(link_pattern, self.content)
        
        empty_links = 0
        suspicious_links = []
        
        for match in links:
            text = match.group(1)
            url = match.group(2)
            
            # Check for empty URLs
            if not url or url.isspace():
                empty_links += 1
            
            # Check for placeholder URLs
            if any(placeholder in url.lower() for placeholder in 
                   ['example.com', 'your-', 'placeholder', 'todo']):
                suspicious_links.append(f"{text} -> {url}")
        
        if empty_links > 0:
            self.issues.append(f"❌ {empty_links} empty link(s) found")
        
        if suspicious_links:
            self.warnings.append(
                f"⚠️  {len(suspicious_links)} placeholder link(s) found:\n" +
                '\n'.join(f"     - {link}" for link in suspicious_links[:3])
            )
    
    def check_length(self):
        """Check README length"""
        line_count = len(self.lines)
        word_count = len(self.content.split())
        
        if line_count < 20:
            self.warnings.append("⚠️  README is very short (<20 lines)")
        elif line_count > 1000:
            self.suggestions.append(
                "💡 README is very long (>1000 lines). Consider splitting into multiple docs"
            )
        
        if word_count < 50:
            self.issues.append("❌ README is too short (<50 words)")
    
    def check_formatting(self):
        """Check formatting and style"""
        # Check for consistent heading levels
        headings = []
        for line in self.lines:
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                headings.append(level)
        
        # Check for skipped heading levels
        if headings:
            for i in range(len(headings) - 1):
                if headings[i+1] - headings[i] > 1:
                    self.warnings.append(
                        "⚠️  Skipped heading level (e.g., H1 -> H3 without H2)"
                    )
                    break
        
        # Check for multiple H1s
        h1_count = sum(1 for h in headings if h == 1)
        if h1_count > 1:
            self.warnings.append(f"⚠️  Multiple H1 headings ({h1_count}). Use only one H1 for title")
        elif h1_count == 0:
            self.issues.append("❌ No H1 heading found")
        
        # Check for very long lines
        long_lines = sum(1 for line in self.lines if len(line) > 120 and not line.startswith('http'))
        if long_lines > 10:
            self.suggestions.append(f"💡 {long_lines} lines are very long (>120 chars)")
    
    def calculate_score(self) -> int:
        """
        Calculate quality score (0-100)
        
        Scoring:
        - Start at 100
        - -10 for each issue
        - -3 for each warning
        - No penalty for suggestions
        """
        score = 100
        score -= len(self.issues) * 10
        score -= len(self.warnings) * 3
        
        return max(0, min(100, score))
    
    def print_results(self, results: Dict):
        """Print validation results"""
        print("\n" + "="*60)
        print(f"README Validation Results: {self.path}")
        print("="*60)
        
        # Score
        score = results['score']
        if score >= 80:
            emoji = "🎉"
            rating = "Excellent"
        elif score >= 60:
            emoji = "👍"
            rating = "Good"
        elif score >= 40:
            emoji = "😐"
            rating = "Fair"
        else:
            emoji = "😞"
            rating = "Needs Improvement"
        
        print(f"\nScore: {score}/100 {emoji} ({rating})")
        
        # Issues
        if results['issues']:
            print(f"\n❌ Issues ({len(results['issues'])}):")
            for issue in results['issues']:
                print(f"   {issue}")
        else:
            print("\n✅ No critical issues found!")
        
        # Warnings
        if results['warnings']:
            print(f"\n⚠️  Warnings ({len(results['warnings'])}):")
            for warning in results['warnings']:
                print(f"   {warning}")
        
        # Suggestions
        if results['suggestions']:
            print(f"\n💡 Suggestions ({len(results['suggestions'])}):")
            for suggestion in results['suggestions']:
                print(f"   {suggestion}")
        
        # Summary
        print("\n" + "="*60)
        if results['valid']:
            print("✅ README validation passed!")
        else:
            print("❌ README validation failed. Please fix the issues above.")
        print("="*60 + "\n")


def main():
    """Main entry point for command-line usage"""
    if len(sys.argv) < 2:
        print("Usage: validate_readme.py <path/to/README.md>")
        print("\nExample:")
        print("  python validate_readme.py README.md")
        sys.exit(1)
    
    readme_path = sys.argv[1]
    
    try:
        validator = READMEValidator(readme_path)
        is_valid, results = validator.validate_all()
        validator.print_results(results)
        
        # Exit with appropriate code
        sys.exit(0 if is_valid else 1)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
