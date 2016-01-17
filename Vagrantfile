Vagrant.configure("2") do |config|
    #config.vm.box = "hashicorp/precise32"
    config.vm.box = "arvindr21/mean-box"
    config.vm.hostname = "rov-gg2016"
    config.vm.provision :shell, :path => "provision.sh"

    #config.vm.provision :file, source: "virtual_hosts/jh_laravel.conf", destination: "/etc/apache2/sites-available/jh_laravel.conf"
    #config.vm.provision :shell, inline: "a2ensite jh_laravel"
    #config.vm.provision :shell, inline: "service apache2 restart"
    config.vm.network :forwarded_port, host: 8888, guest: 8888
    config.vm.network :forwarded_port, host: 8080, guest: 8080
    config.vm.network :forwarded_port, host: 27017, guest: 27017
    config.vm.network :forwarded_port, host: 28017, guest: 28017
    #config.vm.network :forwarded_port, host: 4568, guest: 8081 #laravel
    #config.vm.network :forwarded_port, host: 4569, guest: 8082 #jh
    # http://stackoverflow.com/questions/21599728/apache-fails-to-start-on-vagrant
    #config.vm.provision "shell", inline: "service apache2 start", run: "always"
end
