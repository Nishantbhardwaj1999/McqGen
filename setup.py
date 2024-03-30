from setuptools import find_packages ,setup


setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Nishantbhardwaj',
    author_email='Nishantbhardwaj445@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)