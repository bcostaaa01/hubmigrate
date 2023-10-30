from setuptools import setup, find_packages

setup(
    name="hubmigrate",
    version="1.0.1",
    description="An open-source Python library is designed to simplify the process of migrating data to HubSpot, a powerful customer relationship management (CRM) platform. Whether you're moving contacts, companies, deals, or any other data to HubSpot, this library provides an easy-to-use interface for managing your migration tasks.",
    author="bcostaaa01",
    author_email="bcostaaa01@gmail.com",
    install_requires=["pytest", "python-decouple"],
    packages=find_packages(),
    long_description=open("hubmigrate/README.md").read(),
    long_description_content_type="text/markdown",
)
