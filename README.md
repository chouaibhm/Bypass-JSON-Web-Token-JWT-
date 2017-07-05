# Jwt-Bypass
###What is JSON Web Token?

JSON Web Token (JWT) is an open standard ([RFC 7519](https://tools.ietf.org/html/rfc7519)) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA.

A JSON Web Token [JWT] consists of three parts; an encoded Header, an encoded Payload and the Signature as shown below:


![Alt text](https://www.notsosecure.com/wp-content/uploads/2016/05/image001.png)

## Description
jWT-Br34k3r is an exploit for some APIs (API v2 ) today that implementing a more powerful security model using JSON Web Tokens.

jWT-Br34k3r enumurate existing users and then the  exploit will be with two ways :
  firstly : Brute Force Authorization Signature to get the securit Key and Create new Authorization with.
  secondly : Bypass Authorization JWT and Elevation of Privilege.


# Apache License
Copyright 2017 Chouaib Hm

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.








