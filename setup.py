from setuptools import setup, find_packages
```python
from setuptools import setup, find_packages
setup(
    name="ShGUI",
    version="1.0.0",  # رقم الإصدار
    description="A simple Python GUI library for beginners using tkinter and PIL & turtle",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="engineer shaimaa sileem ibrahim mohammed",
    author_email="eng.shaimaa.sileem@gmail.com",
    url="https://github.com/engineershaimaa/ShGUI_KW",  # رابط المشروع (GitHub مثلاً)
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Pillow>=9.0.0"  # مكتبة Pillow كاعتماد
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
