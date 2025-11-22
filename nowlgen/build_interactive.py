#!/usr/bin/env python3
"""
Enhanced PyInstaller build script for NOWL Converter with interactive mode support
"""

import subprocess
import sys
import os
import site
from pathlib import Path

def find_owlready2_data():
    """Find owlready2 installation and its data files"""
    
    try:
        import owlready2
        owlready2_path = Path(owlready2.__file__).parent
        print(f"🔍 Found owlready2 at: {owlready2_path}")
        
        # Check for reasoners and other data
        data_items = []
        
        # Look for reasoners
        reasoners = ['pellet', 'hermit', 'fact++']
        for reasoner in reasoners:
            reasoner_path = owlready2_path / reasoner
            if reasoner_path.exists():
                data_items.append((str(reasoner_path), f"owlready2/{reasoner}"))
                print(f"  ✅ Found reasoner: {reasoner}")
        
        # Look for other data files
        for item in owlready2_path.iterdir():
            if item.is_file() and item.suffix in ['.jar', '.so', '.dll', '.dylib']:
                data_items.append((str(item), f"owlready2/{item.name}"))
                print(f"  ✅ Found data file: {item.name}")
        
        return data_items
        
    except ImportError:
        print("❌ owlready2 not found. Please install it first: pip install owlready2")
        return []

def create_console_spec():
    """Create a custom PyInstaller spec file for console application"""
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['cli/main.py'],
    pathex=[],
    binaries=[],
    datas=datas_list,
    hiddenimports=hidden_imports_list,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'PyQt5', 'PyQt6', 'PySide2', 'PySide6'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='nowl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Keep console window open
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    return spec_content

def build_executable():
    """Build standalone executable using PyInstaller with enhanced console support"""
    
    print("🔨 Building NOWL Converter executable with interactive mode...")
    
    # Check if main file exists
    main_file = "cli/main.py"
    if not os.path.exists(main_file):
        print(f"❌ Error: {main_file} not found!")
        print("Make sure you're running this from the project root directory.")
        return False
    
    # Get owlready2 data files
    owlready2_data = find_owlready2_data()
    
    # Base PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--name=nowl",
        "--clean",
        "--console",  # Explicitly specify console mode
        # Exclude some modules to reduce size
        "--exclude-module=tkinter",
        "--exclude-module=PyQt5",
        "--exclude-module=PyQt6",
        "--exclude-module=PySide2",
        "--exclude-module=PySide6",
        "--exclude-module=matplotlib.backends.backend_tkagg",
    ]
    
    # Add project data files
    data_dirs = ["generator"]  # Include generator package
    for data_dir in data_dirs:
        if os.path.exists(data_dir):
            if os.name == "nt":
                cmd.append(f"--add-data={data_dir};{data_dir}")
            else:
                cmd.append(f"--add-data={data_dir}:{data_dir}")
            print(f"📁 Including {data_dir} files...")
    
    # Add nowl files if they exist
    if os.path.exists("nowl"):
        if os.name == "nt":
            cmd.append("--add-data=nowl;nowl")
        else:
            cmd.append("--add-data=nowl:nowl")
        print(f"📁 Including nowl template files...")
    
    # Add owlready2 data files
    for src, dst in owlready2_data:
        if os.name == "nt":
            cmd.append(f"--add-data={src};{dst}")
        else:
            cmd.append(f"--add-data={src}:{dst}")
    
    # Add hidden imports - but exclude problematic readline modules on Windows
    hidden_imports = [
        "owlready2",
        "owlready2.reasoning", 
        "owlready2.driver",
        "networkx",
        "click",
        "generator",
        "generator.main",
        "generator.axiom2puml",
        "generator.rdf2puml",
        "generator.utils",
        "generator.utils.strings",
        "generator.utils.label",
        "generator.utils.error_msg",
        "ssl",
        "urllib3",
        "certifi",
        "webbrowser",
        "base64",
        "zlib",
        "atexit",    # For saving history on exit
        "glob",      # For file completion
        "shlex",     # For parsing quoted CLI arguments
    ]
    
    # Only add readline if it's not Windows or if it's working properly
    if os.name != "nt":
        hidden_imports.append("readline")
    else:
        # On Windows, be very selective about readline imports
        print("  🪟 Windows detected - handling readline carefully...")
        
        # Test if pyreadline3 is available and working
        pyreadline3_works = False
        try:
            import pyreadline3
            # Quick compatibility test
            import collections
            if hasattr(collections, 'abc'):  # Modern Python structure
                pyreadline3_works = True
                hidden_imports.extend([
                    "pyreadline3",
                    "pyreadline3.rlmain",
                    "pyreadline3.console"
                ])
                print("    ✅ pyreadline3 will be included")
        except Exception as e:
            print(f"    ⚠️  pyreadline3 not available: {e}")
        
        # Only add pyreadline if pyreadline3 isn't working and pyreadline is compatible
        if not pyreadline3_works:
            try:
                import pyreadline
                import collections
                # Check for the compatibility issue
                if hasattr(collections, 'Callable'):
                    hidden_imports.extend([
                        "pyreadline",
                        "pyreadline.rlmain",
                        "pyreadline.console"
                    ])
                    print("    ✅ pyreadline will be included (legacy)")
                else:
                    print("    ❌ pyreadline has compatibility issues - excluding")
            except Exception as e:
                print(f"    ⚠️  pyreadline not compatible: {e}")
        
        if not pyreadline3_works and "pyreadline" not in str(hidden_imports):
            print("    📝 No readline support - executable will use basic input mode")
    
    for imp in hidden_imports:
        cmd.append(f"--hidden-import={imp}")
    
    # Add the main file
    cmd.append(main_file)
    
    print("🔧 PyInstaller command:")
    print(" ".join(cmd))
    
    try:
        print("⏳ Running PyInstaller (this may take several minutes)...")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # Check if executable was created
        if os.name == "nt":
            exe_path = "dist/nowl.exe"
        else:
            exe_path = "dist/nowl"
            
        if os.path.exists(exe_path):
            print(f"✅ Build successful!")
            print(f"📦 Executable created: {exe_path}")
            print(f"💾 Size: {os.path.getsize(exe_path) / 1024 / 1024:.1f} MB")
            return True
        else:
            print("❌ Build failed - executable not found")
            if result.stdout:
                print("STDOUT:", result.stdout[-1000:])  # Last 1000 chars
            if result.stderr:
                print("STDERR:", result.stderr[-1000:])
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ PyInstaller failed with error:")
        print("STDOUT:", e.stdout[-1000:] if e.stdout else "None")
        print("STDERR:", e.stderr[-1000:] if e.stderr else "None")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller not found!")
        print("Install it with: pip install pyinstaller")
        return False

def create_wrapper_script():
    """Create a wrapper script that ensures proper console behavior"""
    wrapper_content = '''@echo off
title NOWL Generator
echo Starting NOWL Generator...
"%~dp0nowl.exe" %*
if %errorlevel% neq 0 (
    echo.
    echo Press any key to exit...
    pause >nul
)
'''
    
    wrapper_path = "dist/nowl_launcher.bat"
    try:
        with open(wrapper_path, 'w') as f:
            f.write(wrapper_content)
        print(f"📝 Created Windows launcher: {wrapper_path}")
        return True
    except Exception as e:
        print(f"⚠️ Failed to create launcher script: {e}")
        return False

def test_executable():
    """Test the built executable"""
    
    if os.name == "nt":
        exe_path = "dist/nowl.exe"
    else:
        exe_path = "dist/nowl"
    
    if not os.path.exists(exe_path):
        print("❌ Executable not found for testing")
        return False
    
    print("🧪 Testing executable...")
    
    try:
        # Test help command
        result = subprocess.run([exe_path, "--help"], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and "NOWL Generator" in result.stdout:
            print("✅ Executable test passed!")
            print("🎉 Your NOWL Converter is ready to use!")
            return True
        else:
            print("❌ Executable test failed")
            print(f"Return code: {result.returncode}")
            print(f"STDOUT: {result.stdout[:500]}")
            print(f"STDERR: {result.stderr[:500]}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Executable test timed out")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def create_readme():
    """Create a README file for the distribution"""
    readme_content = '''# NOWL Generator - Standalone Executable

## Quick Start

### Windows
1. Double-click `nowl.exe` to launch interactive mode
2. Or use `nowl_launcher.bat` for enhanced Windows experience
3. Or run from command line: `nowl.exe --help`

### Linux/Mac
1. Make executable: `chmod +x nowl`
2. Run: `./nowl` for interactive mode
3. Or: `./nowl --help` for command line options

## Interactive Mode

When you run the executable without arguments, it enters interactive mode:

- **object** or **o** - Generate object diagram
- **class** or **c** - Generate class diagram  
- **list** or **ls** - List available ontology files
- **help** or **h** - Show help
- **exit** or **quit** - Exit program

## Command Line Mode

```bash
# Generate object diagram from specific file
./nowl -f myontology.owl

# Generate class diagram
./nowl -c -e "MyClass:n,AnotherClass:ns"

# View generated diagram in browser
./nowl -f myontology.owl -v
```

## File Requirements

- Place your `.owl` or `.rdf` files in the same directory as the executable
- Generated `.puml` files will be saved in the current directory
- Use PlantUML online viewer or local installation to render diagrams

## Troubleshooting

- If the program closes immediately, try running from command line
- On Windows, use `nowl_launcher.bat` to keep console open
- Check that your ontology files are valid RDF/OWL format

For more information, visit: https://github.com/your-repo/nowl
'''
    
    readme_path = "dist/README.txt"
    try:
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        print(f"📚 Created README: {readme_path}")
        return True
    except Exception as e:
        print(f"⚠️ Failed to create README: {e}")
        return False

def main():
    print("🚀 NOWL Converter - Enhanced PyInstaller Build")
    print("=" * 55)
    
    # Check current directory
    if not os.path.exists("cli"):
        print("❌ Error: cli/ directory not found!")
        print("Please run this script from the nowl project root directory.")
        print(f"Current directory: {os.getcwd()}")
        sys.exit(1)
    
    # Check dependencies
    required_packages = ['owlready2', 'click', 'networkx']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} found")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} not found")
    
    if missing_packages:
        print(f"\n❌ Missing required packages: {', '.join(missing_packages)}")
        print(f"Install them with: pip install {' '.join(missing_packages)}")
        sys.exit(1)
    
    # Build executable
    if build_executable():
        # Create additional files for better user experience
        if os.name == "nt":
            create_wrapper_script()
        
        create_readme()
        
        # Test executable
        if test_executable():
            print("\n📋 Build Summary:")
            print("✅ Executable built successfully")
            print("✅ Interactive mode enabled")
            print("✅ Console support configured")
            print("✅ All tests passed")
            
            print("\n📋 Next steps:")
            print("1. Find your executable in the 'dist' folder")
            if os.name == "nt":
                print("2. For Windows: Use 'nowl_launcher.bat' or double-click 'nowl.exe'")
            else:
                print("2. For Linux/Mac: Run './nowl' from terminal")
            print("3. Place your .owl/.rdf files in the same directory")
            print("4. Enjoy the interactive NOWL Generator!")
            
        else:
            print("\n⚠️ Build completed but test failed.")
            print("The executable might still work - try running it manually.")
        
    else:
        print("\n❌ Build failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()