from setuptools import setup, find_packages

setup(
    name="credit-approval-mlops",
    version="0.1.0",
    author="Santosh Ingle",
    description="End-to-end Credit Approval ML pipeline with MLOps",
    package_dir={"": "src"},          # 🔴 THIS IS THE KEY LINE
    packages=find_packages(where="src"),
    python_requires=">=3.9",
)
