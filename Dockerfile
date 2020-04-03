FROM roboxes/centos8

LABEL "about"="This will build a RHEL6 image with density and all dependencies installed"
RUN mkdir /density-install
#VOLUME /density-install
COPY RPMS/ /density-install/
COPY start.sh /start.sh
#RUN yum -y install python-flask python-requests sqlite; yum clean all
RUN yum -y localinstall /density-install/noarch/app_a-1-0.noarch.rpm; yum clean all
RUN yum -y localinstall /density-install/noarch/app_b-1-0.noarch.rpm; yum clean all
EXPOSE 5000 5001
WORKDIR /opt/density
CMD /start.sh
