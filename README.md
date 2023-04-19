<h2><img src="https://cdn.discordapp.com/attachments/1074839843781218344/1098337611631837276/raspberrypi.png" alt="Raspberry Pi Logo" height="19px" width="auto"/> <b>Raspberry Pi Zero Door Lock</b></h2>
<h3>Repo Info:</h3>
<p>RPi Python script that locks / unlocks my door using the GPIO pins with a UI for small screens. Optimized for the RPi Zero WH. (NOT A DOOR PIN LOCK)</p>
<h3>Features:</h3>
<ul>
<li><code>/open</code> Endpoint built in.</li>
<li>Controlled by UI for touch screen displays like <a href="https://amzn.to/3GWaXhk">this</a> one.</li>
<li>Easy intergration with Home Assistant using the <code>/open</code> POST API endpoint.</li>
<li>Built in client and serverside rate limiting to disallow spamming the unlock button.</li>
<li>Unlock length can be changed in <code>main.py</code>.</li>
<li>Uses GPIO to lock / unlock door (requires a custom built door lock which should look something like the one from <a href="https://youtu.be/pBO0-xkMY0w?t=22"> The Amazing Spider-Man 2</a>).</li>
<li>Optimized for the <a href="https://amzn.to/41BLjGy">Raspberry Pi Zero</a>, but works with any <a href="https://amzn.to/3oqOkLI">Pi</a>.</li>
</ul>
<h3>Screenshots:</h3>
<img src="https://user-images.githubusercontent.com/80414685/233195166-a08e8c27-8d86-47f3-9572-dec642c7bebe.png" width="100%" alt="screemshot"/>
<h3>How it works:</h3>
<p>This is a Python code that runs on a Raspberry Pi to control a door lock. It uses the `RPi.GPIO` library to communicate with the GPIO pins on the Raspberry Pi and a web server to provide a user interface. The door can be unlocked for a specified duration of time by sending a POST request to the server.

The code starts by setting up the GPIO pin for the door lock and defining functions to open and close the door. The `open_door_for_seconds()` function opens the door for a specified number of seconds and then closes it. It uses the Tornado web framework to create a web server with two endpoints: `/` and `/open`.

The MainHandler class handles requests to the root URL and renders an HTML template with a button to open the door. The OpenDoorHandler class handles requests to the `/open` URL and calls `open_door_for_seconds()` with the specified duration.

When the button is clicked, a `POST` request is sent to the /open URL using jQuery's `$.ajax()` function. The button is temporarily disabled to prevent multiple clicks, and its background color is changed to green to indicate that the door is being unlocked. After the specified duration, the button is re-enabled, and its background color is restored to its original value. The SVG image inside the button is also updated to show a different icon when the door is unlocked.</p>

<h5><b>Original code by <a href="https://github.com/peaceman">peaceman</a></b>.</h5> 
