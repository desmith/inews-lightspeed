# inews-lightspeed


- ami-0efb76882af9859da (CentOS 9 Stream)

TODO:

1) Lose additional EBS volume

2) load dotfiles from (git|s3) ?

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
