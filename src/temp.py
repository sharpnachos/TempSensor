import subprocess
import time
import tweepy

auth = tweepy.OAuthHandler("X", "X")
auth.set_access_token("X","X")

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
    time.sleep(3600)
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
    api.update_status("The current temperature is " + str(tempF) + " degrees fahrenheit.")

main()