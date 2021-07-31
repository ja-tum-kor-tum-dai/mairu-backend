FROM centos:7

WORKDIR /installing/

# Install Python 3.8.10
RUN yum -y update
RUN yum install gcc openssl-devel bzip2-devel libffi-devel wget make epel-release python3-pip python3-devel -y
RUN yum -y groupinstall "Development Tools"
RUN wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
RUN tar xvf Python-3.8.10.tgz
RUN ./Python-3.8.10/configure --enable-optimizations
RUN make altinstall

WORKDIR /app/

COPY . .

RUN pip3 install -r requirements.txt

# Clean up
RUN rm -rf /installing

EXPOSE 11244