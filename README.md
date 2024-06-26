# Avery Website

This is the official Avery House website. The branch `master` contains a very bare-bones version of the website which does not depend on any external APIs. The branch `maximal` contains a number of other features which are more maintenance-intensive, such as a music queue, a gallery which pulls photos from Facebook using the Facebook API, and an events page which pulls events from the Google calendar using the Google Calendar API.

## Updating on server,
We have a systemctl service just run `systemctl restart avery-website.service` to restart any changes. Also make sure to git pull on the server, don't do any code changes on the server, instead just do it locally, push to git and then git pull. When updating the constitution, just `git pull` in constitution folder and `cd ../` then run `pandoc constitution/constitution.md -o avery_website/templates/constitution-contents.html`.

You might get some weird errors so you might need to `git pull` on `sudo su -l www-data -s /bin/bash`, this is not ideal, but I am too lazy to actually figure out what is causing the error.

Also if you pull on your personal account, make sure to: `sudo chown -R www-data:webadmin ./*` in the git repo.

## Development setup:
First setup python:
### Python virtual environment (recommended)

If you choose not to use a virtual environment, you will need to install the dependencies in `requirements.txt` globally. Otherwise, proceed as follows (assuming `python` is Python 3)

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

### Running
Go to `avery_website/config.py` and comment out `SERVER_NAME='avery.caltech.edu'` then go back up a stage, aka `cd ../` and then run `./wsgi.py`.

## Server setup
Make sure to setup python first. Look at Development Setup.

To get a web server up and running using `nginx` with the default configuration:

### nginx installation and configuration

1. Install nginx (Ubuntu: `sudo apt install nginx`)
2. Copy the basic configuration file `avery-website.nginx.conf` to `/etc/nginx/sites-available`
3. Symlink the nginx configuration file to `sites-enabled`: `ln -s /etc/nginx/sites-available/avery-website.nginx.conf /etc/nginx/sites-enabled/`
4. Start and enable `nginx` (Ubuntu: `systemctl start nginx; systemctl enable nginx`)


### Running the web app

Finally, run `./run.sh` to start the web app.
