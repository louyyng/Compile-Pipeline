#include <windows.h>
#include <iostream>

int main() {
    std::cout << "Loading DLL..." << std::endl;

    // Attempt to load the DLL
    HMODULE hDll = LoadLibraryA("libcares-2.dll");

    if (hDll) {
        std::cout << "DLL Loaded Successfully." << std::endl;
        // Keep program alive to ensure thread finishes if needed
        Sleep(5000);
        FreeLibrary(hDll);
    }
    else {
        std::cout << "Failed to load DLL. Error: " << GetLastError() << std::endl;
    }

    return 0;
}