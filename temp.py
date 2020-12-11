import subprocess
import time
import tweepy

auth = tweepy.OAuthHandler("w4J98Qk4qkD7yDAlVHb98p36b", "MnGJdovG5pdXUkETkxokGZTottP7G99p1mzLAYJULr7VI8JFkE")
auth.set_access_token("1302514377283731456-NqHIy9sBpxbdqIN9acZGzKbJpjTbT3", "HyVguC43mBsmpkaHuakb2yc9eI8KW1rNQ3PO40JewTyju")

api = tweepy.API(auth)

def main():
    bashCommand = "sudo i2cget -y 1 0x48"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    tempC = hexConvert(output)
    tempF = tempConvert(tempC)
    uploadToDB(tempF)
    tweet(tempF)
    print("Temp Recorded!")
    time.sleep(21600)
    main()

def hexConvert(output):
    tempC = int(output, 16)
    return tempC

def tempConvert(tempC):
    tempF = (tempC * 9/5) + 32
    return tempF

def uploadToDB(tempF):
    pass

def tweet(tempF):
    api.update_status("The current temperature is " + str(tempF) + " degrees farenheit.")

main()