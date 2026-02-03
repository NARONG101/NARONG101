#!/usr/bin/env python3
"""
Generate GitHub contribution snake animation.
This script generates SVG files showing your GitHub contributions as a snake.
"""

import os
import subprocess
import sys
from datetime import datetime

def run_command(cmd, cwd=None):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            cwd=cwd, 
            capture_output=True, 
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    """Main function to generate the snake animation."""
    print("🐍 Generating GitHub contribution snake animation...")
    
    # Get the GitHub username from environment or use default
    github_user = os.environ.get('GITHUB_USER', 'NARONG101')
    
    # Create output directory if it doesn't exist
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate the snake animation using the snk action
    # The action will generate SVG files based on GitHub contributions
    success, stdout, stderr = run_command(
        f'git config user.name "github-actions[bot]" && '
        f'git config user.email "github-actions[bot]@users.noreply.github.com"'
    )
    
    if not success:
        print(f"❌ Failed to configure git user: {stderr}")
        sys.exit(1)
    
    print(f"✅ GitHub user configured: {github_user}")
    print(f"📁 Output directory: {output_dir}")
    print(f"⏰ Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n📝 Note: The actual SVG generation is handled by the GitHub Action.")
    print("   This script is a placeholder for local execution.")
    print("\n✅ Snake generation script completed!")

if __name__ == '__main__':
    main()
