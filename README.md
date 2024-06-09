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
<!-- ### Install plugin
```shell
wazo-plugind-cli -c "install git https://github.com/connectino-platform/wazo-blacklist-plugin.git"
```
### Uninstall plugin
```shell
wazo-plugind-cli -c "uninstall connectino/wazo-confd-blacklist"
```

### Linux requirement
``curl``

### Configuration
Set the blacklist inquiry api url in `/etc/wazo-plugin-blacklist/blacklist_api_url`.
The address should be something like this `https://YOUR_DOMAIN.com/api/confd/1.1/blacklists/inquiry` -->



