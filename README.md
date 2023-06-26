# Discord-Token-Verification-Sorter
Sorts all tokens into categories (Email verified, phone verified, unclaimed, unverified, full verified)

## How To Run?
> 1) Clone / download this repository.
> 2) Open the folder in command prompt or terminal.
> 3) Run `pip install -r requirements.txt`.
> 4) Put proxies in  `proxies.txt`, format: `username:password@host:port` or `ip:port` if you wish to use proxies.
> 5) Put tokens in `tokens.txt`.
> 6) Run `python main.py`.

## Meaning of the acroynms used:
> - IV | Invalid | The token is invalid, it does not work 
> - UC | Unclaimed | The token does not have an email or a phone linked 
> - UV | Unverified | The token has an email linked, but it is not verified, it does not have a phone linked 
> - EV | Email Verified | The token has an email linked that is verified, it does not have a phone linked 
> - PV | Phone Verified | The token has an email linked, but it is not verified, it has a phone linked and verified 
> - FV | Full Verified | The token has both an email and a phone linked and verified 
