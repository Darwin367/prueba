
Vagrant.configure("2") do |config|

  config.vm.synced_folder './' , '/home/sahlim/Escritorio/django1.11/aplicativo'

  #config.vm.synced_folder "/home/sahlim/Escritorio/platform/esvyda_platform", "/home/vagrant/esvyda_platform/"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 5432, host: 15432
  config.vm.network "forwarded_port", guest: 6600, host: 6600
  config.vm.network "forwarded_port", guest: 5500, host: 5500
  config.vm.network "forwarded_port", guest: 5555, host: 5555
end

Vagrant::Config.run do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"
end

