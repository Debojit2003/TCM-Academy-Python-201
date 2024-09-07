from ctypes import *
from ctypes import wintypes


SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD


MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

"""
mov r10 , rcx
mov eax, 18h
syscall
ret

"""
def verify(x):
	if not x:
		raise WinError()
		
buf = create_string_buffer(b"\xb8\x05\x00\x00\x00\xc3")
buf_addr = addressof(buf)
print(hex(buf_addr))

VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.LPDWORD)
VirtualProtect.restype = wintypes.INT


old_protection = wintypes.DWORD(0)
protect = VirtualProtect(buf_addr, len(buf), PAGE_EXECUTE_READWRITE, byref(old_protection))
verify(protect)
#After commenting we will see that we are getting an access violation.


asm_type = CFUNCTYPE(c_int)
asm_function = asm_type(buf_addr)

r = asm_function()
print(hex(r))

buf2 = create_string_buffer(b"\x49\x89\xca\xb8\x18\x00\x00\x00\x0f\x05\xc3")
buf_addr2 = addressof(buf2)
print("Buffer address:", hex(buf_addr2))
old_protection = wintypes.DWORD(0)
protect = VirtualProtect(buf_addr2, len(buf2), PAGE_EXECUTE_READWRITE, byref(old_protection))
verify(protect)

syscall_type = CFUNCTYPE(NTSTATUS,  wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
syscall_function = syscall_type(buf_addr2)

handle = 0xffffffffffffffff
base_address = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
size = wintypes.ULONG(1024 * 24)

ptr2 = syscall_function(handle, byref(base_address), zero_bits, byref(size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if ptr2 != 0:
	print("error!")
	print(ptr)

print("Syscall allocation: ", hex(base_address.value))


input()