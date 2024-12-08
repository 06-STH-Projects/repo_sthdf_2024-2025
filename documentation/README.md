# SMVIT-AuroVision-Labs
![Python](https://img.shields.io/badge/Python-3.12-a?style=flat&logo=python&logoColor=white&labelColor=blue&color=black)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-a?style=flat&logo=fastapi&logoColor=white&labelColor=%23009688&color=black)
![Raspberry_PI](https://img.shields.io/badge/Raspberry%20PI-Pico-a?style=flat&logo=raspberrypi&logoColor=white&labelColor=%23A22846&color=black)

---

This is the full documentation for our project.

#### **Authors**

- Bc. Peter Slovák
- Bc. Tibor Vanek
- Bc. Pavol Hradský

We are a group of three enthusiastic students working together on an exciting project: **measuring the temperature of coffee or tea using a Raspberry Pi Pico**.

This is our first project which we decided to do together and we are all committed to contributing our skills and ideas to achieve great results. We will continue with project from previous years [Automated Tea Infuser | Overview | Wikifactory](https://wikifactory.com/+fablabbratislava/automated-tea-infuser) where students created an automated tea infuser.

---

### Key Improvements

- 📱 **Interactive web app**: Real-time notifications and customizable temperature thresholds.
- 📊 **View measurement history**: Easily track and review past temperature measurements for better insights.
- 🔍 **Enhanced accuracy**: Improved sensor placement for precise measurements directly in the drink.
- 🌐 **Mobile-Friendly**: Full functionality on desktops and mobile devices.

## **Thermo-measure**

### **Table of contents**

1. [Where it started](#where-it-started)
2. [Description](#description)
3. [Motivation](#motivation)
4. [Use Cases](#use-cases)
5. [EA modeling](#ea-modeling)
6. [Preparation of HW](#preparation-of-hw)
7. [Putting things together](#putting-things-together)
8. [Programming &amp; Deployment](#programming--deployment)
9. [Testing](#testing)
10. [Outcome](#outcome)
11. [Documentation and Videos](#documentation-and-videos)

### **Description**

Our project involves developing a **temperature measurement system** for coffee and tea using a Raspberry Pi Pico. The system will be placed directly on the cup and will measure the drink's temperature in **real-time**. Users will be able to view the temperature through a web application on their smartphones or computers. This allows for easy access and monitoring, enhancing the overall drinking experience.

### **Motivation**

We share a love for coffee and tea and know the struggle of sipping a too-hot beverage. Our solution aims to help users enjoy their drinks safely at the perfect temperature and will be for everyone, but especially for home usage.

Additionally, this project gives us the opportunity to learn new skills in technology and teamwork while making a positive impact on everyday life. By combining our interests in programming and electronics, we aim to design a product that not only enhances the drinking experience but also encourages others to think about the importance of temperature in their daily routines. At the end, we could test which drink (coffee or tea) cools down faster by measuring the time it takes for each beverage to reach a safe drinking temperature.


#### Prototype Sketch

<img src="/images/paperbook.jpg" width="75%">


#### Temperature measurement methods

There are several methods to measure the temperature of a beverage, and each has its own advantages and drawbacks. Below are a few common alternatives to using a Raspberry Pi Pico-based system for measuring temperature, along with a discussion of why we chose our approach.

1. **Thermal strips (Color-changing thermometers)** 9,91€:

   * **How it works** : These strips change color when exposed to heat. They are typically placed on the surface of a cup. The color change corresponds to different temperature ranges.
   * **Advantages** :
     * Simple to use, low cost and easy to apply.
     * Instant temperature indication without the need for any power source.
   * **Disadvantages** :
     * Limited accuracy, as the color change provides a rough estimate rather than an exact reading.
     * Not reusable or durable for long-term use.
     * Does not provide real-time temperature tracking, which is not ideal for ongoing monitoring.
   * **Why We Didn't Choose This Method** : While thermal strips are inexpensive and simple, they don't offer the precision, real-time monitoring or convenience of a digital system. The accuracy limitations and the lack of integration with a modern monitoring system like a smartphone app were significant drawbacks for our needs.
2. **Laser thermometers (Infrared thermometers)**  37,99 €:

   * **How it works** : These devices use infrared radiation to measure the temperature of a surface from a distance without making physical contact. The thermometer detects the infrared radiation emitted by the object and calculates its temperature.
   * **Advantages** :
     * Non-contact measurement, which means no risk of contamination or interference with the drink.
     * Provides fast and accurate temperature measuring.
   * **Disadvantages** :
     * Requires pointing the device at the surface, which could be cumbersome for continuous monitoring.
     * Can be relatively expensive compared to other methods.
     * Might not work well for liquid temperatures as infrared sensors are more accurate for solid surfaces, and measuring liquids can give inconsistent results.
   * **Why We Didn't Choose This Method** : Although laser thermometers offer non-contact measurements, we found them to be impractical for continuous real-time monitoring of a drink's temperature, especially when it's placed on a table or cup holder. Additionally, the cost and reliance on manual measurements made it less suitable for our goal of providing seamless, automatic, and remote temperature tracking.
3. **Contact Thermometers** :

   * **How it works** : These are traditional thermometers that use a metal probe to measure the temperature by physically contacting the liquid.
   * **Advantages** :
     * Very accurate and easy to use.
     * Can be relatively inexpensive and available in most household settings.
   * **Disadvantages** :
     * Direct contact with the beverage, which can affect hygiene and cleanliness.
     * Not ideal for continuous monitoring, as the user would need to insert and remove the probe each time they want a temperature measuring.

#### Why we chose the Raspberry Pi Pico-Based system

We decided to go with the **Raspberry Pi Pico-based temperature measurement system** for several key reasons:

* **Accuracy and Real-time monitoring** : With using a digital temperature sensor, we can achieve precise and real-time temperature measurements, allowing us to continuously monitor the beverage's temperature and send it to a web application. This provides users with an easy way to check the temperature remotely without needing to be physically near the drink.
* **User convenience** : Our system can automatically track the temperature and send notifications when the beverage has reached an optimal temperature, ensuring users avoid burning their mouths. This is far more user-friendly than manual temperature checks, which could disrupt the drinking experience.
* **Hygiene considerations** : Although our system involves contact with the cup, it eliminates the need for invasive or intrusive methods like probes or thermometers that must touch the beverage itself. The Raspberry Pi Pico-based system uses a temperature sensor placed directly on the cup, ensuring a balance between accuracy and hygiene. Moreover, the system does not require any direct interaction or contamination risk compared to probe thermometers.
* **Cost-effectiveness** : While the initial setup cost of a Raspberry Pi Pico and a temperature sensor might be slightly higher than alternatives like strips, the long-term benefits of real-time monitoring, data collection, and integration with a web app make it a more cost-effective solution overall.
* **Scalability and flexibility** : Our system can easily be expanded to monitor multiple cups simultaneously and can be integrated into various other smart home applications. The web application allows for greater customization and could be used to analyze data trends over time, such as the rate at which drinks cool down or the most preferred drinking temperatures. But this will be not a part of this school project now.

---

### Use Cases

1. **Safe Drinking Temperature Monitoring:** Users can check the temperature of their drinks before sipping, ensuring they don’t burn their mouths. This feature gives real-time updates on the temperature of coffee or tea, helping users avoid discomfort.
2. **Safe Drinking Temperature Notification:** Users get notification when coffee or tea has a desired temperature. This ensures that users can enjoy their beverages at the perfect temperature without having to constantly check. There will be set tresholds for notifying.
3. **Remote Monitoring for Multiple Drinks:** With the web application, users can monitor the temperature of multiple cups simultaneously, making it useful for gatherings or family settings.

#### SUB - use cases

1. Opening web app (UC3) - Drink enjoyers can open the web application via mobile or PC to access the interface of our web app where they can view the temperature measurement of their drinks. This use case is the beginning of the temperature checking process.
2. Set alerts threshold (UC2) - Users can set the desired temperature threshold for notifications. For example, they may configure the system to alert them when the temperature falls within a safe drinking range, such as 49°C to 60°C for coffee. This value can be re-set to another if beverage is still hot.
3. Measuring of temperature (UC1) - The system continuously measures the temperature of the beverage in real-time, displaying updates on the web application. This ensures that users have up-to-date information on the status of their drink.
4. Checking actual temperature (UC1) - Users can check the current temperature of their drinks at any given moment. This feature ensures that the user can quickly assess whether the beverage is safe to drink.
5. Preparing of beverages - This use case servers as an input/condition for our system, we need tho have beverage to measure prepared first.
6. Safe drinking of beverages (UC3) - Once the beverage has cooled to a safe temperature, users can enjoy it without the risk of burns. The system ensures that the drink is ready for consumption when the temperature is within the safe range.
7. Display measurement stats (UC1) - The system displays measurement statistics, such as the current temperature of the beverage, time of cooling from start. This allows users to monitor how their drink's temperature changes over time.
8. View temperature history (UC1) - Previous measurings can be seen.

   <img src="/images/usecase_connected.png" width="90%">

   <img src="/images/usecase_list.png" width="90%">

---

### EA modeling

* Business Process cooperation

<img src="/images/Business Process cooperation.jpg" width="50%">

* Motivation view

<img src="/images/Motivation View.png" width="50%">

* Technology view

<img src="/images/Technology VIEW.jpg" width="70%">

In terms of technology, our project leverages the Raspberry Pi Pico, a low-cost microcontroller, making it accessible for hobbyists and learners. The DS18B20 waterproof temperature sensor allows for accurate temperature readings in liquids, and the integration with a web application provides a user-friendly interface for interaction. The simplicity of using MicroPython for programming the Pico also enables future enhancements and modifications.

<img src="/images/usecase_detailed.png" width="100%">

<img src="/images/state_1.png" width="60%">

<img src="/images/state_2.png" width="60%">

---

### Preparation of HW

For this project, we needed to gather and prepare several essential components to ensure the temperature measurement system works correctly with the Raspberry Pi Pico. Below is a list of the hardware we purchased and prepared:

* **Metalized Resistor 4K7 - 0.125W:** This resistor is used as a pull-up resistor to stabilize the data line between the temperature sensor and the microcontroller.
* **Waterproof Temperature Sensor for Single-Board Computers (DS18B20):** The DS18B20 sensor is responsible for measuring the temperature of the liquid (coffee or tea) and can be easily interfaced with the Raspberry Pi Pico. Its waterproof feature makes it ideal for measuring the temperature of beverages.
* **Raspberry Pi Pico:** The Raspberry Pi Pico is the microcontroller at the heart of our system. It reads data from the DS18B20 sensor and sends it to the web app.
* **Breadboard:** The breadboard is used to connect the components (sensor, resistor, and Raspberry Pi Pico) without soldering, allowing for easy prototyping and testing.

  We followed the detailed instructions provided by [Random Nerd Tutorials](https://randomnerdtutorials.com/raspberry-pi-pico-ds18b20-micropython/) to set up the Raspberry Pi Pico with the DS18B20 temperature sensor. This guide helped us with wiring the components, installing the necessary libraries, and writing the MicroPython code to read temperature data from the sensor.

  Some components we had at home:

  1. Raspberry Pi Pico + Breadboard
  2. Powerbank to power our system
     
<div style="display: flex; flex-direction: row; gap: 10px;">
         <img src="/images/hardware/rpi,breadboard.jpg" alt="Rpi and breadbard" width="45%">
         <img src="/images/hardware/powerbank.png" alt="powerbank" width="45%">
</div>

Some components needed to be bought, and here are the links to where we purchased them:

1. Thermometer sensor: [Arduino teploměr vodotěsný DS18B20 | drotik-elektro.sk](https://www.drotik-elektro.sk/arduino-platforma/848-vodeodolny-teplomer-pre-jednodoskove-pocitace-ds18b20-1-meter.html)
2. Resistor: [Metalizovaný rezistor 4k7 0.125 W 1% | drotik-elektro.sk](https://www.drotik-elektro.sk/arduino-platforma/7663-metalizovany-rezistor-4k7-0-125w-1.html)

<div style="display: flex; flex-direction: row; gap: 10px;">
    <img src="/images/hardware/sensor.png" alt="Sensor" width="45%">
    <img src="/images/hardware/connectors.png" alt="Connectors" width="45%">
</div>

3. 3D printed box to contain our product

<div style="display: flex; flex-direction: row; gap: 10px;">
    <img src="/images/box/box1.png" alt="Sensor" width="45%">
    <img src="/images/box/box3.png" alt="Connectors" width="45%">
</div>

---

### Putting things together

Overall, our final product looks like this:

<img src="/images/hardware/final_product.png" width="60%">

Video about making parts together is available on the following link: [https://youtu.be/CCFt9_PZLs4](https://youtu.be/CCFt9_PZLs4 "https://youtu.be/CCFt9_PZLs4")

### Programming &amp; Deployment

**Raspberry**:

- raspberry is connected to Wi-Fi
- every 2 seconds the temperature is measured and a POST request is sent to server

**Server**:

- the server is in Python, an app using FastAPI
- has (POST) endpoint which, every 2 seconds, receives output from rpi about actual temperature
- temperature is written to global variables
- has (GET) endpoint which services this temperature

**Frontend**:

- simple frontend app (vanilla js + tailwind css)
- every 2 seconds a GET request is sent to the server, and the updated temperature is shown on frontend

<div style="display: flex; flex-direction: row; gap: 10px;">
    <img src="/images/schema1.png" alt="Sensor" width="45%">
    <img src="/images/schema2.png" alt="Connectors" width="45%">
</div>

###### Code For Microcontroller

```python
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ds18b20-micropython/

import machine, onewire, ds18x20, time
import urequests
import network

led = machine.Pin("LED", machine.Pin.OUT)
led.on()

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = 'Pixel 7'
password = '01189998819991197253'
wlan.connect(ssid, password, channel=12)

# Wait for connection
while not wlan.isconnected():
    wlan.connect(ssid, password, channel=12)
    time.sleep(1)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.1)
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.1)

ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    tempC = ds_sensor.read_temp(rom)
    print('temperature (ºC):', "{:.2f}".format(tempC))
    try:
        r = urequests.post("http://49.12.65.96/temperature", data="{\"temperature\": " + "{:.2f}".format(tempC) + "}")
        print(r.json())
        r.close()
    except:
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
  led.on()
  time.sleep(1)
  led.off()
  time.sleep(1)
```

###### Deployment of the Web App

Using Hetzner VPS (https://console.hetzner.cloud/) on IP 49.12.65.96 you can easily see our result:

<img src="/images/app/temp_history.png" width="100%">

Video about deploying web app on hetzner vps is recorded on the following link: https://youtu.be/vCuRECcbWYA

### Testing

Testing is a crucial part of our project:

1. **Functional testing** : Ensuring all components work together correctly, including the sensor, microcontroller, and web application.
2. **Temperature accuracy** : Comparing the readings from our system with a reliable thermometer to verify accuracy.
3. **User experience testing** : Gathering feedback from users on the web application’s interface and overall functionality.
4. **Durability testing** : Checking how the system performs over extended use and under varying conditions, such as different drink types and ambient temperatures.

Video about testing web app and our thermometer is recorded on the following link: https://youtu.be/J3pNO6BmosMOutcome

---

### **Outcome**

<img src="/images/hardware/final_outcome.png" width="60%">

---

### Documentation and Videos

> [!TIP]
> If you appreciate our efforts and would like to support our projects to the future, consider visiting us on social media listed below. Your support helps us acquire better equipment, fund new projects, and continue sharing our journey with the community 😊. Thank you for your support!

> [!NOTE]
> All steps in our project are documented and videos are uploaded to our YouTube channel, featuring an unlisted playlist. This playlist shows our progress, tutorials, and the challenges we faced. We hope this content inspires others to explore similar projects and learn alongside us!
>
> [Youtube][youtube-url]
>
> [LinkedIN][LinkedIN-url]
>
> [Patreon][patreon-url]

[youtube]: https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white
[youtube-url]: https://www.youtube.com/@AuroVisionLabs
[linkedin]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[LinkedIN-url]: https://www.linkedin.com/in/aurovision-labs
[patreon]: https://img.shields.io/badge/patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white
[patreon-url]: https://www.patreon.com/AuroVisionLabs