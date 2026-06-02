from pathlib import Path

from setuptools import setup

ROOT = Path(__file__).resolve().parent
VERSION = (ROOT / 'VERSION').read_text(encoding='utf-8').strip().removeprefix('v')
README = (ROOT / 'README.md').read_text(encoding='utf-8')

setup(
    name='vcp-cli',
    version=VERSION,
    description='Local Python CLI and packaging surface for Vibe Coding Protocols',
    long_description=README,
    long_description_content_type='text/markdown',
    python_requires='>=3.9',
    packages=['vcp_cli'],
    entry_points={'console_scripts': ['vcp=vcp_cli.cli:main']},
)
