# Authentication & Production Server

## What is JWT?
- JWT stands for JSON Web Token.
- Its a compact and self-contained way for securely transmitting information between parties as a JSON object.
- The token can be verified and trusted because it is digitally signed.

## When should you use JSON Web Tokens?
- **Authorization**
  - When the user logged in each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token.
- **Information Exchange**
  - Because JWTs can be signed using public/private key pairs—you can be sure the senders are who they say they are

## JSON Web Token Structure
- JSON Web Tokens consist of three parts separated by dots (.), which are:
  - Header
  - Payload
  - Signature

JWT typically looks like the following.

<span style="color:#FB005B;">eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9</span>.</br><span style="color:#D53AFE;">eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ</span>.</br><span style="color:#6AD1F2;">SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c</span>

## Let's break down the different parts.
- ### **Header**
  - The header typically consists of two parts: 
    - The type of the token, which is JWT.
    - Signing algorithm being used, such as HMAC SHA256 or RSA.
```json
    {
    "alg": "HS256",
    "typ": "JWT"
    }
```

- ### **Payload**
  - The payload contains the claims. Claims are statements about an entity (typically, the user) and additional data.
  - There are three types of claims:
      1. Registered
         - These are a set of predefined claims which are not mandatory but recommended, to provide a set of useful, interoperable claims. Some of them are: **iss** (issuer), **exp** (expiration time), **sub** (subject), **aud** (audience). 
      2. Public
         - These can be defined at will by those using JWTs. But to avoid collisions they should be defined in the IANA JSON Web Token Registry or be defined as a URI that contains a collision resistant namespace. 
      3. Private claims
         - These are the custom claims created to share information between parties that agree on using them and are neither registered or public claims.
  - An example payload could be:
```json
    {
    "sub": "1234567890",
    "name": "John Doe",
    "admin": true
    }
```

- ### **Signature**
  - To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.
  - The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is.


---

# Production Server
 - If you want to run Django in production, be sure to use a production-ready web server like Nginx, and let your app be handled by a WSGI application server like Gunicorn.