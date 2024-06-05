sudo apt-get update
sudo apt-get install docker-compose

sudo apt get update
sudo apt-get install nginx

sudo apt install docker

sudo chmod 777 /var/run/docker.sock

cd /var/www/
git clone git@github.com:hsarbas/DRIVER2.0.git
sudo chmod 777 driver_new_tech/

cd ~
sudo rm -rf driver_new_tech/

cd /var/www/
sudo mkdir media
sudo chmod 777 media/
cd /var/www/media/
sudo mkdir incident_errorlog_data
sudo mkdir multi-language
sudo chmod 777 incident_errorlog_data/ multi-language/

(crontab -l ; echo "0 6 * * * /var/www/driver_new_tech/runcron.sh >> /var/www/driver_new_tech/finding_duplicate_records.log")| crontab -

(crontab -l ; echo "0 0 */7 * * /var/www/driver_new_tech/update_irap_data.sh >> /var/www/driver_new_tech/update_irap_data.log")| crontab -

(crontab -l ; echo "0 */6 * * * /var/www/driver_new_tech/bulk_upload.sh >> /var/www/driver_new_tech/bulk_log.log")| crontab -
