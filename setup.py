"""
Real Estate Intelligence Platform Setup Configuration
====================================================

Advanced ML-powered real estate analytics platform with price prediction,
property recommendations, market analysis, and comprehensive MLOps integration.

Author: Real Estate Intelligence Team
License: MIT
Python: >=3.13.7
"""

from setuptools import setup, find_packages
from pathlib import Path
import os

# Read the README file for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements from requirements.txt
def read_requirements():
    """Read requirements from requirements.txt file."""
    requirements_path = this_directory / "requirements.txt"
    if requirements_path.exists():
        with open(requirements_path, 'r', encoding='utf-8') as f:
            requirements = [
                line.strip() 
                for line in f.readlines() 
                if line.strip() and not line.startswith('#')
            ]
        return requirements
    return []

# Package metadata
PACKAGE_NAME = "real_estate_intelligence_platform"
VERSION = "1.0.0"
AUTHOR = "Real Estate Intelligence Team"
AUTHOR_EMAIL = "team@realestateintelligence.com"
DESCRIPTION = "Advanced ML-powered real estate analytics platform"
URL = "https://github.com/yourusername/real-estate-intelligence-platform"
LICENSE = "MIT"

# Python version requirement
PYTHON_REQUIRES = ">=3.13.7"

# Package classifiers for PyPI
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.13",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Office/Business :: Financial",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Framework :: Flask",
    "Environment :: Web Environment",
]

# Keywords for package discovery
KEYWORDS = [
    "real-estate", "machine-learning", "price-prediction", "property-analytics",
    "market-analysis", "flask", "mlops", "regression", "recommendation-system",
    "data-science", "artificial-intelligence", "property-valuation", "xgboost",
    "lightgbm", "shap", "explainable-ai", "real-estate-investment", "mlflow"
]

# Project URLs
PROJECT_URLS = {
    "Bug Reports": f"{URL}/issues",
    "Source": URL,
    "Documentation": f"{URL}/wiki",
    "Funding": f"{URL}/sponsors",
    "Say Thanks!": f"https://twitter.com/intent/tweet?text=Thanks%20for%20Real%20Estate%20Intelligence%20Platform!",
}

# Entry points for command-line scripts
ENTRY_POINTS = {
    'console_scripts': [
        'real-estate-train=scripts.train_models:main',
        'real-estate-predict=scripts.predict:main',
        'real-estate-server=web_app.app:main',
        'real-estate-data-pipeline=scripts.data_pipeline:main',
        'real-estate-deploy=scripts.deploy_app:main',
    ],
}

# Package data to include
PACKAGE_DATA = {
    'real_estate_intelligence_platform': [
        'config/*.yaml',
        'web_app/templates/*.html',
        'web_app/static/css/*.css',
        'web_app/static/js/*.js',
        'web_app/static/images/*',
        'web_app/static/images/icons/*',
    ],
}

# Additional files to include in the package
INCLUDE_PACKAGE_DATA = True

# Data files to include (external to package)
DATA_FILES = [
    ('config', ['config/database_config.yaml', 'config/model_config.yaml']),
    ('docs', ['docs/API_documentation.md', 'docs/User_Guide.md']),
]

# Extra requirements for different use cases
EXTRAS_REQUIRE = {
    'dev': [
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
        'pytest-mock>=3.10.0',
        'black>=23.0.0',
        'flake8>=6.0.0',
        'isort>=5.12.0',
        'mypy>=1.0.0',
        'pre-commit>=3.0.0',
        'sphinx>=6.0.0',
        'sphinx-rtd-theme>=1.2.0',
    ],
    'cloud': [
        'boto3>=1.26.0',
        'google-cloud-storage>=2.7.0',
        'azure-storage-blob>=12.14.0',
        'kubernetes>=25.0.0',
    ],
    'monitoring': [
        'prometheus-client>=0.16.0',
        'grafana-api>=1.0.3',
        'elasticsearch>=8.6.0',
        'kibana-api>=0.1.0',
    ],
    'deep-learning': [
        'tensorflow>=2.12.0',
        'torch>=2.0.0',
        'torchvision>=0.15.0',
        'transformers>=4.26.0',
    ],
    'nlp': [
        'spacy>=3.5.0',
        'nltk>=3.8.0',
        'textblob>=0.17.0',
        'transformers>=4.26.0',
    ],
    'geo': [
        'geopandas>=0.12.0',
        'folium>=0.14.0',
        'contextily>=1.3.0',
        'osmnx>=1.3.0',
    ],
    'all': [
        # Include all extras
    ]
}

# Flatten all extras for 'all' option
EXTRAS_REQUIRE['all'] = list(set(
    req for extra_reqs in EXTRAS_REQUIRE.values() 
    for req in extra_reqs if isinstance(req, str)
))

setup(
    # Basic package information
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    project_urls=PROJECT_URLS,
    
    # Package discovery and structure
    packages=find_packages(
        include=[
            'src',
            'src.*',
            'web_app',
            'web_app.*',
            'config',
            'scripts',
            'tests',
            'tests.*'
        ],
        exclude=[
            'notebooks',
            'data',
            'models',
            'logs',
            'docs._build',
            'deployment',
            'monitoring'
        ]
    ),
    
    # Package data and files
    package_data=PACKAGE_DATA,
    include_package_data=INCLUDE_PACKAGE_DATA,
    data_files=DATA_FILES,
    
    # Dependencies
    install_requires=read_requirements(),
    extras_require=EXTRAS_REQUIRE,
    python_requires=PYTHON_REQUIRES,
    
    # Entry points
    entry_points=ENTRY_POINTS,
    
    # Classification and metadata
    classifiers=CLASSIFIERS,
    keywords=' '.join(KEYWORDS),
    license=LICENSE,
    
    # Packaging options
    zip_safe=False,
    platforms=['any'],
    
    # Test configuration
    test_suite='tests',
    tests_require=EXTRAS_REQUIRE['dev'],
    
    # Package options
    options={
        'build': {
            'build_base': 'build',
        },
        'egg_info': {
            'tag_build': '',
            'tag_date': False,
        },
        'bdist_wheel': {
            'universal': False,
        },
    },
)

# Post-installation message
print("""
╔══════════════════════════════════════════════════════════════╗
║               Real Estate Intelligence Platform              ║
║                     Installation Complete!                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🏠 Advanced ML-powered real estate analytics platform      ║
║  📊 Price prediction & property recommendations             ║
║  🗺️ Market analysis & investment insights                   ║
║  🤖 MLOps integration with monitoring & deployment          ║
║                                                              ║
║  Quick Start:                                                ║
║  1. Copy .env.example to .env and configure                 ║
║  2. Run: real-estate-data-pipeline                          ║
║  3. Train models: real-estate-train                         ║
║  4. Start server: real-estate-server                        ║
║                                                              ║
║  Documentation: https://your-docs-url.com                   ║
║  Issues: https://github.com/your-repo/issues                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
