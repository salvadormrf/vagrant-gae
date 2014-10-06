#!/usr/bin/env ruby
Vagrant.require_version '>=1.6.0'

Vagrant.configure("2") do |config|
	
	# box options
	config.vm.provider :virtualbox do |virtualbox|
		virtualbox.customize ["modifyvm", :id, "--memory", 2048]
		virtualbox.customize ["modifyvm", :id, "--cpus", 2]
    end
    
    # update host OS hosts file
    config.hostmanager.enabled = true
    config.hostmanager.manage_host = true
  	
    # devbox
    config.vm.define :devbox do |node|
    	
    	# box
        node.vm.box = "vagrant-gae"
        node.vm.box_url = 'https://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-i386-vagrant-disk1.box'
		
        # post deploy messages
        node.vm.post_up_message = "Run: vagrant ssh\nand after: ./demo_app/run.sh"
        
		# set hostname
		node.vm.hostname = "demo-app.dev"
        
        # network
        node.vm.network :private_network, ip: "192.168.100.120"
        
    end
    
    # provisioning
    config.vm.provision :ansible do |ansible|
        ansible.playbook = "ansible/playbook/site.yml"
        ansible.inventory_path = "ansible/inventory/vagrant"
        ansible.verbose = "vvvv"
        ansible.limit = 'all'
    end
    
end

#
# # vagrant plugin install vagrant-hostmanager
#
# remove existing keys
# ssh-keygen -R demoapp.dev 
# ssh-keygen -R 192.168.100.120
#
#
# Hacks, patches (ubuntu 12 and some for 14)
#
# ansible-playbook ansible/playbook/site.yml -i ansible/inventory/vagrant -vvvv
#
# install new dependencies
#pip install -r {{ project.pip_requirements }}
#pip install PIL==1.1.7 --allow-external PIL --allow-unverified PIL
#
#sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib
#sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib
#sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib
#
# http://www.turnkeylinux.org/docs/virtualization/udev-persistent-net-generation
# echo -n > /etc/udev/rules.d/70-persistent-net.rules
#
# gunzip < /vagrant/resources/dumps/demoapp.sql.gz | mysql -uroot -proot demoapp
#
# sudo pico demoapp/tools/google_appengine/google/appengine/tools/devappserver2/watcher_common.py
# _IGNORED_DIRS = ('.git', '.hg', '.svn', 'mode_modules')


#
