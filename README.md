by isolating the voice chat relay to a vpn connection without affecting the in-game performance and latency, keep in mind that results may vary from machine to machine due numerous factors such as network stability and the total connections being made to the vpn.

This software is targeted for a specific audience which is any resident from the following countries:

- Algeria 
- Tunisia 
- Saudi Arabia 
- Egypt 
- United Arab Emirates 
- Bengladesh 

that's alot of silenced players, fixed that for your boys.

# Using a normal VPN software.
<p align="center"> 
<img src="https://i.imgur.com/XZRB7Je.png">
</p>

                                       

# Using CIT.
<p align="center"> 
<img src="https://i.imgur.com/VOs6LS4.png">
</p>
                                             


# Regarding the current version.
the current version of CIT only works with Tom clancy's Rainbow six siege PlayerUnknown Battlegrounds.
- Rainbow six has a stable connection to the voice chat servers depends on the time up of the vpn you're connected to, i'll talk about that below regarding using your own vpn

- PlayerUknown Battlegrounds voice chat works Only in EU/AS/SA servers using a France or German IP  it disconnects sometimes for some reasons i beleive its on their side.


# Using your own/another Openvpn server.
head over to /vpn/data/config/ you will find server.ovpn feel free to replace it but don't forget to add those additional configurations otherwise you won't isolate the voice chat servers to the vpn connection. 


```
tap-sleep 3
route-delay 1 3
route-nopull
route 18.0.0.0 255.0.0.0
route mpx5j.vivox.com
route disp-rbswp-5-1.vivox.com
route 169.45.201.128
route api.ipify.org
resolv-retry infinite
nobind
persist-key
persist-tun
client
verb 3
```


