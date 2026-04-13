# use [] to obtain the value thats associated with a key.
info = {"name":"Sandy", "occupation":"manager"}
print(info["name"])

# if key is not present in the dictionnary, an error is raised. 
# print(info["job"])

# If the existence of a key is uncertain, test for it using the operator in 
if "job" in info: 
    print(info["job"])


# an easier strategy is to use the method get. 
# If the key is absent, the default value passed to get is returned 
print(info.get("job", None))

