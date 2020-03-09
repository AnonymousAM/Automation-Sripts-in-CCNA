import keyboard
import telnetlib as tn
import pyautogui as py

tn = tn.Telnet("192.168.0.200")

tn_read = tn.read_until('Username:'.encode('ascii'))
tn.write("admin".encode("ascii") + "\n".encode("ascii"))

tn.read_until('Password:'.encode('ascii'))
tn.write("123".encode("ascii") + "\n".encode("ascii"))

tn.write("enable".encode("ascii") + "\n".encode("ascii"))
tn.write("123\n".encode("ascii"))

device = ['r1', 'r2', 'r3', 'r4']
var = 33
# tn.write("r1".encode('ascii'))

for i in range(0, 4):
    tn.write(device[i].encode('ascii') + "\n".encode('ascii'))

    print(device[i])
    tn.write("\nclear line ".encode('ascii') + str(var).encode('ascii') + "\n".encode('ascii'))
    # keyboard.press_and_release()

    tn.write("\n".encode('ascii'))

   # keyboard.press_and_release('ctrl+shift+x')
   # keyboard.press_and_release('x')
    py.hotkey('ctrl','shift','6')
    py.press('x')
    var = var + 1

# tn.write("sh session\n".encode('ascii'))
tn.write("ls\n".encode("ascii"))
tn.write("exit\n".encode("ascii"))

print(tn.read_until('exit'.encode('ascii'), 10))
