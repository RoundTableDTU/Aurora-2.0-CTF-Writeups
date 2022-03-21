In this challenge 10 qr frames were given , they were not together so i
made a qr merging all the 10 frames by:
```bash
$ convert 1.png 2.png 3.png 4.png 5.png 6.png 7.png 8.png 9.png 10.png -append QRcode1.png
```

Now zbarimag on the final qr to get the flag

```bash
❯ zbarimg QRcode1.png
QR-Code:}
QR-Code:flag
QR-Code:the_
QR-Code:isn't_
QR-Code:this_
QR-Code:but_
QR-Code:try_
QR-Code:nice_
QR-Code:{
QR-Code:$flag
```

Now just reformat the flag with aurora wrapper &
submitted

//complete