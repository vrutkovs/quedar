Self-hosted platform for meetups and RSVP
====

Run: `sudo docker run --rm -p 8080:8080 -ti vrutkovs/quedar`

Development:
```
sudo docker run --rm -v /root/.local/share/virtualenvs:/root/.local/share/virtualenvs -v `pwd`:/code -ti vrutkovs/quedar check
sudo docker run --rm -v /root/.local/share/virtualenvs:/root/.local/share/virtualenvs -v `pwd`:/code -ti vrutkovs/quedar install_dev
sudo docker run --rm -v /root/.local/share/virtualenvs:/root/.local/share/virtualenvs -v `pwd`:/code -ti vrutkovs/quedar pytest
```
