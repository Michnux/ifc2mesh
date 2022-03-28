import alteia



sdk = alteia.SDK(config_path='./config-connections.json')



# project = sdk.projects.search(filter={'name': {'$eq': 'ifc2mesh'}})[0]
# print(project.id)
# datasets = sdk.datasets.search(filter={'project': {'$eq': project.id}})
# print(len(datasets))
# print(datasets[2].__dict__)

# print([x.name for x in datasets])

cred = sdk.credentials.search()
creds = [x.name for x in cred]
print(creds)
# creds = [x for x in cred if x.name=='Michael de Lagarde']
# print(creds[0].__dict__)

# help(sdk.credentials.delete)
# sdk.credentials.delete(credential=creds[0].id, company='5c5c58a532bbdb4b66905abb')
