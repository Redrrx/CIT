# Introduction.
CIT for "Can I Talk"is a dummy solution to bypass video games voip restrictions, by isolating the voice chat relay to a vpn connection without affecting the in-game performance and latency, keep in mind that results may vary from machine to machine due numerous factors such as network stability and the total connections being made to the vpn, the current version is experimental and not complete.


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
the current version of CIT only works with Tom clancy's Rainbow six siege and PlayerUnknown Battlegrounds.
- Rainbow six has a stable connection to the voice chat servers depends on the time up of the vpn you're connected to, i'll talk about that below regarding using your own vpn

- PlayerUknown Battlegrounds voice chat works Only in EU/AS/SA servers using a France or German IP  it disconnects sometimes for some reasons i beleive its on their side.



# Download and usage.
- **CLOSE ALL GAMES BEFORE STARTING CIT !**
- **And don't forget to disable your firewall it might interfer.**
- **Run as administrator or the routing won't be done.**
- [DOWNLOAD](https://github.com/Redrrx/CIT/releases/download/EXP-V2/binaries-exp-v2.zip) extract and double click on CIT.exe and there you go launch your game and start yelling.


# Known issues.
- **"Nothing works its bullshit"**
check your permissions, CIT requires full admin privileges.
- **"the voice chat suddenly stops working"**
this is related to your connectivity to the VPN i can't help with that.
- **"the voice lags"**
well the voice chat bitrate is less than 64kb this is your net or the vpn nothing with the software. 

# Quick fix for VPN not launching 
Go to the vpn folder and set openvpn.exe to run as administrator this should fix it, a workaround for the current permissions issues to be fixed later.

# The To-Do list.

- [x] Tom clancy's rainbow six siege voice chat work.
- [X] Tweak few stability things.
- [X] PUBG voice chat work EU/AS/SA.
- [ ] League of legends voice chat fix.
- [ ] Fortnite voice chat fix.
- [ ] Clean that Junk code..
- [ ] find a better vpn solution.
- [ ] add H1Z1 voip bypass.
- [ ] add overwatch voip bypass.
- [ ] fix permissions issues.
- [ ] Make a Console version ps4/xb1.

# Using your own/another Openvpn server.
head over to /vpn/data/config/ you will find server.ovpn feel free to replace it but don't forget to add those additional configurations otherwise you won't isolate the voice chat servers to the vpn connection. 

not to forget that your openvpn server needs to accept routing configurations and doesn't force the entire gateway plus being hosted in a French or German IP.

Check for free and public Openvpn servers at http://vpngate.net don't forget to look for france and germany only.

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
