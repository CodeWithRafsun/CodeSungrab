#!/usr/bin/env python3
# setup.py

from setuptools import setup
import os

# config.py থেকে ভার্সন পড়ে নিচ্ছি
version = "3.0.2"
with open('config.py', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('VERSION'):
            version = line.split('=')[1].strip().strip('"')
            break

# README.md পড়ে নিচ্ছি
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='codesungrab',
    version=version,
    author='Mahedi Hasan Rafsun',
    author_email='codewithrafsun@gmail.com',
    description='A modern command-line media downloader with Argentina flag theme (Argentina Victory Edition)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CodeWithRafsun/CodeSungrab',
    
    # সব পাইথন ফাইল লিস্ট করুন
    py_modules=[
        'main', 'config', 'downloader', 'menus', 
        'dashboard', 'validator', 'utils', 'banner', 'platforms'
    ],
    
    install_requires=[
        'yt-dlp>=2023.10.13',
        'rich>=13.7.0',
    ],
    
    entry_points={
        'console_scripts': [
            'sungrab=main:start',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities',
    ],
    keywords='youtube downloader video audio downloader yt-dlp termux media argentina',
    project_urls={
        'Bug Reports': 'https://github.com/CodeWithRafsun/CodeSungrab/issues',
        'Source': 'https://github.com/CodeWithRafsun/CodeSungrab',
        'Developer': 'https://codewithrafsun.vercel.app',
    },
)
