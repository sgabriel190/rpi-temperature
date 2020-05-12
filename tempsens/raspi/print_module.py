import time
import file_system_module

# Defining functions
def printToFile(humidity, temperature):
    file_system_module.cdToPath("home/pi/temp")
    try:
        f = open("log.txt", "a")
        text = " temperature:" + str(temperature) + "\thumidity:" + str(humidity) +  " \ttime:" + str(time.strftime("%H:%M:%S",time.localtime())) + "\n"
        f.write(text) 
        f.close()
    except:
        print("Log: Error opening local log file.")

# Formatted print for terminal
def myPrint(humidity, temperature):
    print("temperature:",temperature,"humidity:",humidity,"time:",time.strftime("%H:%M:%S",time.localtime()))
    
# Formatted print for html website
def htmlPrint(humidity, temparature):
    file_system_module.cdToPath("var/www/html")
    try:
        html_file = open("temp.html", "w")
        html_content= "<h1>Local temperature</h1><p>temperature: %s humidity: %s time: %s</p>" % (temperature, humidity, time.strftime("%H:%M:%S",time.localtime()))
        html_file.write(html_content)
        html_file.close()
    except:
        print("Log: Error writing in the html file.")
