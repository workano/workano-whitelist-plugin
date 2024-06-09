### Set `rules` executable in windows
```shell
git ls-files --stage wazo/rules
git update-index --chmod=+x wazo/rules
```
### Enable debugging log in wazo
```shell
echo "debug: true" > /etc/wazo-plugind/conf.d/debug.yml
systemctl restart wazo-confd
```
### Install plugin
```shell
wazo-plugind-cli -c "install git https://github.com/workano/workano-whitelist-plugin.git"
```
### Uninstall plugin
```shell
wazo-plugind-cli -c "uninstall workano/wazo-confd-whitelist"
```

### Linux requirement
``curl``



