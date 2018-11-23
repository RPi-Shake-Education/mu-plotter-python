This code is a simple demonstration of taking and displaying real-time data from a raspberry Shake and displaying it using the plotter function in the Mu editor.

Currently the Shake will need to be configured to stream UDP packets to the IP address of the computer running Mu:

For example, if the ip address of the machine running Mu is 192.168.1.5, edit /opt/settings/user’/UDP-data-streams.conf

(note that there is also a UDP-data-streams.conf.tpl file - this is the templet, cot the actual config)

```{
    "UDP-destinations" : [
        { "dest" : "UDP-SHAKE-PI"},
        { "dest" : "UDP-NETWORK-PI"}
    ],

    "UDP-SHAKE-PI" : {
        "Hostname" : "UDPIPFILE:/opt/settings/sys/ip.txt",
        "Port" :         "54321"
    },

    "UDP-NETWORK-PI" : {
        "Hostname" : "192.168.1.5",
        "Port" :         "8889"
    }
}
```
