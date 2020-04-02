FROM roboxes/centos6

LABEL "about"="This will build a RHEL6 image with density and all dependencies installed"
RUN mkdir /density-install
VOLUME /density-install
COPY RPMS/ /density-install/
#RUN yum -y install python-flask python-requests sqlite; yum clean all
RUN yum -y localinstall /density-install/noarch/app_a-1-0.noarch.rpm; yum clean all
EXPOSE 5000 5001
WORKDIR /opt/density
CMD bash /opt/density/etc/init.d/app_a.init start
