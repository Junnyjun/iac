# 1분마다 `terrafrom apply` 커맨드를 실행하는 스케줄러
from dotenv import load_dotenv
import os
import time

load_dotenv()

tenancy_ocid = os.getenv('tenancy_ocid')
user_ocid = os.getenv('user_ocid')
fingerprint = os.getenv('fingerprint')
private_key_path = os.getenv('private_key_path')
region = os.getenv('region')

def terraform_apply():
    os.system(f'terraform apply -var "tenancy_ocid={tenancy_ocid}" -var "user_ocid={user_ocid}" -var "fingerprint={fingerprint}" -var "private_key_path={private_key_path}" -var "region={region}" -auto-approve')

if __name__ == '__main__':
    print('Start Scheduler')
    print("TENANCY_OCID: ", tenancy_ocid)
    print("USER_OCID: ", user_ocid)
    print("FINGERPRINT: ", fingerprint)
    print("PRIVATE_KEY_PATH: ", private_key_path)
    print("REGION: ", region)

    while True:
        terraform_apply()
        time.sleep(10)


