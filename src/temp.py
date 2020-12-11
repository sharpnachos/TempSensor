import subprocess
import time
import tweepy
import datetime
import calendar

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
    #found the temp sensor to be around 10-15 degrees off 
    tempF = tempF - 15
    ct = datetime.datetime.now() 
    ts = ct.timestamp() 
    ts = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    api.update_status("It is " + ts + "and the current temperature is " + str(tempF) + " degrees fahrenheit.")

main()