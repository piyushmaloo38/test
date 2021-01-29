import os
import subprocess

os.getcwd()
os.system('mount /dev/cdrom /mnt ')
os.mkdir('local_repo')
os.system('touch /etc/yum.repos.d/local-dvdrom.repo')
os.system('chmod  u+rw,g+r,o+r  /etc/yum.repos.d/local-dvdrom.repo')
os.chdir('/mnt')
os.getcwd()
os.system('tar cvf - . | (cd /local_repo/; tar xvf -)')
os.chdir('/etc/yum.repos.d/')
with open('local-dvdrom.repo', 'w') as fp:
    filebuffer = ["[LocalRepo_BaseOS]","name=LocalRepo_BaseOS","metadata_expire=-1","enabled=1","gpgcheck=1","baseurl=file:///local_repo/BaseOS/","gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release","[LocalRepo_AppStream]","name=LocalRepo_AppStream","metadata_expire=-1","enabled=1","gpgcheck=1","baseurl=file:///local_repo/AppStream/","gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release"]
    fp.writelines("%s\n" % line for line in filebuffer)
    fp.close()

os.chdir('/mnt')
os.system('yum repolist')
os.system('yum install createrepo  yum-utils')
os.system('createrepo /local_repo/')
os.system('yum clean all')
os.system('yum repolist')
print('-----done creating yum repo-----')
exit()
