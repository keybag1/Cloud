az vm show --name KilliansVM \
  --resource-group KilliansResource \
  --query 'networkProfile.networkInterfaces[].id' \
  --output tsv

az group delete --name KilliansGroup --no-wait
az group wait --name KilliansGroup --deleted
