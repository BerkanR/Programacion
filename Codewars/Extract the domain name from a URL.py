# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

# For example:

# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

import re


def domain_name(url):
    if "www" not in url:
        return re.findall(r"[\w']+", url)[1]
    else:
        return url.split('.')[1]


assert (domain_name("http://github.com/carbonfive/raygun")) == "github", "Error en el dominio"
assert (domain_name("http://www.zombie-bites.com")) == "zombie-bites", "Error en el dominio"
assert (domain_name("https://www.cnet.com")) == "cnet", "Error en el dominio"