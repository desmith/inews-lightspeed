# inews-lightspeed


- ami-0efb76882af9859da (CentOS 9 Stream)

TODO:

- Update packer configs to match current instance (lsphp, root/bin, etc)

1) load dotfiles from (git|s3) ?
3) Watchdog (watchdog) ?
4) Munin (munin-node) ?
5) Monit (monit) ?
6) date >> /var/log/cpu_hogs && ps -eo pcpu,pid,user,args | sort -r -k1 | head -5 >> /var/log/cpu_hogs
7) date >> /var/log/mem_hogs && ps -eo pmem,pid,user,args | sort -r -k1 | head -5 >> /var/log/mem_hogs

```bash
rsync -av /home/ec2-user/.local/share/omf/ .local/share/omf/
rsync -av /home/ec2-user/.dotfiles/ .dotfiles/
setup dotfiles {root,ec2-user}
chsh {root,ec2-user}
```

3) tag new ami with `inews-lightspeed` and `inews-lightspeed-<version_or_date>` ?
4) add ami_id to ssm parameter store (see scripts/99-post-build.py) for terraform to use (optional)


Notes:
Certbot auto renewal timer is not started by default.
amazon-ebs.packer-ebs: Run `systemctl start certbot-renew.timer` to enable automatic renewals.


Optional:

- create terraform to instantiate EC2 instance
