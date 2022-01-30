# JWTBrute.py

### Use this tool to brute force JWT tokens.

## Usage:
`./jwtbrute.py MyJWTToken [keyspace] [min key length] [max key length] [-s for silent]`
- MyJWTToken is the HS256 JWT token you want to crack. 
- keyspace is your alphabet that you want to use. By default this is lower and uppercase letters and all numbers, as well as special characters: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+`
- min key length is the shortest guess that should be iterated over
- max key length is the longest guess that should be iterated to
- use the -s flag for silent mode - won't output every 1000 guesses with an update, will only tell you upon success or failure.
