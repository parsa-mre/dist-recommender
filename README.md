1. create AWS public key
```
cd terraform
aws ec2 create-key-pair --key-name dist-rec --key-type rsa --query 'KeyMaterial' --output text > dist-rec.pem 
```
2. run terraform
```
terraform init
terraform apply
terraform output


terraform destroy
```
3. 
