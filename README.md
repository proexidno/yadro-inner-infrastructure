1. Script:
```bash
python ./status.py <url>
```

2. Docker:
```bash
docker build -t name:tag .
docker run --name test -d name:tag (Optional)<url>
docker logs test
```

3. Ansible:
```bash
ansible-playbook -i inventory.ini playbook.yml --ask-pass --ask-become-pass
```
