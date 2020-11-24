serial = "s10/x69"

values = serial.split('/')

distance = values[0].replace('s', '')
ldr = values[1].replace('x', '')

print('Distance: ' + distance + '\n' +
        'LDR: ' + ldr)