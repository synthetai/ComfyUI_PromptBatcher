from setuptools import setup, find_packages

setup(
    name="comfyui_prompt_batcher",
    version="0.1.0",
    description="A ComfyUI custom node for batch processing prompts from text files",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 