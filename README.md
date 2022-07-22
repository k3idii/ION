# IoN - Indicators of Normality


## The idea: 
this is just format specification.  NOT an implementation !
Like IOC.




## Rules like 
* sigma rules
* yara rules
* YAML based
* Swagger/OpenAPI 
* web-application profile for WAF

## Why: 
* human readable
* well-structured
* diff-able
* stored in repo as text files

## Implementation ?
Rules in this format can be later translated to solution-specific format. 
For example (Planned implementation / shortlist):
* Linux AppArmor
* Selinux
* Applocker
* Sysmon
* procmon
 

## Formats of data:

xxx.ion.yaml  = plaintext yaml <- source 
xxx.ion.json  = plaintext json 
xxx.ion.jwt   = JWT  ( to handle signed stuff )


## syntax:

* what is not allowed is ... not allowed :)
* allow list
* additinal block list (exclusion from white list)



# OPEN PROBLEMS: 

## DNS and resolve 
* passive tools will see IP connectivity in IP level not DNS
* os-level hooks - like socket::connect(...) - will see full domain name or IP
    * exception: when host resolution is performed manually !
* Potential solution: cache DNS queries on OS libs/logs level and re-use them


### possible solution (need review!):
Accually using "allow" keyword might be good idea => cause it self exmplain the intention of rule.

* allow to have a pair of directives: allow+block. Order: allow -> block 
```
section:
  allow: list-of-allowed-stuff
  block: list-of-blocked stuff

```
* allow+except || block+except:
```
section1:
  allow : /*
  except: *.exe 

section2:
  blocck: /tmp/*
  except: /tmp/magic/*
```




