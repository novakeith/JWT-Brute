# JWTBrute.py

### Use this tool to brute force JWT tokens.

Variables that need to be set:
- myToken: the JWT token.
- myAlpha: the keyspace the program will iterate over
- myLength: the max guess length
- minLength: the minimum guess length

v2 will take keyword args from a command line to make this nicer to use.

## Usage:
`./jwtbrute.py MyJWTToken [keyspace] [min key length] [max key length] [-s for silent]`
