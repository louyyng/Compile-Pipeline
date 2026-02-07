import os
import random
import string
import glob

def generate_junk_code():
    """Generates a valid C++ function containing random junk operations."""
    func_name = "poly_" + ''.join(random.choices(string.ascii_letters, k=8))
    
    # Generate some random math operations
    ops = []
    for _ in range(5):
        var = ''.join(random.choices(string.ascii_lowercase, k=4))
        val = random.randint(1, 1000)
        ops.append(f"    int {var} = {val};")
        ops.append(f"    {var} = {var} * {random.randint(2, 5)} + {random.randint(1, 100)};")
    
    code = f"\n\n// POLYMORPHIC JUNK CODE - GENERATED AUTOMATICALLY\n"
    code += f"#ifdef _WIN32\n" # Only compile on Windows to avoid cross-platform header issues if strict
    code += f"extern \"C\" __declspec(dllexport) void {func_name}() {{\n"
    code += "\n".join(ops)
    code += f"\n    volatile int entropy = {random.randint(1000, 9999)};\n"
    code += "}\n"
    code += f"#endif\n"
    
    return code

def polymorph_files(root_dir="."):
    """Scans for .cpp files and appends junk code to them."""
    print(f"[*] Starting Polymorphic Engine in: {root_dir}")
    
    cpp_files = glob.glob(os.path.join(root_dir, "**/*.cpp"), recursive=True)
    
    if not cpp_files:
        print("[!] No .cpp files found to modify.")
        return

    for file_path in cpp_files:
        # Skip files in hidden directories or build folders
        if ".git" in file_path or "node_modules" in file_path:
            continue
            
        print(f"    -> Injecting polymorphism into: {file_path}")
        
        junk = generate_junk_code()
        
        try:
            with open(file_path, "a") as f:
                f.write(junk)
        except Exception as e:
            print(f"    [!] Failed to write to {file_path}: {e}")

if __name__ == "__main__":
    polymorph_files()
