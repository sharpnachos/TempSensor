import subprocess
import time

def main():
    bashCommand = "sudo i2cget -y 1 0x48"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    tempC = hexConvert(output)
    tempF = tempConvert(tempC)
    uploadToDB(tempF)
    print("Temp Recorded!")
    time.sleep(21,600)
    main()

def hexConvert(output):
    tempC = int(output, 16)
    return tempC

def tempConvert(tempC):
    tempF = (tempC * 9/5) + 32
    return tempF

def uploadToDB(tempF):
    pass

main()