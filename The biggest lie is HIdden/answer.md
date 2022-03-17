## The biggest lie is hidden

In this we are presented with a webapp at https://akronsampleweb.000webhostapp.com/ .
In this webapp the / simply says "Akron Widgets Webiste Coming Soon!". Like most of the sites, this site also should have a robots.txt so going there we get a robots.txt which disallows all bots to map /admin.php
Going to /admin.php we get an admin panel login interface. Trying some basic sqli payloads, we get in using the payload `' or 1=1; #` in the username field.
After we are in we see a fake flag `$flag{hello_world}`. We also fuzzed the directories using gobuster, and got a /flag/. Going there we see directory indexing is enabled in that directory and we see a hello_world.php
Opening that, we see the flag `aurora{you_found_me_lol}` but this was also a fake flag. Asking for a hint from one of the admins we get that "Hint: Hello world is ur key to the flag".
This got us thinking. So we used cewl to scrape the website and all the known locations and made a wordlist out of it. After that we again fuzzed the directories and files using the custom wordlist and now we get a 200 on /hello_world.php
Going there we get the real flag.

Flag: `aurora{easy_injection}`
