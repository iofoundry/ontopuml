"""
Enhanced Main CLI entry point for NOWL generator command-line interface
Located in generator/cli/main.py
"""
import click
import os
import sys
from generator.main import rdf_to_puml, axiom_to_puml

# Enhanced readline support for command history and completion
# Use dynamic imports to avoid hard failures during packaging (PyInstaller)
# and to support multiple readline implementations on Windows.
import importlib
import pathlib

# Defaults
HAS_READLINE = False
readline = None

def _try_import(module_name):
    try:
        return importlib.import_module(module_name)
    except Exception:
        return None

# Try the platform-default 'readline' first (POSIX)
_mod = _try_import('readline')
if _mod:
    readline = _mod
    try:
        import atexit  # atexit is in stdlib; import normally
    except Exception:
        pass
    HAS_READLINE = True

# On Windows, try pyreadline3 then pyreadline if builtin isn't available
if os.name == 'nt' and not HAS_READLINE:
    for candidate in ('pyreadline3', 'pyreadline'):
        _mod = _try_import(candidate)
        if _mod:
            readline = _mod
            try:
                import atexit
            except Exception:
                pass
            HAS_READLINE = True
            break
    # If neither is available, provide a helpful message (don't raise)
    if not HAS_READLINE:
        # Note: avoid noisy output during automated builds; print only on interactive sessions
        if sys.stdout and sys.stderr and sys.stdin and sys.stdin.isatty():
            print("⚠️  Note: No readline support available on Windows.")
            print("   For enhanced interactive features, install: pip install pyreadline3")

# Fix for PyInstaller
if hasattr(sys, '_MEIPASS'):
    sys.path.insert(0, sys._MEIPASS)
    sys.path.insert(0, os.path.join(sys._MEIPASS, 'generator'))

# Global session configuration
SESSION_CONFIG = {
    'nowl_profile_path': './nowl/nowl.iuml'
}

def configure_include_path():
    """Configure NOWL include path for the session"""
    global SESSION_CONFIG
    
    print(f"\n📁 Current NOWL include path: {SESSION_CONFIG['nowl_profile_path']}")
    print("\n💡 This path is added to all generated PUML files as:")
    print(f"   !include {SESSION_CONFIG['nowl_profile_path']}")
    print()
    print("Common paths:")
    print("  ./nowl/nowl.iuml          # Default (local nowl folder)")
    print("  /path/to/nowl/nowl.iuml   # Absolute path")
    print("  ../shared/nowl.iuml       # Relative path")
    print("  none                      # No include statement")
    print()
    
    new_path = get_input_with_prompt("Enter new include path (or press Enter to keep current): ")
    
    if new_path.strip():
        if new_path.lower() == 'none':
            SESSION_CONFIG['nowl_profile_path'] = None
            print("✅ Include statement will be omitted from PUML files")
        else:
            # Normalize and expand user path to be cross-platform
            normalized = os.path.normpath(os.path.expanduser(new_path.strip()))
            SESSION_CONFIG['nowl_profile_path'] = normalized
            print(f"✅ Include path updated to: {SESSION_CONFIG['nowl_profile_path']}")
    else:
        print("✅ Keeping current path")

def get_current_profile_path():
    """Get the current include path for this session"""
    path = SESSION_CONFIG.get('nowl_profile_path', './nowl/nowl.iuml')
    if path is None:
        return None
    return os.path.normpath(os.path.expanduser(path))

def clear_screen():
    """Clear the terminal screen in a cross-platform way"""
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        # Fallback: print a bunch of newlines
        print('\n' * 100)

def setup_readline():
    global HAS_READLINE   # ✅ Declare first
    """Setup readline for command history and completion"""
    if not HAS_READLINE:
        return
    
    try:
        # History file setup
        history_file = os.path.join(os.path.expanduser("~"), ".nowl_history")
        
        # Load existing history
        try:
            readline.read_history_file(history_file)
            # Limit history size
            readline.set_history_length(1000)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"⚠️  Could not load command history: {e}")
        
        # Save history on exit
        def save_history():
            try:
                readline.write_history_file(history_file)
            except Exception:
                pass
        
        atexit.register(save_history)
        
        # Setup auto-completion
        setup_completion()
        
        # Configure readline behavior
        readline.parse_and_bind("tab: complete")
        readline.parse_and_bind("set show-all-if-ambiguous on")
        readline.parse_and_bind("set completion-ignore-case on")
        
        # Enable Vi or Emacs mode based on preference
        try:
            readline.parse_and_bind("set editing-mode emacs")
        except:
            pass
            
    except Exception as e:
        # If readline setup fails, disable it gracefully
        # global HAS_READLINE
        HAS_READLINE = False
        print(f"⚠️  Readline setup failed: {e}")
        print("   Continuing with basic input mode...")

def setup_completion():
    """Setup command auto-completion"""
    if not HAS_READLINE:
        return
    
    try:
        # Available commands for completion
        commands = [
            'help', 'h', '?',
            'object', 'o',
            'class', 'c', 
            'list', 'ls', 'files',
            'status', 'info',
            'clear',
            'exit', 'quit', 'q',
            'history',
            'cd',
            'pwd'
        ]
        
        def completer(text, state):
            """Auto-completion function"""
            try:
                options = []
                
                # Complete commands
                if not text or text.startswith(('', ' ')):
                    options = [cmd for cmd in commands if cmd.startswith(text.lower())]
                
                # Complete file names for certain commands
                if any(text.startswith(cmd) for cmd in ['object', 'class', 'o', 'c']):
                    try:
                        files = find_ontology_file()
                        options.extend([f for f in files if f.startswith(text.split()[-1])])
                    except:
                        pass
                
                # Complete file paths
                try:
                    import glob
                    # Accept either OS separator or common forward/back slashes typed by users
                    if any(sep in text for sep in (os.path.sep, '/', '\\')) or text.endswith('.'):
                        options.extend(glob.glob(text + '*'))
                except:
                    pass
                
                if state < len(options):
                    return options[state]
                return None
            except Exception:
                return None
        
        readline.set_completer(completer)
        
    except Exception as e:
        # If completion setup fails, continue without it
        pass

def print_welcome():
    """Print welcome message and instructions"""
    print("="*60)
    print("🚀 Welcome to NOWL Generator!")
    print("   NIST OWL to PlantUML Converter")
    print("="*60)
    print()
    print("This tool converts RDF/OWL ontology files into PlantUML diagrams.")
    print("You can generate both object diagrams and class diagrams.")
    print()
    print("🎯 Quick Start:")
    print("• Place your .owl or .rdf file in the current directory")
    print("• Run commands interactively or use command-line options")
    print("• Generated .puml files will be saved in the current directory")
    print()
    if HAS_READLINE:
        print("⌨️  Enhanced Features:")
        print("• Use ↑/↓ arrow keys for command history")
        print("• Use Tab for auto-completion")
        print("• Use Ctrl+C to interrupt, Ctrl+D or 'exit' to quit")
    else:
        print("📝 Basic Input Mode:")
        print("• Command history and auto-completion not available")
        if os.name == "nt":
            print("• For enhanced features, install: pip install pyreadline3")
    print()
    print("⚠️  NOWL Include Path Configuration:")
    print("• Default: ./nowl/nowl.iuml")
    print("• You can specify a custom path for your NOWL include files")
    print("• Type 'config' to set a custom include path")
    print()
    print("Type 'help' for available commands or 'exit' to quit.")
    print("-"*60)

def print_help():
    """Print available commands and options"""
    print()
    print("📚 Available Commands:")
    print()
    print("🎮 Simple Interactive Commands:")
    print("  help, h, ?        - Show this help message")
    print("  object, o         - Generate object diagram")
    print("  class, c          - Generate class diagram")
    print("  list, ls, files   - List available ontology files")
    print("  config            - Configure NOWL include path")
    print("  status, info      - Show current settings")
    print("  history           - Show command history")
    print("  clear             - Clear screen")
    print("  cd <directory>    - Change directory")
    print("  pwd               - Show current directory")
    print("  version           - Show version")
    print("  exit, quit, q     - Exit the program")
    print()
    print("⚡ CLI-Style Commands (with flags):")
    print("  -f file.owl                   - Object diagram from specific file")
    print("  -c -e \"Person:n,Student:ns\"   - Class diagram with entities")
    print("  -f file.owl -l spring         - Object diagram with layout")
    print("  -f file.owl -v                - Object diagram with visualization")
    print("  --file=file.owl --view        - Long flag format")
    print("  --nowl-profile=path           - Set NOWL include path")
    print()
    if HAS_READLINE:
        print("⌨️  Keyboard Shortcuts:")
        print("  ↑/↓ arrows       - Navigate command history")
        print("  Tab              - Auto-complete commands/files")
        print("  Ctrl+C           - Interrupt current operation")
        print("  Ctrl+D           - Exit program")
        print("  Ctrl+L           - Clear screen")
        print()
    print("🚀 Available Flags:")
    print("  -f, --file FILE               Input ontology file")
    print("  -c, --class-diagram           Generate class diagram")
    print("  -e, --class-entity TEXT       Class entities (e.g., 'Person:n,Student:ns')")
    print("  -a, --axiom-type CHOICE       Axiom type (n/s/ns/t)")
    print("  -l, --layout CHOICE           Layout algorithm")
    print("  -i, --import-ontology FILE    Additional ontologies to import")
    print("  --exclude-relation IRI        Relations to exclude")
    print("  --inline-class                Inline class declarations")
    print("  --nowl-profile PATH           NOWL include file path")
    print("  -v, --view                    Visualize generated PUML")
    print("  --plantuml-server URL         PlantUML server URL")
    print()
    print("💡 Examples:")
    print("  Simple style:")
    print("    object myfile.owl")
    print("    class Person:n,Student:ns")
    print("    config                       # Set include path")
    print()
    print("  CLI style:")
    print("    -f pizza.owl")
    print("    -c -e \"Pizza:n,Topping:ns\" -f pizza.owl")
    print("    -f pizza.owl --nowl-profile=../shared/nowl.iuml")
    print("    --file pizza.owl --nowl-profile=none  # No include")
    print()

def find_ontology_file():
    """Find ontology file in current directory"""
    ontology_extensions = ['.owl', '.rdf']
    files = []
    
    for file in os.listdir('.'):
        if any(file.lower().endswith(ext) for ext in ontology_extensions):
            files.append(file)
    
    return files

def list_ontology_files():
    """List all available ontology files"""
    files = find_ontology_file()
    if files:
        print(f"\n📁 Found {len(files)} ontology file(s):")
        for i, file in enumerate(files, 1):
            size = os.path.getsize(file) / 1024  # KB
            print(f"  {i}. {file} ({size:.1f} KB)")
    else:
        print("\n❌ No ontology files (.owl, .rdf) found in current directory.")
    return files

def select_file_interactive(files):
    """Let user select a file interactively"""
    if len(files) == 1:
        print(f"\n✅ Using: {files[0]}")
        return files[0]
    
    # Show numbered file list
    print(f"\n📁 Found {len(files)} ontology files:")
    for i, file in enumerate(files, 1):
        try:
            size = os.path.getsize(file) / 1024  # KB
            print(f"  {i}. {file} ({size:.1f} KB)")
        except OSError:
            print(f"  {i}. {file}")
    
    while True:
        try:
            choice = input(f"\nSelect file (1-{len(files)}) or filename: ").strip()
            
            # Try to parse as number
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(files):
                    return files[idx]
                else:
                    print(f"❌ Please enter a number between 1 and {len(files)}")
                    continue
            except ValueError:
                pass
            
            # Try as filename
            if choice in files:
                return choice
            
            # Try with extension
            for ext in ['.owl', '.rdf']:
                if choice + ext in files:
                    return choice + ext
            
            print("❌ File not found. Please try again.")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)

def get_input_with_prompt(prompt="🔧 nowl> "):
    """Get user input with readline support"""
    try:
        if HAS_READLINE:
            return input(prompt).strip()
        else:
            return input(prompt).strip()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except EOFError:
        print("\n\n👋 Goodbye!")
        sys.exit(0)

def show_history():
    """Show command history if readline is available"""
    if not HAS_READLINE:
        print("❌ Command history not available (readline not installed)")
        return
    
    try:
        history_length = readline.get_current_history_length()
        if history_length == 0:
            print("📝 No command history yet")
            return
        
        print(f"📝 Command History ({history_length} entries):")
        print("-" * 40)
        
        # Show last 20 commands
        start = max(1, history_length - 19)
        for i in range(start, history_length + 1):
            try:
                cmd = readline.get_history_item(i)
                if cmd:
                    print(f"  {i:3d}: {cmd}")
            except:
                pass
                
    except Exception as e:
        print(f"❌ Error accessing history: {e}")

def change_directory(path=None):
    """Change current directory"""
    if path is None:
        path = input("📁 Enter directory path: ").strip()
    
    if not path:
        print("❌ No path provided")
        return
    
    try:
        # Expand user directory (~)
        path = os.path.expanduser(path)
        
        if os.path.exists(path) and os.path.isdir(path):
            os.chdir(path)
            print(f"✅ Changed to: {os.getcwd()}")
            # Update file list after changing directory
            files = find_ontology_file()
            if files:
                print(f"📁 Found {len(files)} ontology file(s) in new directory")
            else:
                print("📁 No ontology files found in new directory")
        else:
            print(f"❌ Directory not found: {path}")
            
    except PermissionError:
        print(f"❌ Permission denied: {path}")
    except Exception as e:
        print(f"❌ Error changing directory: {e}")

def run_object_diagram_interactive(filename=None):
    """Run object diagram generation interactively"""
    print("\n🎯 Generating Object Diagram")
    print("-" * 30)
    
    if filename:
        # File specified in command
        if not os.path.exists(filename):
            print(f"❌ File not found: {filename}")
            return
        selected_file = filename
    else:
        # Interactive file selection
        files = find_ontology_file()
        if not files:
            print("❌ No ontology files found in current directory.")
            print("💡 Use 'cd' to change directory or 'list' to see files")
            return
        
        selected_file = select_file_interactive(files)
    
    try:
        print(f"\n⚡ Processing {selected_file}...")
        puml_content, output_path = rdf_to_puml(
            input_rdf=selected_file,
            nowl_profile_path=get_current_profile_path(),
            save_puml=True
        )
        
        if output_path:
            print(f"✅ Object diagram generated: {os.path.basename(output_path)}")
            print(f"📍 Location: {output_path}")
        else:
            print("✅ Object diagram generated successfully!")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def run_class_diagram_interactive(class_spec=None):
    """Run class diagram generation interactively"""
    print("\n🎯 Generating Class Diagram")
    print("-" * 30)
    
    files = find_ontology_file()
    if not files:
        print("❌ No ontology files found in current directory.")
        return
    
    # Select file
    selected_file = select_file_interactive(files)
    
    # Get class entities
    if class_spec:
        class_input = class_spec
    else:
        print("\nℹ️ Enter class entities in format: ClassName:type")
        print("   Types: n=necessary, s=sufficient, ns=both, t=taxonomy")
        print("   Example: MyClass:n,AnotherClass:ns")
        print("   (Use Tab for auto-completion)")
        
        class_input = get_input_with_prompt("Class entities: ")
        if not class_input:
            print("❌ No class entities provided.")
            return
    
    try:
        print(f"\n⚡ Processing {selected_file}...")
        class_entities_list, types_list = parse_class_entities(class_input)
        
        puml_content, output_path = axiom_to_puml(
            ontology=selected_file,
            class_entities=list(zip(class_entities_list, types_list)),
            nowl_profile_path=get_current_profile_path(),
            save_puml=True
        )
        
        if output_path:
            print(f"✅ Class diagram generated: {os.path.basename(output_path)}")
            print(f"📍 Location: {output_path}")
        else:
            print("✅ Class diagram generated successfully!")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def parse_cli_command(command_line):
    """Parse CLI-style commands with flags in interactive mode"""
    import shlex
    
    # Normalize backslashes to forward slashes for cross-platform compatibility
    command_line = command_line.replace('\\', '/')
    
    try:
        # Use shlex to properly parse quoted arguments
        parts = shlex.split(command_line)
    except ValueError:
        # Fallback to simple split if shlex fails
        parts = command_line.split()
    
    if not parts:
        return None, {}, []
    
    # Check if first part is a flag (for cases like "-i file.rdf" or "-f file.rdf")
    if parts[0].startswith('-'):
        # If it starts with a flag, there's no explicit command
        command = None
        args = parts
    else:
        command = parts[0]
        args = parts[1:]
    
    # Parse flags and options
    flags = {}
    remaining_args = []
    i = 0
    
    while i < len(args):
        arg = args[i]
        
        if arg.startswith('--'):
            # Long flag
            if '=' in arg:
                key, value = arg[2:].split('=', 1)
                flags[key] = value
            else:
                key = arg[2:]
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    flags[key] = args[i + 1]
                    i += 1
                else:
                    flags[key] = True
        elif arg.startswith('-') and len(arg) > 1:
            # Short flag
            flag_char = arg[1:]
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                flags[flag_char] = args[i + 1]
                i += 1
            else:
                flags[flag_char] = True
        else:
            # Regular argument
            remaining_args.append(arg)
        
        i += 1
    
    return command, flags, remaining_args

def handle_cli_style_command(command_line):
    """Handle CLI-style commands with flags"""
    command, flags, args = parse_cli_command(command_line)
    
    if command is None and not flags:
        return False
    
    # Handle nowl include path configuration
    nowl_profile = flags.get('nowl-profile')
    if nowl_profile is not None:
        global SESSION_CONFIG
        if isinstance(nowl_profile, str) and nowl_profile.lower() == 'none':
            SESSION_CONFIG['nowl_profile_path'] = None
            print("✅ NOWL include disabled for this session")
        else:
            # Normalize the provided path
            try:
                normalized = None if nowl_profile is None else os.path.normpath(os.path.expanduser(str(nowl_profile)))
            except Exception:
                normalized = nowl_profile
            SESSION_CONFIG['nowl_profile_path'] = normalized
            print(f"✅ NOWL include path set to: {normalized}")
    
    # Handle nowl-style commands
    if command and command.lower() == 'nowl':
        # Extract the actual command if "nowl" prefix is used
        if args:
            actual_command = args[0]
            remaining_args = args[1:]
        else:
            actual_command = None
            remaining_args = []
    else:
        actual_command = command
        remaining_args = args
    
    # Check if only -i (import) is provided without main file
    import_ontologies = flags.get('i') or flags.get('import-ontology', [])
    if import_ontologies and not (flags.get('f') or flags.get('file')):
        print("❌ An input file must be specified with -f.")
        print("💡 Usage: -f ontology.owl -i additional.owl")
        return True
    
    # If there's an import but we have a file, proceed. If no file and no import, continue with auto-detection
    # File processing
    input_file = flags.get('f') or flags.get('file')
    
    # Auto-detect file if not specified
    if not input_file and remaining_args:
        # Check if any remaining arg is a file
        for arg in remaining_args:
            if arg.endswith(('.owl', '.rdf')) and os.path.exists(arg):
                input_file = arg
                remaining_args.remove(arg)
                break
    
    # Check if this is a diagram generation command that requires a file
    needs_file = (
        flags.get('c') or flags.get('class-diagram') or 
        flags.get('e') or flags.get('class-entity') or
        actual_command in ['class', 'c', 'object', 'o'] or
        import_ontologies  # If import is specified, file is needed
    )
    
    # Auto-select file only if a diagram command was requested
    if not input_file and needs_file:
        files = find_ontology_file()
        if len(files) == 1:
            input_file = files[0]
            print(f"📄 Auto-selected: {input_file}")
        elif len(files) > 1:
            print("❌ Multiple files found. Specify with -f or place single file in directory")
            print("📁 Available files:")
            for i, f in enumerate(files, 1):
                try:
                    size = os.path.getsize(f) / 1024
                    print(f"  {i}. {f} ({size:.1f} KB)")
                except OSError:
                    print(f"  {i}. {f}")
            return True
        else:
            print("❌ No ontology files found")
            return True
    
    # If no file is needed (e.g., only --nowl-profile), return early
    if not input_file and not needs_file:
        return True
    
    try:
        # Only process diagrams if we have an input file
        if not input_file:
            return True
        
        # Class diagram handling
        if flags.get('c') or flags.get('class-diagram') or actual_command in ['class', 'c']:
            class_entities = flags.get('e') or flags.get('class-entity')
            axiom_type = flags.get('a') or flags.get('axiom-type')
            layout = flags.get('l') or flags.get('layout')
            
            # If no entities specified but command is class, ask for them
            if not class_entities:
                if remaining_args:
                    class_entities = ' '.join(remaining_args)
                else:
                    print("❌ Class entities required. Use -e 'Person:n,Student:ns' or 'class Person:n,Student:ns'")
                    return True
            
            print(f"⚡ Generating class diagram from {input_file}")
            class_entities_list, types_list = parse_class_entities(class_entities, axiom_type)
            print_class_entities_summary(class_entities_list, types_list)
            
            puml_content, output_path = axiom_to_puml(
                ontology=input_file,
                class_entities=list(zip(class_entities_list, types_list)),
                layout_type=layout,
                nowl_profile_path=get_current_profile_path(),
                save_puml=True
            )
            
            if output_path:
                print(f"✅ Class diagram: {os.path.basename(output_path)}")
                print(f"📍 Location: {output_path}")
            
        # Object diagram (default)
        else:
            layout = flags.get('l') or flags.get('layout')
            inline_class = flags.get('inline-class', False)
            # import_ontologies already extracted in validation above
            if isinstance(import_ontologies, str):
                import_ontologies = [import_ontologies]
            
            exclude_relation = flags.get('exclude-relation', [])
            if isinstance(exclude_relation, str):
                exclude_relation = [exclude_relation]
            
            print(f"⚡ Generating object diagram from {input_file}")
            puml_content, output_path = rdf_to_puml(
                input_rdf=input_file,
                import_ontologies=import_ontologies,
                exclude_relation=exclude_relation,
                layout_type=layout,
                inline_class_declaration=inline_class,
                nowl_profile_path=get_current_profile_path(),
                save_puml=True
            )
            
            if output_path:
                print(f"✅ Object diagram: {os.path.basename(output_path)}")
                print(f"📍 Location: {output_path}")
        
        # Handle visualization
        if flags.get('v') or flags.get('view'):
            if output_path and os.path.exists(output_path):
                server_url = flags.get('plantuml-server', "http://www.plantuml.com/plantuml/img/")
                success = visualize_puml(output_path, server_url)
                if not success:
                    print_plantuml_server_help()
            else:
                print("❌ No output file to visualize")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return True

def interactive_mode():
    """Run the CLI in interactive mode with support for both simple and CLI-style commands"""
    # Setup readline features
    setup_readline()
    
    print_welcome()
    
    while True:
        try:
            command_line = get_input_with_prompt()
            
            if not command_line:
                continue
            
            # Check if it's a CLI-style command (contains flags)
            if '-' in command_line and any(part.startswith('-') for part in command_line.split()):
                if handle_cli_style_command(command_line):
                    continue
                else:
                    break
            
            # Parse as simple interactive command
            parts = command_line.split()
            command = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
            
            if command in ['exit', 'quit', 'q']:
                print("\n👋 Thank you for using NOWL Generator!")
                break
                
            elif command in ['help', 'h', '?']:
                print_help()
                
            elif command in ['object', 'o']:
                filename = args[0] if args else None
                run_object_diagram_interactive(filename)
                
            elif command in ['class', 'c']:
                class_spec = ' '.join(args) if args else None
                run_class_diagram_interactive(class_spec)
                
            elif command in ['list', 'ls', 'files']:
                list_ontology_files()
                
            elif command in ['status', 'info']:
                print(f"\n📊 Current Status:")
                print(f"   Working directory: {os.getcwd()}")
                files = find_ontology_file()
                print(f"   Ontology files found: {len(files)}")
                include_path = get_current_profile_path()
                if include_path:
                    print(f"   NOWL include path: {include_path}")
                else:
                    print(f"   NOWL include: disabled")
                
                # Show readline status
                if HAS_READLINE:
                    try:
                        hist_len = readline.get_current_history_length()
                        print(f"   Enhanced input: enabled ({hist_len} history entries)")
                    except:
                        print(f"   Enhanced input: enabled")
                else:
                    print(f"   Enhanced input: disabled")
                    if os.name == "nt":
                        print(f"   To enable: pip install pyreadline3")
                
            elif command == 'config':
                configure_include_path()
                
            elif command in ['history', 'hist']:
                show_history()
                
            elif command in ['clear']:
                clear_screen()
                print_welcome()
                
            elif command == 'cd':
                path = ' '.join(args) if args else None
                change_directory(path)
                
            elif command == 'pwd':
                print(f"📁 Current directory: {os.getcwd()}")
                
            elif command == 'version':
                try:
                    from generator import __version__, __author__
                    print(f"🚀 NOWL Generator v{__version__}")
                    if __author__:
                        print(f"👨‍💻 Author: {__author__}")
                except ImportError:
                    print("🚀 NOWL Generator")
                
            else:
                print(f"❌ Unknown command: '{command}'")
                print("💡 Type 'help' to see available commands.")
                print("💡 Use Tab for auto-completion of commands and files.")
                print("💡 You can also use CLI-style commands with flags (e.g., '-f file.owl -c -e Person:n')")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Goodbye!")
            break

def parse_class_entities(class_entity_string, axiom_type=None):
    """Parse comma-separated class entities string into lists of entities and types."""
    if not class_entity_string:
        raise ValueError("No class entity string provided")
    
    valid_types = ['n', 's', 'ns', 't']
    class_entities_list = []
    types_list = []
    warnings = []
    
    # Split by comma and process each entity
    entities = [entity.strip() for entity in class_entity_string.split(',')]
    
    for entity in entities:
        # Skip empty strings
        if not entity:
            continue
            
        # Split on the last colon to handle IRIs that may contain colons
        parts = entity.rsplit(':', 1)
        
        if len(parts) == 2:
            entity_name, entity_type = parts
            entity_name = entity_name.strip()
            entity_type = entity_type.strip()
            
            if entity_type in valid_types:
                class_entities_list.append(entity_name)
                types_list.append(entity_type)
            else:
                warnings.append(
                    f"Invalid type '{entity_type}' for class entity '{entity_name}'. "
                    f"Type must be one of {valid_types}. Skipping this entity."
                )
        else:
            # If no type is provided, use the default from axiom_type
            if axiom_type and axiom_type in valid_types:
                class_entities_list.append(entity.strip())
                types_list.append(axiom_type)
            else:
                warnings.append(
                    f"No type specified for class entity '{entity}' and no valid default "
                    f"axiom type provided. Skipping this entity."
                )
    
    # Print warnings
    for warning in warnings:
        print(f"⚠️ Warning: {warning}")
    
    if not class_entities_list:
        raise ValueError("No valid class entities found after parsing")
    
    return class_entities_list, types_list

def print_class_entities_summary(class_entities_list, types_list):
    """Print a summary of the class entities being processed."""
    print(f"📋 Processing {len(class_entities_list)} class entities:")
    for i, (cls, typ) in enumerate(zip(class_entities_list, types_list)):
        print(f"  {i+1}. {cls} (type: {typ})")

def visualize_puml(puml_file, server_url):
    """Visualize PUML file using PlantUML server"""
    try:
        import urllib.parse
        import base64
        import zlib
        import webbrowser
        
        # Read PUML file
        with open(puml_file, 'r', encoding='utf-8') as f:
            puml_content = f.read()
        
        # Encode for PlantUML server
        compressed = zlib.compress(puml_content.encode('utf-8'))
        encoded = base64.b64encode(compressed).decode('ascii')
        
        # Create URL
        url = f"{server_url}{encoded}"
        
        # Open in browser
        webbrowser.open(url)
        print(f"🌐 Opened visualization in browser: {puml_file}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to visualize: {e}")
        return False

def find_recent_puml_file():
    """Find most recently created PUML file"""
    puml_files = []
    for file in os.listdir('.'):
        if file.endswith('.puml'):
            stat = os.stat(file)
            puml_files.append((file, stat.st_mtime))
    
    if puml_files:
        # Sort by modification time, newest first
        puml_files.sort(key=lambda x: x[1], reverse=True)
        return puml_files[0][0]
    
    return None

def print_plantuml_server_help():
    """Print help for PlantUML visualization"""
    print("🌐 PlantUML Visualization Help:")
    print("   • Visit http://www.plantuml.com/plantuml/")
    print("   • Copy and paste your .puml file content")
    print("   • Or use a local PlantUML installation")

class IRIParamType(click.ParamType):
    name = "IRI"
    def convert(self, value, param, ctx):
        return value

IRI = IRIParamType()

@click.command(
    context_settings={
        "ignore_unknown_options": True,
        "help_option_names": ["--help"],
        "terminal_width": 100,
    }
)
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    expose_value=True,
    help="Show version information and exit."
)
@click.option(
    "--help",
    is_flag=True,
    is_eager=True,
    expose_value=True,
    help="Show this help message and exit."
)
@click.option(
    "-f", "--file",
    help="(optional) Input ontology file. Supported formats: .rdf, .owl.\n"
    "If not provided, the tool will search for an ontology file in the current directory.",
)
@click.option(
    "-i", "--import-ontology",
    multiple=True,
    help="(optional) Additional ontologies to import. You can provide multiple ontologies.",
)
@click.option(
    "-c", "--class-diagram",
    is_flag=True,
    help="(optional) Generates a class diagram. By default, only an object diagram will be generated.",
)
@click.option(
    "-e", "--class-entity",
    type=str,
    help="(optional) Comma-separated list of class entities to include in the diagram.\n"
    "Format: <class_name1>:<type1>,<class_name2>:<type2>,...\n"
    "Types: 'n' (necessary), 's' (sufficient), 'ns' (necessary & sufficient), 't' (taxonomy)\n"
    "Example: -e \"MyClass1:n,MyClass2:ns,MyClass3:t\""
)
@click.option(
    "--include-class",
    default=[],
    type=IRI,
    help="(optional) List of classes to include in the object diagram. " \
    "If -c is set, only axioms from these classes are included in the class diagram. " \
    "Expect full IRIs. " \
    "Multiple classes can be provided by --class-entity (should be then entities as label of the argument). "
    "--class-included is a filter for object diagram, only those instances are included in the diagram which has a class in the given list as type. " \
    "If not used, no such filter is applied and all individuals are considered.",
)
@click.option(
    "--exclude-relation",
    multiple=True,
    type=IRI,
    help="(optional) List of relations to exclude between instances in the object diagram. " \
    "Has no effect on class diagrams." \
    "This is a filter only for object diagram, these relations if provided are excluded from the diagram"
)
@click.option(
    "-a","--axiom-type",
    type=click.Choice(["n", "s", "ns", "t"]),
    help="(optional) Determines which axioms to include in the class diagram.",
)
@click.option(
    "-l", "--layout",
    type=click.Choice([
        "spring", "circular", "kamada_kawai", "spectral", "shell", 
        "planar", "random", "bipartite", "multipartite", "up", "u", "down", "d", "left", "l", "right", "r"
    ]),
    help="(optional) Specifies the layout algorithm to use.",
)
@click.option(
    "--inline-class",
    is_flag=True,
    help="(optional) Use inline class declaration for individuals in object diagrams.",
)
@click.option(
    "-v", "--view",
    is_flag=True,
    help="(optional) Visualize the generated PUML file using a PlantUML server.",
)
@click.option(
    "--plantuml-server",
    default="http://www.plantuml.com/plantuml/img/",
    help="(optional) URL of the PlantUML server to use for visualization.",
)
@click.option(
    "--nowl-profile",
    help="(optional) Path to NOWL include file. Use 'none' to disable include statement.",
)
@click.option(
    "--interactive", "-int",
    is_flag=True,
    help="Launch interactive mode."
)
def main(
    file, import_ontology, class_diagram, class_entity, include_class,
    exclude_relation, axiom_type, layout, inline_class, view, 
    plantuml_server, nowl_profile, help, version, interactive
):
    """NOWL Generator - Convert RDF/OWL ontologies to PlantUML diagrams"""
    
    if version:
        try:
            from generator import __version__, __author__
        except ImportError:
            # Fallback when running as standalone executable
            __version__ = "0.2.20251121"
            __author__ = "NIST"
        click.echo(f"🚀 NOWL Generator v{__version__}")
        if __author__:
            click.echo(f"👨‍💻 Author: {__author__}")
        raise SystemExit(0)
        
    if help:
        click.echo(click.get_current_context().get_help())
        raise SystemExit(0)

    # Set global include path if specified
    if nowl_profile is not None:
        global SESSION_CONFIG
        if isinstance(nowl_profile, str) and nowl_profile.lower() == 'none':
            SESSION_CONFIG['nowl_profile_path'] = None
        else:
            try:
                SESSION_CONFIG['nowl_profile_path'] = None if nowl_profile is None else os.path.normpath(os.path.expanduser(str(nowl_profile)))
            except Exception:
                SESSION_CONFIG['nowl_profile_path'] = nowl_profile

    # If no arguments provided or interactive flag, launch interactive mode
    if interactive or (not file and not class_entity and not include_class and not import_ontology):
        interactive_mode()
        return
    
    # Check if only -i (import) is provided without main file
    if import_ontology and not file and not class_entity and not include_class:
        click.echo("❌ An input file must be specified with -f.")
        click.echo("💡 Usage: nowlgen -f ontology.owl -i additional.owl")
        return

    # Find input file if not provided
    if file is None:
        click.echo("🔍 No input file provided. Searching for an ontology file in the current directory...")
        files = find_ontology_file()
        if not files:
            click.echo("❌ No ontology file found. Abort!")
            return
        file = files[0]  # Use first found file
        click.echo(f"✅ Using found ontology file: {file}")

    output_path = None
    puml_content = None

    try:
        if class_diagram:
            # Process class diagram
            if class_entity:
                try:
                    class_entities_list, types_list = parse_class_entities(class_entity, axiom_type)
                    print_class_entities_summary(class_entities_list, types_list)

                    puml_content, output_path = axiom_to_puml(
                        ontology=[file] + list(import_ontology),
                        class_entities=list(zip(class_entities_list, types_list)),
                        layout_type=layout,
                        nowl_profile_path=get_current_profile_path(),

                    )
                except ValueError as e:
                    click.echo(f"❌ Error parsing class entities: {e}")
                    return
                    
            elif include_class:
                # Legacy support
                class_entities_list, types_list = parse_class_entities(class_entity, axiom_type)
            
                if axiom_type:
                    puml_content, output_path = axiom_to_puml(
                        ontology=file,
                        class_entities=include_class,
                        types=axiom_type,
                        layout_type=layout,
                        nowl_profile_path=get_current_profile_path(),
                    )
                else:
                    click.echo("❌ When using --include_class, you must also specify --axiom-type.")
                    return
            else:
                click.echo("❌ No class entities provided. Use --class-entity or --include_class options.")
                return
        else:
            # Process object diagram
            puml_content, output_path = rdf_to_puml(
                input_rdf=file,
                import_ontologies=import_ontology,
                exclude_relation=list(exclude_relation),
                layout_type=layout,
                inline_class_declaration=inline_class,
                nowl_profile_path=get_current_profile_path(),
            )
        
        # Handle visualization if requested
        if view and puml_content:
            # Find the PUML file to visualize
            if not output_path or not os.path.exists(output_path):
                output_path = find_recent_puml_file()
                if output_path:
                    click.echo(f"🔍 Using most recently created PUML file: {output_path}")

            if output_path:
                success = visualize_puml(output_path, plantuml_server)
                if not success:
                    print_plantuml_server_help()
            else:
                click.echo("❌ No PUML file found to visualize.")
        elif view:
            click.echo("❌ No PUML content generated to visualize.")
            
    except FileNotFoundError as e:
        click.echo(f"❌ {e}", err=True)
        raise click.Abort()
    except ImportError as e:
        click.echo(f"❌ Import Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"❌ Unexpected Error: {e}", err=True)
        raise click.Abort()

    # Keep terminal open after processing in standalone mode
    if output_path:
        print(f"\n✅ Process completed successfully!")
        print(f"📁 Output file: {output_path}")
        print(f"📍 Location: {os.path.abspath(output_path)}")
        
        # Ask user if they want to do more
        try:
            choice = input("\n🔄 Would you like to process another file? (y/N): ").strip().lower()
            if choice in ['y', 'yes']:
                interactive_mode()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")

if __name__ == "__main__":
    main(prog_name="nowl")