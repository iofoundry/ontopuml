#!/usr/bin/env python3
"""
Fixed PyInstaller build script for NOWL Converter with owlready2 support
Save as: build_exe_fixed.py
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
        print(f"📍 Found owlready2 at: {owlready2_path}")
        
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

def build_executable():
    """Build standalone executable using PyInstaller with owlready2 fixes"""
    
    print("🔨 Building NOWL Converter executable with owlready2 support...")
    
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
        # Exclude some modules to reduce size
        "--exclude-module=tkinter",
        "--exclude-module=PyQt5",
        "--exclude-module=PyQt6",
        "--exclude-module=PySide2",
        "--exclude-module=PySide6",
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
    
    # Add hidden imports
    hidden_imports = [
        "owlready2",
        "owlready2.reasoning", 
        "owlready2.driver",
        "networkx",
        # "matplotlib",
        # "matplotlib.backends.backend_agg",  # For matplotlib without GUI
        "click",
        "generator",
        "generator.main",
        "generator.axiom2puml",
        "generator.rdf2puml",
        "ssl",
        "urllib3",
        "certifi"
    ]
    
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
        
        if result.returncode == 0:
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

def main():
    print("🚀 NOWL Converter - PyInstaller Build (owlready2 Fixed)")
    print("=" * 55)
    
    # Check current directory
    if not os.path.exists("cli"):
        print("❌ Error: cli/ directory not found!")
        print("Please run this script from the nowl project root directory.")
        print(f"Current directory: {os.getcwd()}")
        sys.exit(1)
    
    # Check dependencies
    try:
        import owlready2
        print("✅ owlready2 found")
    except ImportError:
        print("❌ owlready2 not found. Install with: pip install owlready2")
        sys.exit(1)
    
    # Build executable
    if build_executable():
        # Test executable
        if test_executable():
            print("\n📋 Next steps:")
            print("1. Find your executable in the 'dist' folder")
            print("2. Copy it wherever you want to use it")
            print("3. Run it with: ./nowl --help")
        else:
            print("\n⚠️  Build completed but test failed.")
            print("The executable might still work - try running it manually.")
        
    else:
        print("\n❌ Build failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()