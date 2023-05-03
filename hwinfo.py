
import platform
import psutil
import socket

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

print("="*40, "HW Info", "="*40)

print("CPU:", platform.processor())

print("počet jáder:", psutil.cpu_count(logical=True))

svmem = psutil.virtual_memory()
print(f"velikost RAM: {get_size(svmem.total)}")


print("="*40, "OS Info", "="*40)

print("OS:", platform.system())

print("Verze:", platform.version())

print("uživatel:", platform.uname().node)


print("="*40, "informace o síti", "="*40)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("IP Addresa:", IPAddr)

print("Hostname:", hostname)
