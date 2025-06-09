# Siemens SOA .NET DLL Python Stubs

This repository contains Python stub files (`.pyi`) generated for the Siemens Teamcenter SOA .NET API assemblies. These stubs provide type information, autocompletion support and docs when using the SOA API from Python, specifically with the [pythonnet](https://github.com/pythonnet/pythonnet) package.

## Purpose

The Siemens Teamcenter SOA (Service-Oriented Architecture) API is primarily distributed as a set of .NET assemblies (DLLs). While it's possible to use these DLLs in Python via `pythonnet`, doing so lacks native type hints, making development more difficult due to the absence of autocompletion, documentation, and static type checking.

This project bridges that gap by providing `.pyi` stub files for the SOA DLLs, enabling:

- **IDE autocompletion and intellisense** (in editors like VS Code or PyCharm)
- **Static type checking** with tools like `mypy`
- **Improved developer experience** when integrating Python with Teamcenter SOA
- **Documentation** parsed from .chm files

## Features

- Comprehensive stub coverage for key SOA .NET assemblies
- Compatibility with pythonnet-based workflows
- No runtime impact — the stubs are used only for development tooling

## Setup

1. Download stub files from this repository
2. Add them to VS code settings.json
   ```json
   {
       "python.analysis.extraPaths": ["C:\\PyTC-stubs\\tc14"],
       "python.languageServer": "Pylance",
   }
   ```

## Usage

1. Install `pythonnet` in your Python environment:

   ```bash
   pip install pythonnet
   ```
2. Load the required .NET dll from soa_client folder
    ```python
    import os

    for ref in os.listdir(r"C:\soa_client\net\libs"):
        try:
            if ref.endswith(".dll"):
                clr.AddReference(os.path.join(r"C:\soa_client\net\libs", ref))
        except Exception as e:
            pass
            #print(f"{e}")
    ```

3. Import required modules as such

    ```python
    from Teamcenter.Soa.Client import Connection
    from Teamcenter.Soa.Client.Model.Strong import User
    from Teamcenter.Schemas.Soa._2006_03.Exceptions import InvalidCredentialsException
    from Teamcenter.Services.Strong.Core import SessionService, DataManagementService
    ```

    Note that it is required to first load .NET dlls into memory, before doing any imports.

## Showcase

![image](https://github.com/user-attachments/assets/cbd17f8e-d79c-4aa1-99ae-12f9715a14bc)

![image](https://github.com/user-attachments/assets/568fe0b6-b945-44b7-854e-b5b5be6f524e)

![image](https://github.com/user-attachments/assets/8921a127-3042-4539-9503-d8c20e99cdfb)
