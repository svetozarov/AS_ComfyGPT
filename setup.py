from setuptools import setup, find_packages

setup(
    name="AS_ComfyGPT",
    version="0.1.0",
    description="A ComfyUI plugin that integrates ChatGPT using the OpenAI API.",
    author="Artem Svetozarov",
    author_email="art.svetozarov@gmail.com",
    url="https://github.com/svetozarov/AS_ComfyGPT",
    packages=find_packages(),
    install_requires=[
        "openai>=1.00.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
